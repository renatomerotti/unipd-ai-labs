# The model

The Central Bank Game combines prices, employment, financial stress and people
moving. Implement these equations exactly, including the order of rounding.
The target, the Taylor rule, migration and the score all use **inflation**.

---

## Constants

| Name | Value | Meaning |
|---|---|---|
| `TARGET` | 2.0 | inflation target (%) |
| `NEUTRAL_RATE` | 2.0 | neutral policy rate (%) |
| `NATURAL_UNEMP` | 4.5 | normal unemployment (%) |
| `SEED` | 42 | fixed random seed |
| `LAMBDA` | 0.5 | unemployment weight in the score |
| `NU` | 0.25 | policy-rate move weight in the score |
| `TERM` | 20 | quarters in a player's term |
| `STRESS_FREE` | 0.5 | policy-rate move causing no financial stress |
| `STRESS_K` | 0.5 | output gap lost per point above that move |
| `POPULATION_START` | 10,029,600 | people before the inherited history |
| `MIGRATION_PER_POINT` | 20,000 | people moving per point of misery |
| `MISERY_NEUTRAL` | 1.0 | misery at which nobody moves |

Inflation weights, in this order: core 0.70, food 0.20, fuel 0.04, energy 0.06.
Food, fuel and energy persistence: 0.6, 0.4 and 0.6.
Shock ranges: demand ±0.3, food ±1.0, fuel ±4.0, energy ±2.0.
One `random.Random(SEED)` supplies **four draws per quarter in that order**.

## Inflation

```text
headline(quarter) = round(0.70 * core + 0.20 * food + 0.04 * fuel + 0.06 * energy, 2)
```

Use a function, never a stored `inflation` or `headline` field. Core inflation excludes
food, fuel and energy. Energy means electricity and gas; fuel is separate.
The weighted sum is evaluated in the order core, food, fuel, energy.
Python's built-in `round()` is used throughout, including its handling of ties.

## Advancing one quarter

Let `previous` and `before` be the last two quarters already in the history.
Draw all four shocks first. Then compute, in this exact order:

```text
move           = abs(previous.rate - before.rate)
stress         = round(0.5 * max(0, move - 0.50), 2)
gap            = round(-0.5 * (previous.rate - 2.0) + demand_shock - stress, 2)
energy_push    = 0.4 * (previous.fuel - 2.0) + 0.6 * (previous.energy - 2.0)
core           = round(previous.core + 0.3 * gap + 0.05 * energy_push, 2)
food           = round(2.0 + 0.6 * (previous.food - 2.0) + food_shock, 2)
fuel           = round(2.0 + 0.4 * (previous.fuel - 2.0) + fuel_shock, 2)
energy         = round(2.0 + 0.6 * (previous.energy - 2.0) + energy_shock, 2)
unemployment   = round(4.5 - 0.4 * gap, 2)
misery         = abs(headline(new_quarter) - 2.0) + max(0, unemployment - 4.5)
migration      = int(round(-20000 * (misery - 1.0), -2))
population     = previous.population + migration
```

The new quarter stores the submitted policy rate, rounded economic values,
migration in whole people (multiples of 100), and population in whole people.
Keep the submitted policy rate as entered; do not force it onto a 0.25 grid.
Core inflation and unemployment use the **already rounded** gap. Migration uses the
**already rounded** inflation. Append one new `Quarter`, leaving earlier ones alone.

### Read that once more

The new quarter answers to `previous.rate`, never the newly submitted rate.
Financial stress also answers to the move already made, between `before` and
`previous`. A large decision has its score cost immediately and its economic
stress next quarter. The input accepts any finite policy rate from 0 to 20.

The warning is stateless: show it when `abs(history[-1].rate - history[-2].rate)
> 0.50`, with that absolute difference as X, to two decimals:
*💥 You moved X points in one quarter. Markets will feel it next quarter.*
Show a red financial-stress badge only when the latest quarter's stress is positive.

## Worked example

Set the policy rate to 2.50 twice from the inherited economy, with seed 42:

| Quarter | Policy rate | Inflation | Core inflation | Gap | Unemployment | Stress | People moving | Population |
|---|---|---|---|---|---|---|---|---|
| 2026-Q1 | 2.50 | 3.57 | 3.48 | 0.08 | 4.47 | 0.00 | −11,400 | 9,988,600 |
| 2026-Q2 | 2.50 | 3.51 | 3.57 | −0.11 | 4.54 | 0.00 | −11,000 | 9,977,600 |

Inflation falls as fuel and energy fade, while core rises. The first new quarter
still answers to the inherited 2.00% policy rate. Setting 12.00 once gives that
same first gap, but the next quarter carries stress **4.75** from the 10.00-point
move: `0.5 * (10.00 - 0.50)`.

