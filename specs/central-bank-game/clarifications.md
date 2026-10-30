# Clarifications — Central Bank Game

Questions settled before students build. [data-model.md](data-model.md) owns the
arithmetic; [tasks.md](tasks.md) owns exact files, function names and contexts.

## Contradictions found

| # | The problem | Settled |
|---|---|---|
| C1 | Script headers were not read by the test runner | Dependencies remain only in `pyproject.toml` |
| C2 | Imports could miss the project root | The supplied test configuration sets `pythonpath = ["."]` |
| C3 | Validation errors lacked chart variables | Economy and decision errors use the complete game context; the separate /rules route owns the six experiment values |
| C4 | Tests could share history and random state | Reset history and seed before and after each mutating test |
| C5 | A falling inflation might suggest policy already worked | Two 2.50 decisions give inflation 3.57 / 3.51 but core 3.48 / 3.57; first effects still lag |
| C6 | Large moves were costless | Score charges the current move; stress reduces next quarter's gap |

## Ambiguities settled

| # | Question | Answer |
|---|---|---|
| A1 | Store inflation? | No: use the same rounded `headline(quarter)` function everywhere |
| A2 | Round gap before core and unemployment? | Yes, with Python's built-in `round()` |
| A3 | Draw order? | Demand, food, fuel, energy, from one seeded generator |
| A4 | Which move causes stress? | The absolute difference between the previous two recorded policy rates |
| A5 | Can a player make a large or non-grid move? | Yes: any finite policy rate 0–20, form `step="any"`; warn above 0.50 |
| A6 | Does Taylor have the same freedom? | It rounds to 0.25 and moves at most 0.50 per quarter |
| A7 | Does migration change the score? | No: people are shown only; movements round to hundreds |
| A8 | Which unemployment attribute? | `quarter.unemployment`, keeping the existing template convention |
| A9 | Which chart names? | `player_inflation` and `rule_inflation` now carry inflation; `player_core` carries core |
| A10 | Population change starts when? | At the last inherited population, 10,000,000 |
| A11 | Scores equal? | Show tied; retain the existing tie-inclusive gold boundary |
| A12 | Is the warning stored? | No: derive it from the last two quarters on every render |
| A13 | Which layout? | Bootstrap 5.3.3 in the supplied base; shared templates own cards, faces, chart and past-policy comparison; Phase 5 authors a separate rules.html experiment page |
| A14 | Which files may a rebuild collect? | Only Phase 2 through the requested phase's tests from `later-tests/`; never any other file there |

## Left open on purpose

Students choose their strategy and later their A/B coefficients. The economic
rules, reference figures, shared templates and tests are fixed. Creative changes
come after all five phases pass.
