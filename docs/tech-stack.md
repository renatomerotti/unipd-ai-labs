# Tech stack

Fixed. Do not substitute libraries, add dependencies, or change versions.

| Layer | Choice | Version |
|---|---|---|
| Language | Python | 3.11 or newer |
| Runner | `uv` | latest |
| Web framework | `fastapi[standard]` | 0.115.10 |
| Templates | Jinja2 | bundled with FastAPI |
| Styling (CSS, Cascading Style Sheets) | Bootstrap 5 | from a content delivery network (CDN), no build step |
| Charts | Chart.js | CDN only |
| Data | `dataclasses.dataclass` + a module-level list | — |
| Storage | in memory | none |
| Tests | pytest + `starlette.testclient.TestClient` | 8.3.4, pinned in `pyproject.toml` |

## Dependencies come from `pyproject.toml`

There is no virtual environment to create and no install step to run. The
project's `pyproject.toml` declares what it needs, and `uv` fetches everything —
including Python itself — the first time you run a command.

`pyproject.toml` arrives with the download. **Do not edit it, and do not add
dependencies to it.**

Do **not** put a `# /// script` header at the top of `app.py`. Dependencies are
declared in one place only.

## Commands

```bash
uv run start.py     # start the application and print its address
uv run stop.py      # stop the application started by start.py
uv run pytest -q    # run the tests
```

The first command you run downloads Python and the libraries. It is slower
than the rest, and happens once.

Open the address `start.py` prints. The usual port is 8001; if it is busy,
the backups are 8002 and 8003. The app runs in the background.
For a foreground run instead, `uv run app.py` uses port 8001 and stays in
the terminal until you press Ctrl+C; stop the background app first.

## Project layout

The student builds the Python files. `specs/`, `docs/`, `templates/` and the
first test arrive with the download, as do `start.py` and `stop.py`; the assistant
moves the later tests in from `later-tests/`, one phase at a time. The application
files are built by the assistant.

```text
unipd-ai-lab/
├── app.py               routes, and the uvicorn __main__ block
├── models.py            the Quarter dataclass, the history, advance()
├── start.py             starts the app and prints its address — ready-made
├── stop.py              stops the app started by start.py — ready-made
├── templates/
│   ├── base.html        shared layout — ready-made
│   ├── _legend.html     the Phase 2 table's legend — ready-made
│   ├── _chart.html      the Phase 4 chart — ready-made
│   ├── _scoreboard.html the Phase 4 scoreboard — ready-made
│   ├── home.html        the briefing
│   ├── economy.html     the game: history table, form and comparisons
│   └── rules.html       the separate Phase 5 Rule lab experiment
├── tests/
│   └── test_phase_N.py  one file per phase — ready-made
├── opencode.json        the assistant's rules — ready-made, never change it
└── .gitignore           included in the download
```

**Never change a ready-made file.** The tests are the definition of done.

## Rules

* **No database.** The history is a module-level list in `models.py`.
* **No authentication.** There are no users.
* **No build step.** Bootstrap and Chart.js load from a CDN.
* **No extra dependencies.** If something seems to need one, it does not.
* Start the app with `uv run start.py`, not with `python app.py`.
