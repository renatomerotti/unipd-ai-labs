# The prompts

One file per **lab step**. Work through them **in order**. Do not open a file
until the previous file's check has passed.

**Lab Step _N_ builds Phase _N_.** The two numbers are always the same, so there
is nothing to translate.

| File | Lab step | Builds |
|---|---|---|
| `01-the-app-runs.md` | Step 1 | Phase 1 — the application runs |
| `02-the-economy.md` | Step 2 | Phase 2 — the economy you inherited |
| `03-set-a-policy-rate.md` | Step 3 | Phase 3 — set a policy rate, meet the lag |
| `04-score-and-rule.md` | Step 4 | Phase 4 — chart, score, your opponent |
| `05-beat-the-rule.md` | Step 5 | Phase 5 — a policy rule of your own |
| `../docs/improve.md` | Challenges 1 and 2 | one change, then a bigger question — you write the prompts |
| `99-rebuild-from-scratch.md` | — | starting over, in an emergency |

> **Creating the project folder is not in here.** It is the last *setup* step —
> `SETUP.md` **Step 11** — because it copies files rather than building anything.
> Do that first, then open `01-the-app-runs.md`.

## How each file works

Every one has the same four parts:

1. **Before you start** — something to check. If it fails, you are in the wrong
   file. From Step 2 it also names the ready-made test file to copy in.
2. **The prompt** — in a grey block. Copy the whole thing. Nothing else.
3. **What should happen** — so you know whether it worked.
4. **Check before continuing** — a command and its expected output.

**The check is not optional.** It is how you discover that step two went wrong
before you reach step five.

## If a step fails twice

Do not reword the prompt and try again — that is the same request wearing a hat,
and it costs you another slice of your daily allowance.

Read `specs/central-bank-game/data-model.md` or the relevant part of `specs/central-bank-game/tasks.md`, work out
what was ambiguous, and say what you actually want. Once.
