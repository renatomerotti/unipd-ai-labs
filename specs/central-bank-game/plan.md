# Plan — Central Bank Game

The technical approach. What to type is [tasks.md](tasks.md).

## Shape

Two Python modules (`app.py`, `models.py`) and three authored templates
(`home.html`, `economy.html`, `rules.html`), beside shared ready-made templates and tests.
Five phases, one folder, no database, no authentication or build step.
Dependencies remain in the supplied `pyproject.toml`.

## Why the phases split where they do

| Phase | Adds | Visible outcome | Cumulative tests |
|---|---|---|---|
| 1 | app and briefing | Food and energy surge; inflation, core, people | 3 |
| 2 | inherited quarters, inflation function, economy route | Record, prices and population | 7 |
| 3 | advance/reset, form, lag, stress, migration | Play a quarter and watch the economy | 13 |
| 4 | move-aware loss and smoothed Taylor rule | Chart, faces, score, cost diagnosis and past-policy comparison | 18 |
| 5 | optional A/B coefficients and GET /rules | Separate Rule lab, twenty quarters under each rule; game unchanged | 21 |

## Dependencies between phases

```text
1 → 2 → 3 → 4 → 5
```

`advance_quarter(quarters, rate, generator)` keeps one economic calculation for
player and opponent. `advance(rate)` calls it with the player history; `rule_run`
calls it with a copy and fresh seed. Stored values never change after creation.
`headline(quarter)` computes the rounded weighted sum on demand.

## Implementation risks

The lag and stress both use decisions already recorded. The four random draws
have a fixed order. Core inflation uses the rounded gap; migration uses rounded inflation.
Score includes the move made in each row and every inherited row. A shared
`economy_context` prevents incomplete contexts on validation and term-ending errors.
A/B comparisons must not touch the player or its generator.

## Testing approach

One unchanged ready-made test file per phase adds 3 / 4 / 6 / 5 / 3 tests.
Tests use `starlette.testclient.TestClient`, reset history and seed between cases,
and pin the inherited figures, two 2.50 decisions and four twenty-quarter strategies.
Template contracts are exercised under Jinja's strict undefined-value handling.
A browser check at 390 px covers layout; tests alone do not prove rendering.
