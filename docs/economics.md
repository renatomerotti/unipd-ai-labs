# The economics of the Central Bank Game

Every economic term this lab uses, in plain language first. Read this from
Phase 2 onward. The exact implementation is in
[the data model](../specs/central-bank-game/data-model.md); tool terms are in
[the glossary](glossary.md).

## What is in here

Reading the economy table · Inflation target · Output gap · Policy lag · Shock ·
Seed · Taylor rule · Taylor principle · Loss function · Rules versus discretion

## Reading the economy table

## 📋 The columns

One row is one quarter: three months, oldest at the top. The first ten rows,
2023-Q3 to 2025-Q4, are inherited.

| Column | What it means |
|---|---|
| Quarter | The year and quarter: Q1 is January to March, Q4 October to December. |
| Policy rate % | The interest rate the central bank sets. It moves the economy in the **next** row. |
| 📊 Inflation % | The weighted price rise across the whole basket. The target is 2%. |
| 🧺 Core inflation % | Price rises outside food, fuel and energy, shown separately from inflation. |
| 🍞 Food % | Groceries inflation, shown in amber. |
| ⛽ Fuel % | Gasoline and diesel inflation, shown in red. |
| 💡 Energy % | Electricity and gas inflation, shown in yellow. |
| 👷 Unemployment % | The share of people wanting work who have no job. Normal here is 4.50%. |
| Output gap % | How far the economy runs above (+) or below (−) its normal capacity. Above it heats prices; below it costs jobs. |

## 🟨 The yellow rows

A yellow row has inflation more than 0.50 percentage points away from 2%, above
or below. The last six of the ten inherited rows qualify; the first four are near target.

## 🔎 Read one row

| Quarter | Policy rate % | 📊 Inflation % | 🧺 Core inflation % | 🍞 Food % | ⛽ Fuel % | 💡 Energy % | 👷 Unemployment % | Output gap % |
|---|---|---|---|---|---|---|---|---|
| 2025-Q4 | 2.00 | 4.29 | 3.10 | 6.00 | 8.00 | 10.00 | 4.22 | 0.70 |

The policy rate was neutral, but a food and energy surge raised inflation.
Unemployment follows the gap: **4.50 − 0.4 × 0.70 = 4.22**.

The panels above the table open up that inflation number:

| Reading | What it means | 2025-Q4 |
|---|---|---|
| 📊 Inflation | 70% core + 20% food + 4% fuel + 6% energy | 4.29% |
| 🧺 Core inflation | Price rises outside food, fuel and energy; shown in slate | 3.10% |
| 🍞 Food | Food inflation, in amber | 6.00% |
| ⛽ Fuel | Fuel inflation, in red | 8.00% |
| 💡 Energy | Electricity and gas inflation, in yellow | 10.00% |

**0.70 × 3.10 + 0.20 × 6.00 + 0.04 × 8.00 + 0.06 × 10.00
= 2.17 + 1.20 + 0.32 + 0.60 = 4.29.** Arrows compare with the preceding
quarter. Food, fuel and energy fade toward 2% with shocks; core is more persistent
and also absorbs pressure from the previous quarter's fuel and energy.

The people panel and legend complete the picture:

- 👷 **Unemployment** is in the table and, from Phase 4, in blue on the scoreboard.
- 💥 **Financial stress** beside a quarter means a sharp earlier policy-rate
  move has caused an extra hit to activity and jobs in that quarter. A move
  above 0.50 points in either direction reduces next quarter's gap by half the
  excess. The red badge is that extra gap penalty; the icon stays in the record.
  Inherited stress is **0.00**. For the observed 3.00→2.00 decision, the move
  is 1.00 point: **(1.00 − 0.50) × 0.50 = 0.25** points of extra gap penalty
  in the following quarter, even if that quarter records a hold at 2.00.
  Holding other inputs fixed, gap **-0.05** rather than **+0.20** gives
  unemployment **4.52%** rather than **4.42%**. This is the game's teaching
  mechanism, not a universal estimate for real economies.
- ✈️ means arrivals; 🧳 means departures. **25,800 left** in 2025-Q4.
- 👥 **Population** includes those movements: **10,000,000**. At the start of
  your term, “Since you took over” is **+0**; inherited departures happened before you.

Migration uses a simple hardship measure: the absolute inflation miss from 2%,
plus unemployment above 4.50% (never subtract below-normal unemployment).
Above a hardship of 1, people leave; below it, people arrive. Each point moves
20,000 people, rounded to the nearest hundred. Here hardship is **2.29**, so
**−20,000 × (2.29 − 1) = −25,800**. Population is shown, **not scored**.

> 💡 **Why the policy rate does not match the row it sits on:** Row 26 explains the delay.

## Inflation target

