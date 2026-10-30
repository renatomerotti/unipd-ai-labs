# Rebuild from scratch

**Use this only if your project is broken beyond repair** and you would rather
start again than fix it.

Starting over costs requests. Before you do, consider copying the relevant
folder from `checkpoints/` instead — that costs none.

---

## Before you start

Decide which phase you want to reach. Rebuilding to Phase 3 costs roughly as
many requests as building Phases 1 to 3 did the first time.

If your daily allowance is nearly gone, ask for a checkpoint instead.

---

## First, clear the wreckage

Stop the app with `uv run stop.py` before removing the broken files.

Delete these from your `unipd-ai-lab` folder, if they exist:

```text
app.py
models.py
templates/
tests/
```

Keep `specs/`, `docs/`, `later-tests/`, `pyproject.toml`, `README.md`,
`start.py`, `stop.py`, `opencode.json` and `.gitignore`.

Then ask the instructor for a fresh copy of `templates/` and
`tests/test_phase_1.py`. Keep `later-tests/` where it is; the prompt below copies
only the tests up to the phase you choose.

---

## The prompt

Start a new session first — close the **opencode** tab and open it again — so
the assistant has never seen your earlier conversation. Then replace `N` with
the phase number you want to reach.

```text
Read docs/mission.md, docs/tech-stack.md, specs/central-bank-game/tasks.md and
specs/central-bank-game/data-model.md.

The project contains those files and the ready-made templates, tests,
start.py and stop.py. Do these in order:
1. Copy from later-tests/ only test_phase_2.py up to test_phase_N.py into
   tests/; never copy or run any other file from later-tests/.
2. Implement Phase 1 through Phase N from specs/central-bank-game/tasks.md,
   exactly as written, and nothing beyond them. Do not change any ready-made file.

Work one phase at a time. After each phase, run only the tests of the phases
built so far — after Phase 2, for example:
  uv run pytest -q tests/test_phase_1.py tests/test_phase_2.py
and fix anything that fails before starting the next phase. When the last phase
is done, finish in this order:
1. Run uv run pytest -q; fix any failures and run it again until all tests pass.
2. Run uv run start.py once.
3. Stop. Reply with the test line and the line start.py printed. Run nothing
   else, and create no other file.

While building, do not start the application. Never run pkill or kill.

Two things that are easy to get wrong and must be right:
- in advance_quarter(), the gap and stress use preceding recorded policy rates,
  not the newly submitted policy rate; round the gap before core and unemployment
- rule_rate uses headline, rounds moves to 0.25 and limits them to 0.50;
  rule_run uses a fresh random.Random(SEED) with demand, food, fuel, energy draws
```

---

## Check

In the **opencode** tab, the assistant's last test run says:

| Rebuilt to | Expect |
|---|---|
| Phase 1 | `3 passed` |
| Phase 2 | `7 passed` |
| Phase 3 | `13 passed` |
| Phase 4 | `18 passed` |
| Phase 5 | `21 passed` |

---

Open the address the assistant gives you, the one `start.py` printed.
For later lab steps, this is the address from Row 15.

---

## Why this worked

You rebuilt a whole project from files, with an assistant that had never seen
your earlier conversation.

That is the argument for writing things down, and you have just run the
experiment yourself.