## The benchmark rule (Phase 4)

```text
formula = 2.0 + 1.5 * (headline(quarter) - 2.0) + 0.5 * quarter.gap
move    = max(-0.50, min(0.50, round((formula - quarter.rate) * 4) / 4))
policy_rate = max(0.0, min(20.0, round(quarter.rate + move, 2)))
```

Move toward the formula in 0.25-point steps, never more than 0.50 per quarter.
Do not jump directly to the formula's policy rate.
`rule_run(n_quarters)` starts with `list(INITIAL)` and a fresh
`random.Random(SEED)`. Advance its own list with the same four shocks, rounding,
stress and migration as the player; leave the player's history and generator alone.
In Phase 5, add optional `a=1.5`, `b=0.5` coefficients in place of 1.5 and 0.5.
The move limit and 0.25 rounding stay unchanged.

## The score

```text
move_i = quarter_i.rate - quarter_(i-1).rate    # 0 for the first row
loss = round(mean((headline - 2.0)^2 + 0.5 * (unemployment - 4.5)^2
                  + 0.25 * move_i^2), 3)
```

Average over **every row, inherited included**. The inherited policy rate is
constant, so all inherited moves cost zero. Migration and population are shown,
not scored. Lower is better. Display scores to three decimals; economic values
to two decimals, people as integers with thousands separators.

Medals retain the existing rule: gold when the player's score is at most the
Taylor score, silver within 10%, bronze otherwise. Equal scores are shown as tied.
The tug-of-war knot stays at 50% for a tie and reaches an end at a 20% score gap.

| Twenty-quarter strategy | Score | Final inflation | Worst unemployment in played quarters | Population |
|---|---|---|---|---|
| Taylor rule | 1.048 | 1.78 | 4.91 | 10,177,000 |
| Hold 2.00 | 1.492 | 2.72 | 4.61 | 9,978,400 |
| 2.50, 3.00, 3.50, 4.00, then hold 4.00 | 2.330 | -0.95 | 5.00 | 9,769,400 |
| 12.00, then 3.00 nineteen times | 8.215 | -2.11 | 8.34 | 9,114,200 |

## The inherited history

Every row stores all eleven fields, in this order: label, rate, core, food,
fuel, energy, gap, unemployment, stress, migration, population.
These are literal values; load no data file at runtime.

| Quarter | Policy rate | Core inflation | Food | Fuel | Energy | Gap | Unemployment | Stress | Migration | Population |
|---|---|---|---|---|---|---|---|---|---|---|
| 2023-Q3 | 2.00 | 2.00 | 2.00 | 2.00 | 2.00 | 0.00 | 4.50 | 0.00 | 20,000 | 10,049,600 |
| 2023-Q4 | 2.00 | 2.00 | 2.20 | 1.50 | 2.10 | 0.10 | 4.46 | 0.00 | 19,400 | 10,069,000 |
| 2024-Q1 | 2.00 | 2.10 | 2.40 | 3.00 | 2.50 | 0.20 | 4.42 | 0.00 | 15,600 | 10,084,600 |
| 2024-Q2 | 2.00 | 2.20 | 2.60 | 4.00 | 3.00 | 0.30 | 4.38 | 0.00 | 12,000 | 10,096,600 |
| 2024-Q3 | 2.00 | 2.30 | 3.00 | 6.00 | 4.00 | 0.40 | 4.34 | 0.00 | 6,200 | 10,102,800 |
| 2024-Q4 | 2.00 | 2.40 | 4.00 | 10.00 | 7.00 | 0.50 | 4.30 | 0.00 | -6,000 | 10,096,800 |
| 2025-Q1 | 2.00 | 2.50 | 5.00 | 14.00 | 10.00 | 0.50 | 4.30 | 0.00 | -18,200 | 10,078,600 |
| 2025-Q2 | 2.00 | 2.70 | 6.00 | 12.00 | 12.00 | 0.60 | 4.26 | 0.00 | -25,800 | 10,052,800 |
| 2025-Q3 | 2.00 | 2.90 | 6.50 | 9.00 | 11.00 | 0.60 | 4.26 | 0.00 | -27,000 | 10,025,800 |
| 2025-Q4 | 2.00 | 3.10 | 6.00 | 8.00 | 10.00 | 0.70 | 4.22 | 0.00 | -25,800 | 10,000,000 |

Inflation along these ten rows is 2.00, 2.03, 2.22, 2.40, 2.69, 3.30, 3.91, 4.29, 4.35, 4.29.
Population starts at 10,029,600 **before** the first row; during the player's
term, population change is measured from 10,000,000.
