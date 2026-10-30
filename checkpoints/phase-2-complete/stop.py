# Ready-made for Phase 1. Do not change it.
# Stop only the app recorded by start.py, including its reload worker.
import json
import os
from pathlib import Path
import shlex
import signal
import socket
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parent
STATE = ROOT / ".server.json"


def free(port):
    # A wildcard listener can coexist with a reused loopback bind on macOS.
    with socket.socket() as probe:
        probe.settimeout(0.2)
        if probe.connect_ex(("127.0.0.1", port)) == 0:
            return False
    with socket.socket() as sock:
        if os.name != "nt":
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            sock.bind(("127.0.0.1", port))
            return True
        except OSError:
            return False


def recorded_process(pid, port):
    """Refuse a stale record whose process id now belongs to another command."""
    if os.name == "nt":
        result = subprocess.run(
            ["powershell", "-NoProfile", "-NonInteractive", "-Command",
             f"(Get-CimInstance Win32_Process -Filter 'ProcessId={pid}').CommandLine"],
            capture_output=True, text=True, check=True)
    else:
        result = subprocess.run(["ps", "-p", str(pid), "-o", "command="],
                                capture_output=True, text=True)
        if not result.stdout.strip():
            return False
        if os.getpgid(pid) != pid:
            raise ValueError
    command = shlex.split(result.stdout.strip(), posix=os.name != "nt")
    expected = ["run", "uvicorn", "app:app", "--host", "127.0.0.1", "--port", str(port), "--reload"]
    if not command:
        return False
    executable = command[0].strip('"').replace("\\", "/").rsplit("/", 1)[-1].lower()
    if executable not in ("uv", "uv.exe") or command[1:] != expected:
        raise ValueError
    return True


def main():
    if not STATE.exists():
        print("The app is not running from start.py.")
        return 0
    try:
        state_text = STATE.read_text(encoding="utf-8")
        state = json.loads(state_text)
        pid, port = state["pid"], state["port"]
        if type(pid) is not int or pid <= 1 or type(port) is not int or not 1 <= port <= 65535:
            raise ValueError
        if recorded_process(pid, port):
            if os.name == "nt":
                subprocess.run(["taskkill", "/T", "/F", "/PID", str(pid)],
                               capture_output=True, check=True)
            else:
                os.killpg(pid, signal.SIGTERM)
        deadline = time.monotonic() + 15
        while not free(port):
            if time.monotonic() >= deadline:
                print("The app port is still busy; look at server.log and ask the instructor.")
                return 1
            time.sleep(0.1)
        if STATE.read_text(encoding="utf-8") != state_text:
            raise ValueError
        STATE.unlink()
        print("The app is stopped.")
        return 0
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError):
        print("The recorded app could not be stopped safely; look at server.log and ask the instructor.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
