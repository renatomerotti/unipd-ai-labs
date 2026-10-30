# Architecture

How the pieces fit. What each one must do is
[`../specs/central-bank-game/spec.md`](../specs/central-bank-game/spec.md).

## What there is

```text
app.py               routes — what happens when a browser asks for something
models.py            the economy — the data and the arithmetic
templates/           shared base; home, economy and rules pages; ready-made displays
tests/               the checks, one file per phase
```

Two Python files, a shared base and three authored pages, a scoreboard and a chart, and the tests that check them. That
is the whole application. There is no database, no framework beyond FastAPI,
and no build step.

## What happens when you set a policy rate

```text
browser                app.py                    models.py
   │                     │                          │
   │  POST /decide       │                          │
   ├────────────────────▶│                          │
   │                     │  is 0 ≤ rate ≤ 20?       │
   │                     │  no ──▶ re-render with an error
   │                     │                          │
   │                     │  advance(rate)           │
   │                     ├─────────────────────────▶│
   │                     │            appends one quarter to history
   │                     │◀─────────────────────────┤
   │  303 → /economy     │                          │
   │◀────────────────────┤                          │
   │  GET /economy       │                          │
   ├────────────────────▶│  reads history, scores it, runs the rule
   │  the page           │                          │
   │◀────────────────────┤                          │
```

The redirect matters: without it, refreshing the page would submit the same rate
again.

## Where the state lives

`history` is a module-level list in `models.py`. That is the single source of
truth, and it disappears when the application stops.

`INITIAL` holds the ten inherited quarters so the benchmark can replay from the
same starting point, and so the tests can reset between runs.

## Why the benchmark runs separately

The Taylor rule plays its own game on a copy of the history, with its own random
generator seeded identically. It never touches `history`. If it did, comparing
the two would be comparing a run against itself.

## Game and Rule lab have separate jobs

`GET /economy` shows the player's game and its complete Phase 4 context,
including past-policy choices and the score-gap diagnosis.
`GET /rules` renders `rules.html` with the six A/B experiment values.
It simulates twenty quarters independently, without changing the player's game,
scores or generator. Economy links to Rule lab; its scoreboard never reacts to
an experimental rule run.

## What was deliberately left out

See [adr/](adr/) — no database, no persistence, and a scoring function that
prices unemployment rather than measuring inflation alone.
