# Validation — Central Bank Game

How we know it is done. [tasks.md](tasks.md) says when each check runs.

## Acceptance criteria

| # | Criterion |
|---|---|
| V1 | Briefing returns 200; states inflation 4.29%, core 3.10%, target 2%, policy rate 2.00%, unemployment 4.22%, population 10,000,000 and 25,800 departures |
| V2 | Economy returns 200; all ten inherited quarters and price/people panels match the model |
| V3 | A finite policy rate from 0 to 20 adds one quarter and redirects with 303, regardless of move size |
| V4 | Rejection changes no history or random state; full economy context renders the exact error |
| V5 | Two 2.50 decisions give inflation 3.57 / 3.51 and core 3.48 / 3.57 |
| V6 | A move to 12 shows the 10.00-point warning, followed by stress 4.75 next quarter |
| V7 | Hold 2.00 scores 1.492; four 0.50 rises then hold scores 2.330; slam to 12 then 3.00 scores 8.215 |
| V8 | Taylor scores 1.048 with inflation 1.78, worst unemployment 4.91 and population 10,177,000; player state stays untouched |
| V9 | Chart has player/Taylor inflation, player core and target; scoreboard retains faces, knot, medals and people/move costs; played policy choices align and cost diagnosis matches the score gap without future choices |
| V10 | Rule lab at GET /rules clamps A/B to 0–5 and preserves defaults; Economy has only its game and the Rule lab link; all contexts render and rule experiments preserve game/history/random state/scores |
| V11 | Reset restores all inherited fields and seed; no twenty-first decision is accepted |
| V12 | At 390 px, cards, forms, scores and population are readable without horizontal page scroll |

## The tests

| After phase | Total | Added |
|---|---|---|
| 1 | 3 | briefing and all starting figures |
| 2 | 7 | context contract, inherited inflation, complete seed |
| 3 | 13 | decisions, bounds, lag, stress and reset |
| 4 | 18 | four strategies, chart/scoreboard contract and term end |
| 5 | 21 | defaults, A/B context and state preservation |

`uv run pytest -q` is the check. Copy in only the phase test requested, from
`later-tests/` to `tests/`. Do not run tests from a future phase.

## What the tests do not check

Native browser layout, colour, chart drawing, touch targets or keyboard use.
Play the two 2.50 decisions, the large-move warning and a reset on screen, then
try the A/B form without losing the played game. Check the narrow layout separately.

## A rule

Never change a test to make a number agree. Recompute from [data-model.md](data-model.md)
and report a contradiction rather than guessing.