The target for inflation is 2%. Core inflation excludes food, fuel and energy;
inflation combines all four parts using fixed basket weights. A falling
inflation can coexist with rising core, so watch both.

## Output gap

Output relative to its sustainable level. Positive means overheating; negative
means slack. The gap responds to the preceding policy rate and a demand shock,
with financial stress subtracted:

```text
gap = round(-0.5 × (previous policy rate − 2) + demand shock − stress, 2)
stress = round(0.5 × max(0, abs(previous move) − 0.50), 2)
core = round(previous core + 0.3 × gap + 0.05 × energy pressure, 2)
energy pressure = 0.4 × (previous fuel − 2) + 0.6 × (previous energy − 2)
unemployment = round(4.5 − 0.4 × gap, 2)
```

A one-point higher preceding policy rate lowers the gap by half a point,
before rounding and holding shocks and stress fixed. Core inflation carries its previous
level forward, changes with demand and absorbs earlier fuel and energy
pressure. Food, fuel and energy each pull toward 2%, with persistence 0.6,
0.4 and 0.6 respectively. These are teaching parameters, not empirical estimates.

## Policy lag

## ⏳ What happens when you click

1. The app adds one new quarter.
2. That quarter's output gap uses the **previous** quarter's policy rate.
3. Your choice is stored on the new quarter and acts in the quarter after it.
4. If that choice moved more than 0.50 points, financial stress also reduces
   the following quarter's gap.

## 🔎 Row 17, quarter by quarter

| Quarter | Policy rate % | Inflation % | Core inflation % | Unemployment % | Gap moved by |
|---|---|---|---|---|---|
| 2025-Q4 | 2.00 | 4.29 | 3.10 | 4.22 | the inherited economy |
| 2026-Q1 | 2.50 | 3.57 | 3.48 | 4.47 | the old 2.00 policy rate |
| 2026-Q2 | 2.50 | 3.51 | 3.57 | 4.54 | your first 2.50 decision |

- **Why 2.50:** a 0.50-point step above the neutral 2%, without financial stress.
- **Why inflation falls first:** food, fuel and energy fade; that is not evidence
  that your new policy rate has worked. Core inflation rises from **3.10 to 3.48**.
- **Why 2.50 again:** holding the decision shows its delayed effect. The gap
  becomes **−0.11**, but energy pressure still takes core to **3.57**.

## 🧊 Two things that follow

- **Inflation can fall without a squeeze.** Hold the neutral policy rate of 2%
  for twenty quarters: inflation ends at **2.72%**, still above target. The fading
  surge and the policy channel are different effects.
- **A large move has two delayed costs.** Set 12 then 3: the second played
  quarter has financial stress **4.75**, gap **−9.61** and unemployment **8.34%**.
  Its inflation is **1.52%**. The stress comes from the preceding **10-point**
  move, not the new choice of 3. Holding 5 for twenty quarters ends with inflation
  **-3.52%**. Read the delayed effects before tightening again.

## 🌍 Real central banks

