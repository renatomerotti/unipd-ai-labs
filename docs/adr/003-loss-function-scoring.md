# Architecture Decision Record (ADR) 003: score with a loss function

**Status:** Accepted · 2026-09-10; updated for the realistic model, 2026-10-24.
Supersedes the earlier inflation-only score and adds a cost for policy-rate moves.

## Context

Scoring inflation alone ignores jobs and abrupt policy changes. The realistic
model separates inflation from core inflation, adds financial stress after a
large move, and shows migration. The scoreboard must state which outcomes it
judges.

## Decision

The **policy rate** is the interest rate the central bank sets. Score:

```text
loss = mean((headline − 2.0)² + 0.5 × (unemployment − 4.5)²
            + 0.25 × (current policy rate − previous policy rate)²)
```

Include all inherited quarters; the first row has no move cost. Average before
rounding to three decimals. Lower is better. Population is shown but not scored.
A small move has a score cost even when it causes no financial stress.

## Consequences

**Good.** Twenty quarters holding the policy rate at 20 score **324.686**, with
worst unemployment **11.54%**. A move to 12 followed by nineteen decisions of 3
scores **8.215**, with worst unemployment **8.34%**. Abrupt tightening is costly.

**Good.** The smoothed Taylor benchmark scores **1.048**, with worst
unemployment **4.91%**. Its actual moves are limited to 0.50 points per quarter;
the player receives a small-step recommendation but may choose any finite
policy rate from 0 to 20.

**Cost.** Three squared terms require more arithmetic than an inflation miss.
The weights are modelling judgements, not estimates. A lower loss can still
come with a harsher worst quarter, so compare both columns.

**Related.** The Taylor formula uses a 1.5 inflation response, but its actual
decisions are rounded to 0.25-point steps and smoothed. See the data model and
[economics](../economics.md) for worked decisions and the Taylor principle.
