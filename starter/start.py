# Ready-made for Phase 1. Do not change it.
# Start the app in the background, or show the address if it is already running.
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request


ROOT = Path(__file__).resolve().parent
STATE = ROOT / ".server.json"
BRAND = "Central Bank Game"  # The navbar brand in templates/base.html.
HTTP = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def alive(pid):
    if type(pid) is not int or pid <= 1:
        return False
    if os.name == "nt":
        import ctypes
        from ctypes import wintypes

        kernel = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel.OpenProcess.restype = wintypes.HANDLE
        kernel.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
        kernel.GetExitCodeProcess.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
        kernel.CloseHandle.argtypes = [wintypes.HANDLE]
        handle = kernel.OpenProcess(0x1000, False, pid)
        if not handle:
            return False
        try:
            code = wintypes.DWORD()
            return bool(kernel.GetExitCodeProcess(handle, ctypes.byref(code))) and code.value == 259
        finally:
            kernel.CloseHandle(handle)
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True


def our_page(port):
    if type(port) is not int or not 1 <= port <= 65535:
        return False
    try:
        with HTTP.open(f"http://127.0.0.1:{port}/", timeout=0.4) as response:
            return response.status == 200 and BRAND in response.read().decode("utf-8", errors="replace")
    except (OSError, urllib.error.URLError):
        return False


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


def running(port):
    print(f"The app is running at http://127.0.0.1:{port}")
    return 0


def main():
    try:
        first = int(sys.argv[1]) if len(sys.argv) == 2 else 8001
        if len(sys.argv) > 2 or not 1 <= first <= 65533:
            raise ValueError
    except ValueError:
        print("Choose a starting port between 1 and 65533 and look at server.log if needed.")
        return 1

    try:
        state = json.loads(STATE.read_text(encoding="utf-8"))
        if isinstance(state, dict) and alive(state.get("pid")) and our_page(state.get("port")):
            return running(state["port"])
    except (OSError, ValueError):
        pass

    ports = range(first, first + 3)
    for port in ports:
        if our_page(port):
            return running(port)
    port = next((p for p in ports if free(p)), None)
    if port is None:
        print("No app port is free; look at server.log and ask the instructor.")
        return 1

    command = ["uv", "run", "uvicorn", "app:app", "--host", "127.0.0.1", "--port", str(port), "--reload"]
    options = {"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS} if os.name == "nt" else {"start_new_session": True}
    try:
        with (ROOT / "server.log").open("ab") as log:
            process = subprocess.Popen(command, cwd=ROOT, stdin=subprocess.DEVNULL,
                                       stdout=log, stderr=log, **options)
        STATE.write_text(json.dumps({"pid": process.pid, "port": port}) + "\n", encoding="utf-8")
        deadline = time.monotonic() + 15
        while time.monotonic() < deadline:
            if our_page(port):
                return running(port)
            if process.poll() is not None:
                break
            time.sleep(0.1)
    except OSError:
        pass
    print("The app did not start in time; look at server.log and ask the instructor.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