Policy acts with delays, and decisions also affect financial conditions. The
Federal Reserve explicitly considers accumulated tightening and its lags when
choosing the pace of further moves. The game's one-quarter lag and stress
formula are teaching choices, not estimates of that real transmission.
([Federal Reserve, November 2022](https://www.federalreserve.gov/newsevents/pressreleases/monetary20221102a.htm))

## Shock

A disturbance outside the central bank's control. Each quarter draws demand,
food, fuel and energy shocks, in that order, from uniform ranges of ±0.3,
±1.0, ±4.0 and ±2.0. Doubling all four shocks is the Hard experiment in
[Challenge 1](improve.md). Bigger shocks need not raise inflation in every quarter.

## Seed

The starting number for the random sequence. Seed 42 gives every comparison
the same shocks. A fresh replay keeps an opponent's simulation separate from
the player's game. Another seed tests whether a result depends on that sequence.

## Taylor rule, Taylor principle

## 🌡️ The idea: a thermostat with two readings

A thermostat turns the heating down when a room is too warm. The rule reads
inflation and the output gap: prices above target or output above its
sustainable level point toward a higher **policy rate**, the interest rate the
central bank sets. A negative gap pulls the recommendation down.

## 📐 The formula

**formula's policy rate = 2 + 1.5 × (inflation − 2) + 0.5 × output gap**

| Part | What it does | Inherited 2025-Q4 |
|---|---|---|
| 2 | The neutral policy rate | 2.000 |
| 1.5 × (inflation − 2) | Responds to the miss from the 2% inflation target | 1.5 × 2.29 = +3.435 |
| 0.5 × gap | Adds for overheating, subtracts for slack | 0.5 × 0.70 = +0.350 |

The formula gives **5.785%**, but the rule does **not** jump there. Round the
difference from the current policy rate to the nearest 0.25, limit the move to
**−0.50 through +0.50**, then keep the new policy rate between 0 and 20.
This is **interest-rate smoothing**: move gradually toward the recommendation.
The first actual decision is **2.50%**, up from 2.00%.

## 🔎 Watch it decide: its first four quarters

Each decision reads the last available row of the rule's own history.

| It decides for | It sees: inflation, gap | Formula's policy rate | Previous → actual policy rate |
|---|---|---|---|
| 2026-Q1 | 4.29, +0.70 | 2 + 3.435 + 0.350 = 5.785 | 2.00 → **2.50%** |
| 2026-Q2 | 3.57, +0.08 | 2 + 2.355 + 0.040 = 4.395 | 2.50 → **3.00%** |
| 2026-Q3 | 3.51, -0.11 | 2 + 2.265 − 0.055 = 4.210 | 3.00 → **3.50%** |
| 2026-Q4 | 2.99, -0.55 | 2 + 1.485 − 0.275 = 3.210 | 3.50 → **3.25%** |

Read it top to bottom:

1. **First decision:** the formula wants 5.785, but the 0.50 step gives 2.50.
2. **Second:** inflation falls to 3.57, yet the formula's 4.395 is still above
   the current 2.50. Another 0.50 step gives 3.00.
3. **Third:** the formula's 4.210 is above 3.00, so the next step gives 3.50.
4. **Fourth:** the formula falls to 3.210. The difference from 3.50 rounds to
   −0.25, so the decision is 3.25, while inflation is still 2.99%.

After twenty played quarters: inflation **1.78%**, worst unemployment **4.91%**,
score **1.048**. These are the benchmark figures for Rows 18 and 19.

## 🎛️ What its two numbers do

In Row 19’s **Rule lab** page, **A** replaces 1.5 and **B** replaces 0.5. Keep the same smoothing
for every experiment, and reset the other number to its default:

| Rule | Score | Worst unemployment | Final inflation | What it shows |
|---|---|---|---|---|
| Taylor: A = 1.5, B = 0.5 | 1.048 | 4.91% | 1.78% | The benchmark |
| A = 0.5, B = 0.5 | 1.157 | 4.76% | 2.14% | Gentler peak, higher score |
| A = 3.0, B = 0.5 | 1.063 | 4.97% | 1.77% | Higher score and harsher peak |
| A = 1.5, B = 0.0 | 1.029 | 4.91% | 1.81% | Lower score, equal worst unemployment |

## ⚖️ Why 1.5 and not 1

The **Taylor principle** says the policy rate should eventually rise by more
than the rise in inflation. Otherwise inflation-adjusted borrowing costs do
not rise. The formula supplies that stronger response; smoothing delays its
arrival. It does not require an immediate jump to the formula's level.

This game's gap responds to the nominal policy rate relative to 2%, not to a
real-interest-rate channel. It illustrates consequences of different rules,
not a full test of the Taylor principle. A = 0.5 leaves inflation at **2.14%**
after twenty quarters; Taylor's A = 1.5 leaves it at **1.78%**.

## 👤 Where it comes from

John Taylor proposed the rule in 1993. The United States Federal Reserve
compares several rules, including versions that depend on the preceding
policy rate. Taylor's original combines a neutral real interest rate with
inflation; this game's simplified neutral nominal policy rate is fixed at 2%.
([Federal Reserve: policy rules](https://www.federalreserve.gov/monetarypolicy/policy-rules-and-how-policymakers-use-them.htm))

### Why real central banks move in steps

Gradual moves let policymakers assess delayed effects and reduce abrupt
changes in financial conditions. Inertial rules explicitly use the preceding
policy rate, and the Federal Reserve considers accumulated tightening and
lags when setting the pace. Our 0.50 limit is a teaching rule, not a universal
limit on real central banks.
([Federal Reserve: inertial rules](https://www.federalreserve.gov/monetarypolicy/policy-rules-and-how-policymakers-use-them.htm),
[November 2022 statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20221102a.htm))

The exception: in 2022, with inflation high and price pressures spreading,
the Federal Reserve made **0.75-point** increases. On June 15, Chair Jerome
Powell described that move as unusually large. Faster catch-up when behind
the curve can outweigh the usual preference for small steps; it still carries
risks. ([June 2022 press conference](https://www.federalreserve.gov/mediacenter/files/FOMCpresconf20220615.pdf))

## ✏️ Try it yourself

For the fourth decision, inflation is **2.99**, gap **−0.55**, and the current
policy rate **3.50**. First work out **2 + 1.5 × 0.99 + 0.5 × (−0.55)**.
Then apply the 0.25 rounding and 0.50 movement limit. Check the table above.

## Loss function

## 🧭 How to read your score

Your score is an **average economic penalty**, not a grade out of 10 or 100.
There is no configured grading-scale maximum: a larger number means larger
weighted costs. The costs are nonnegative. **0 is the ideal**, but the positive
costs in the ten inherited quarters keep this run above 0; reaching 0 is not
your mission.

Both sides average the same ten inherited quarters plus the quarters played.
After five decisions, that is **fifteen rows**. Population and migration do
not enter the score. Unemployment misses count on either side of 4.50%.

Compare with Taylor **at the same quarter**. After five decisions at 2.50,
your **1.976** versus Taylor's **1.952** is a **0.024** larger average penalty,
about **1.23%** using the rounded displayed totals. A falling score or lower
current unemployment alone does not establish a win.

The breakdown shows average contributions, each rounded for display.
Their sum can differ by **0.001** from the separately rounded total: the
inherited **2.203 + 0.016 + 0.000 = 2.219**, while the full total rounds to
**2.220**. Keep the correct numbers; do not change one to make the sum fit.

## 🧮 What one quarter costs

**cost = (inflation − 2)² + 0.5 × (unemployment − 4.5)²
+ 0.25 × (current policy rate − previous policy rate)²**

- **Prices:** the squared inflation miss from 2%.
- **Jobs:** the squared unemployment miss from 4.5%, at half weight.
- **Moves:** the squared policy-rate change, at quarter weight. Even a move
  of 0.25 or 0.50 costs something; only moves **above** 0.50 create financial
  stress as well, and that stress affects the following quarter.

Average over **every** row, including the ten inherited ones; round the final
score to three decimals. The first row has no move cost. The inherited policy
rate never changed, so the starting score is **2.220** for both sides.

## 🔎 Worked from Row 17

After two decisions of 2.50, 2026-Q2 has inflation **3.51**, unemployment
**4.54**, and no new policy-rate change:

**(3.51 − 2)² + 0.5 × (4.54 − 4.5)² + 0.25 × (2.50 − 2.50)²
= 2.2801 + 0.0008 + 0 = 2.2809.**

That is one quarter's cost, not the score. The average over all twelve rows is
**2.250**. After the first 2.50 decision it was **2.248**. A different first
move can change the score immediately through its move cost, even while the
first quarter's gap is still driven by the inherited policy rate.

## 🔎 Why Taylor is ahead in one played game

After your six decisions at 2.50, then 2.00, 2.00, 2.00 and 3.00, Taylor's
recorded policy rates are 2.50, 3.00, 3.50, 3.25, 2.75, 2.50, 2.75, 2.25,
2.50 and 2.75. The policy comparison shows these past choices beside yours;
each recorded policy rate affects the following quarter.

| Average cost | You | Taylor |
|---|---|---|
| Inflation misses | 1.644 | 1.501 |
| Unemployment misses | 0.011 | 0.016 |
| Policy-rate moves | 0.019 | 0.020 |
| Total score | 1.673 | 1.536 |

You are behind by **0.137** using displayed totals. The larger inflation cost
outweighs your savings on jobs and moves. The diagnosis compares accumulated
costs; it does not establish which next policy rate would improve the outcome.
Components and totals are rounded separately.

## 📈 Why squared

A miss of 1 costs 1; a miss of 2 costs 4. A big miss costs more than two small
ones. The same idea penalizes abrupt policy-rate changes.

## ⚖️ Why jobs count at half

The weights **0.5** for jobs and **0.25** for moves are modelling judgements,
not economic constants. A different mandate or concern about financial
stability could justify different weights. Population is shown but does not
enter this score.

## 🏁 Simple strategies, measured

Twenty played quarters, the same shocks, the inherited rows included:

| Strategy | Score | What happens |
|---|---|---|
| The Taylor rule | 1.048 | Inflation ends at 1.78%; worst unemployment 4.91% |
| Hold the policy rate at 5.00% | 6.934 | Inflation ends at -3.52%; worst unemployment 5.54% |
| Hold it at neutral 2.00% | 1.492 | Inflation ends at 2.72%; worst unemployment 4.61% |
| Hold it at 20.00% | 324.686 | Inflation ends at -35.02%; worst unemployment 11.54% |
| Set 12.00 once, then hold 3.00 | 8.215 | Worst unemployment 8.34% |

> 💡 **Beat 1.048 and you beat Taylor.** Row 18 gives the medals; Row 19 is where you try.

## Rules versus discretion

A rule follows a stated procedure; discretion chooses case by case. Both face
the same shocks here. A lower loss answers the question this score asks, not
every question about a good economy. Compare worst unemployment and population
as well, and try another seed before treating a tuned rule as a general result.

## The numbers that are your economy

The neutral policy rate (2%), target (2%), normal unemployment (4.5%), response
coefficients, basket weights, shock ranges, stress threshold, migration rule,
score weights and seed define this world. Change one at a time, state what
changed and keep the relevant tests explicit. Changing several at once makes
it hard to tell which assumption caused the result.
