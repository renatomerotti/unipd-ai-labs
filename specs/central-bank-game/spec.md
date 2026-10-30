# Specification — Central Bank Game

What the finished application must do. Build in [tasks.md](tasks.md) order;
[data-model.md](data-model.md) overrides this file if they disagree.

## Routes

| Method | Path | Does |
|---|---|---|
| GET | `/` | Briefing about the food and energy surge |
| GET | `/economy` | The player’s game: prices, people, record, form, scoreboard and chart as built |
| GET | `/rules` | Phase 5 Rule lab: a separate twenty-quarter A/B experiment |
| POST | `/decide` | Validate a policy rate, advance one quarter, redirect with 303 |
| POST | `/reset` | Restore inherited history and seed 42, redirect with 303 |

## GET /

State the 2% inflation target, current inflation 4.29%, core 3.10%, policy rate
held at 2.00% for ten quarters, unemployment 4.22%, population 👥 10,000,000,
and 🧳 25,800 people leaving last quarter. Explain the food and energy surge and
the policy lag. Name the Central Bank Game and link to `/economy`.

## GET /economy

| Part | Contents |
|---|---|
| Record | Quarter, Policy rate %, 📊 Inflation %, 🧺 Core inflation %, 🍞 Food %, ⛽ Fuel %, 💡 Energy %, 👷 Unemployment %, Output gap %; oldest first |
| Summary | Ready-made `_summary.html`: policy rate, inflation, unemployment and output gap with last-quarter arrows |
| Prices | Ready-made `_prices.html`: inflation plus food, fuel, energy and core cards, weights and arrows |
| People | Ready-made `_people.html`: population, arrivals/departures this quarter, change during player's term |
| Legend | Ready-made `_legend.html`, after the record, explaining each column and card |
| Emphasis | `table-warning` when rounded inflation is more than 0.50 away from 2% |
| Form | Any policy rate 0–20 accepted; recommend 0.25 or 0.50 moves; require a number |
| Warning | Latest move above 0.50: stateless 💥 warning with two-decimal move size |
| Stress | Red 💥 badge only when current financial stress is positive |
| Scores | `_scoreboard.html` above the chart; faces, population per side, score breakdown including moves, knot, verdict, medal |
| Chart | `_chart.html`: player inflation, Taylor inflation, dashed player core, target |
| Policy comparison | Ready-made `_policy_comparison.html` after the chart: played quarters only, your and Taylor’s policy rates aligned by quarter; no future choices |
| Score diagnosis | Above the form, identify who is behind, the largest average cost disadvantage and any offsetting cost saving; costs only, no suggested policy |

Use the shared Bootstrap 5.3.3 layout. Food is amber, fuel red, energy yellow,
core slate; unemployment blue, population neutral, arrivals green, departures red.
Inflation faces: 🥵 above 3.5, 😐 above 2.5 through 3.5, 😀 1.5 through 2.5,
🥶 below 1.5. Keep the existing score knot and tie behavior.
Economic values have two decimals, scores three, and people thousands separators.
At 390 px wide, content must be readable without horizontal page scrolling.

Final Economy order: heading → scoreboard → policy-rate form and Start again → chart → policy comparison → summary → prices → people → table → legend → Rule lab link. Earlier phases omit parts not built yet.
Heading: `The economy you inherited · 2025-Q4` for ten inherited rows, then `Your economy · <quarter>`. Prefix stressed record quarters with `💥`.

## POST /decide

Accept a finite number named `rate` with `0 ≤ rate ≤ 20`. No restriction on
move size or 0.25-step alignment; the form uses `step="any"`.
Reject an out-of-range or non-finite value with the exact message
`The policy rate must be between 0% and 20%.`, adding no quarter or random draws.
The error response has status 200 and the complete economy context for that phase.
An empty or non-numeric form input is refused by browser validation (and FastAPI
validation if submitted directly).

A valid submission adds exactly one quarter and redirects to `/economy` with
303. From Phase 4, refuse any decision after twenty played quarters, with
`Your term is over. Press Start again from the inherited economy to serve another term.`
Show that error without changing history and hide the policy-rate form after the term.
The reset form stays visible.

## POST /reset

Restore `history[:] = list(INITIAL)` and reseed the existing generator with
`rng.seed(SEED)`. The next decision must reproduce the first game's quarter.

## GET /rules — Rule lab (Phase 5)

Author `templates/rules.html`, extending `base.html` and including the ready-made
`_my_rule.html`. Read optional `a` and `b` query numbers, default 1.5 and 0.5,
clamped to 0–5. Pass exactly the six experiment values: `a`, `b`, `taylor_term`,
`taylor_term_score`, `my_term`, `my_term_score`. The page has the experiment,
not the game scoreboard; the form and reset link target `/rules#my-rule`.

Economy retains every Phase 4 context variable on normal and error paths.
Replace its experiment include with the linked line
“🧪 Ready for the board's question? Open the Rule lab.”, linking to `/rules`.
Menu order: Home · Economy · Rule lab. Earlier phases use the not-built handler
for `/rules`. Comparing rules changes no player history, generator state, scores
or term record. Both rules keep the 0.50 move limit. Scores and worst
unemployment compare the same twenty quarters.

## What must never happen

- A new quarter or random draw on a rejected policy rate.
- Inflation stored or recomputed with different rounding in different places.
- Stress taken from the newly submitted move rather than the previous one.
- Core inflation or unemployment computed from an unrounded gap.
- The benchmark using another shock order or modifying player state.
- A shared template or test edited to make a failing build pass.
