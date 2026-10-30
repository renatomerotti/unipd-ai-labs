# Product Requirements Document (PRD) — Central Bank Game

The player is the central bank of a country: they set its **policy rate**, the
interest rate the central bank sets, quarter by quarter, and live with what follows.

What we are building, from the user's side. It does not name files or functions;
that is [`../specs/central-bank-game/spec.md`](../specs/central-bank-game/spec.md).

## The problem

Students on a Master's in Applied Economics are asked to direct an artificial intelligence (AI) coding
assistant, most of them for the first time, on free-tier models with a daily
request limit. They need a focused project with visible checks and an economic question
worth investigating.

## Who it is for

| | |
|---|---|
| Primary | Master's students, University of Padua, 2026. Mixed ability. Some have never used an AI assistant; some are rusty on Python |
| Secondary | The instructor, who must support twenty-five people at once |

## What the player can do

- See ten inherited quarters: a neutral 2.00% policy rate and a food and
  energy surge, ending with inflation 4.29% and core inflation 3.10%.
- Set the policy rate for the coming quarter.
- Watch the delayed demand effect and the financial stress caused by large moves.
- Compare inflation with core, food, fuel and energy inflation.
- See people arrive or leave as hardship changes, with population shown but not scored.
- See their whole record as a table and a chart.
- Compare inflation, unemployment and move costs against a smoothed Taylor rule
  facing the same shocks and moving at most 0.50 points per quarter.
- Try their own rule coefficients without changing their game.
- Serve a term of twenty quarters, get a medal, and start again for another.

## In scope

- One web application, run locally by the student.
- An in-memory history of quarters.
- Five build phases, each with a visible result and a check.

## Out of scope

- Accounts, logins, or anything that survives a restart.
- Live economic data. Every number comes from the model.
- Deployment or hosting.
- Realism beyond the equations in
  [`../specs/central-bank-game/data-model.md`](../specs/central-bank-game/data-model.md). This is a
  teaching model, not a forecast.

## How we know it worked

1. Every student has an application they built by directing an assistant.
2. Every student can explain why their first attempt at stabilisation failed.
3. No student was blocked by a broken file, an exhausted allowance, or a failed
   installation.

The first is necessary. The second is the point. The third is the one that
decides whether the other two happen.
