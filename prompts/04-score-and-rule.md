# Step 4 — Phase 4: chart, score, and your opponent

**You will finish with:** a chart of your record, a score, and a mechanical rule
to compare with.

---

## Before you start

Phase 3's check passed: in the assistant's tab, its last test run said `13 passed`.

---

## Read this first

Open `specs/central-bank-game/data-model.md` and read **The benchmark rule** and **The score**.

Two things matter:

* Your score is a **loss function**. It charges you for missing the inflation
  target, for the unemployment you caused, and for policy-rate moves. A score that only measured
  inflation would reward wrecking the economy.
* The rule must face the **same shocks** you did, or the comparison means
  nothing — and nothing will look wrong.

---

## The prompt

```text
Implement Phase 4 from specs/central-bank-game/tasks.md exactly as written, and nothing beyond it.

Do these in order:
1. Move only later-tests/test_phase_4.py into tests/. Do not change any test.
2. Add LAMBDA, NU, TERM, loss, rule_rate and rule_run to models.py.
3. Keep every existing economy_context variable and add rule_history,
   player_score, rule_score, term, labels, player_inflation,
   rule_inflation and player_core. Both inflation arrays carry computed inflation;
   the core array carries core. Supply them on every error path too.
4. End the term after twenty decisions and hide the policy-rate form then.
5. In templates/economy.html order the heading, ready-made _scoreboard.html,
   policy-rate and reset forms, _chart.html, _policy_comparison.html,
   _summary.html, _prices.html,
   _people.html, table and _legend.html. Do not write scoreboard or chart
   code or change any ready-made file. Keep all earlier includes.

The application is already running and reloads by itself. Never start, stop or
restart it, never run pkill or kill, and never send requests to it — I will
check it in the browser.

Two things must be exactly as specified:
1. loss includes the current move squared with weight 0.25; inherited rows
   count. rule_rate moves toward the inflation-based formula in 0.25 steps,
   never more than 0.50 per quarter, and remains between 0 and 20.
2. rule_run creates a FRESH random.Random(SEED), uses advance_quarter on
   its own list and must not change the real history or random generator.

Then run: uv run pytest -q
If anything fails, fix it and run it again until all tests pass.
When all tests pass, stop. Reply with the test line and one sentence. Do not
run anything else, and do not create any other file.
```

---

## Check

1. In the assistant's tab, its test run says `18 passed`.
2. In your browser, refresh the economy page.

Your Phase 3 game is gone, and that is expected: building Phase 4 restarted the
app, so the table is back to the ten inherited quarters. Your twenty-quarter term
starts here.

- [ ] `18 passed`
- [ ] The scoreboard at the top: the Taylor rule against you, with both scores and who is ahead
- [ ] A chart with your inflation, Taylor inflation, dashed core and the 2% target

---

## First, a puzzle

The inherited scores are both **2.220**. Your first decision can already change
who is ahead: the move cost is charged immediately, although the economic effect
still waits a quarter. Compare the score and the inflation/core cards separately.

## Now argue with it

Submit a few more, then look again. Compare your score with the rule's.

Ask yourself, before the discussion:

* Did the rule beat you because it was smarter, or because it was *steadier*?
* Watch the 👷 **Workers** on both cards as you play. Whose unemployment climbed
  higher? Step 5 measures the worst quarter exactly.
* You had discretion and the rule had none. Was that an advantage?

## 🧘 The steady hand

Central banks prize few, well-timed moves. Bring inflation into 1.75%–2.25% with the fewest policy-rate changes, in steps of 0.25 or 0.50. Ties: the earlier quarter, then the lower worst unemployment. Bring your count to the board.

Keep this open. You will need it.
