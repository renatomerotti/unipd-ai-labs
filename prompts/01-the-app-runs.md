# Step 1 — Phase 1: the application runs

**You will finish with:** a page that loads in your browser.

---

## Before you start

Your `unipd-ai-lab` folder contains the files that came with the download, and
the assistant has already answered the three questions in `SETUP.md` Step 11.

---

## The prompt

```text
Implement Phase 1 from specs/central-bank-game/tasks.md exactly as written, and nothing beyond it.

Create these files:
  app.py
  templates/home.html

templates/base.html, templates/not_built.html and tests/test_phase_1.py
already exist. Do not change them.

Never run pkill or kill.

Follow the instructions literally. In particular:
1. Do not add a script header to app.py; dependencies come from pyproject.toml.
2. Use the exact route and template names tasks.md specifies.
3. Show the food and energy surge, inflation 4.29%, core inflation 3.10%, policy rate
   2.00%, unemployment 4.22%, population 10,000,000 and 25,800 people leaving.
4. Add only what Phase 1 asks for.

Finish in this order:
1. Run uv run pytest -q; fix any failures and run it again until all tests pass.
2. Run uv run start.py once.
3. Stop. Reply with the test line and the line start.py printed. Run nothing
   else, and create no other file.
```

---

## What should happen

Two files appear. The assistant runs the tests. You see `3 passed`.

The first run downloads Python and some libraries, so it is slower. That
is normal and happens only once.

---

## Check before continuing

In the assistant's tab, find the line it ran — `$ uv run pytest -q` — and read
what is printed under it: `3 passed`. Read that line, not the assistant's
summary of it.

The assistant gives you the address printed by `start.py`. Open that address
in your browser. The usual port is 8001; if it is busy, `start.py` tries 8002
and 8003. You should see the briefing
page, saying inflation is 4.29% and the target is 2%. Leave the application
running for the rest of the lab; it reloads each time a file changes.

- [ ] `3 passed`
- [ ] The briefing page loads and mentions 4.29%

Do not open `02-the-economy.md` until both are true.

---

## Start and stop the app yourself

In VS Code's terminal (**Terminal → New Terminal**), use the same commands on
Mac and Windows:

```bash
uv run start.py
uv run stop.py
```

Use the first command to start the app and read its address. Use the second
only when you want to stop it. Leave it running during the lab.

---

## If it fails

First work down [`docs/troubleshooting.md`](../docs/troubleshooting.md) — start with **S1** to **S5**.

If none of those is it, copy the **whole** error and send: `This is the error. Fix it.`
