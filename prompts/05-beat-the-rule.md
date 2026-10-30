# Step 5 — Beat the rule

**You will finish with:** a policy rule of your own, and a score to defend.

## Before you start

Phase 4's check passed: in the assistant's tab, its last test run said `18 passed`.

🎯 Your mission. You are the central bank's research team. The board asks one question: is there a rule that would have served this economy better than Taylor's? Find the A and B with the lowest score whose worst unemployment is no higher than Taylor's. The best rule on the board wins.

The **policy rate** is the interest rate the central bank sets.

**policy rate = 2% + A × (inflation − 2%) + B × output gap**

**A** controls the response to inflation; **B** controls the response to the
output gap. Both rules move toward the formula by at most 0.50 per quarter. Taylor's numbers are **1.5** and **0.5**.

## 👉 Send this prompt

```text
Implement Phase 5 from specs/central-bank-game/tasks.md exactly as written, and nothing beyond it.

Do these in order:
1. Move only later-tests/test_phase_5.py into tests/. Do not change any test.
2. Give rule_rate and rule_run optional a=1.5 and b=0.5 parameters. Use
   them in the formula; keep headline, 0.25 rounding and the 0.50 move limit.
3. GET /rules reads a and b query numbers, defaults 1.5 and 0.5, clamped
   to 0-5. Its separate context has six values:
   a, b, taylor_term = rule_run(TERM), taylor_term_score = loss(taylor_term),
   my_term = rule_run(TERM, a, b), my_term_score = loss(my_term).
   Keep every earlier economy_context variable on Economy and its error paths.
4. Create templates/rules.html, extending base.html with the title Rule lab
   and including ready-made _my_rule.html. In templates/economy.html replace
   that include with the line "🧪 Ready for the board's question? Open the Rule lab."
   linking to /rules, after the legend. Keep all earlier game includes.
   Do not change any ready-made file. Trying a rule must not change the
   player's history, random generator, scoreboard or game.

The application is already running and reloads by itself. Never start, stop
or restart it, never run pkill or kill, and never send requests to it — I
will check it in the browser.

Then run: uv run pytest -q
If anything fails, fix it and run it again until all tests pass.
When all tests pass, stop. Reply with the test line and one sentence. Do not
run anything else, and do not create any other file.
```

## ✅ Check it

1. In the **opencode** tab, the assistant's test run says **`21 passed`**.
2. Open **Rule lab** from the menu. Under **Twenty quarters under each rule**, the
   **🤖 Taylor rule** row reads **1.048** for the score and **4.91** for worst
   unemployment (%). If it does not, something changed that should not have.

Do not move on until these checks pass.

> 💡 **Why Taylor's numbers, and how the score works:** Rows 27 and 28.

## 👉 Now run the experiment

1. Open **Rule lab** and find **Twenty quarters under each rule**.
2. Change **one** number, **A** or **B**, then press **Try my rule**.
3. Read the **🧪 My rule** row and the verdict. Compare it with **🤖 Taylor rule**.

No prompt, no file to edit, no restart. Your game stays as it is.

| Try | Question it answers |
|---|---|
| `A = 0.5` | What happens when you respond to inflation by less than it rose? |
| `A = 3.0` | Is more aggression always better? |
| `B = 0.0` | Does the output gap term earn its place? |

## 👉 Bring it to the board

Find the lowest score whose worst unemployment is no higher than Taylor's; bring A, B, score and worst unemployment to the board.

Can any rule beat Taylor on both — a lower score and a gentler worst quarter? Try. If you can't, say why on the board.

- [ ] `21 passed`
- [ ] My rule's score and worst unemployment are on the board

**Then the two challenges.** [`docs/improve.md`](../docs/improve.md) has the
method and the prompts to fill in.
