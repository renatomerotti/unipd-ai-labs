# Step 3 — Phase 3: set a policy rate, and meet the lag

**You will finish with:** the ability to set the interest rate — and the
discovery that it does not do what you expect.

This is the most important step in the lab.

---

## Before you start

Phase 2's check passed: in the assistant's tab, its last test run said `7 passed`.

If not, fix Phase 2 first, or copy `checkpoints/phase-2-complete/`.

---

## Read this first — do not skip it

Open `specs/central-bank-game/data-model.md` and read **Advancing one quarter**, including the part
headed *Read that once more*.

The one thing that matters: when a new quarter is calculated, it responds to the
policy rate from the **previous** quarter, not the one you just set. Your decision
takes effect the quarter *after* next.

If that gets implemented wrongly, the application still runs and still looks
right — which is why Phase 3 includes a test written specifically to catch it,
`test_new_quarter_uses_the_previous_rate`. Without that test the mistake would
be invisible.

---

## The prompt

```text
Implement Phase 3 from specs/central-bank-game/tasks.md exactly as written, and nothing beyond it.

Do these in order:
1. Move only later-tests/test_phase_3.py into tests/. Do not change any test.
2. Add next_label, advance_quarter, advance and reset to models.py.
3. Add POST /decide and POST /reset to app.py, and keep the full Phase 2
   economy_context on the normal and error paths: history, headline,
   current, previous, current_headline, previous_headline,
   term_start_population and error.
4. Add the policy-rate form, the 0.25/0.50 hint, the stateless large-move
   warning, the stress badge and the reset form to templates/economy.html.
   Put the forms directly below the live heading and prefix every stressed
   quarter's record label with 💥. Keep the ready-made summary, price, people
   and legend includes unchanged.

The application is already running and reloads by itself. Never start, stop or
restart it, never run pkill or kill, and never send requests to it — I will
check it in the browser.

Critical: advance_quarter uses the previous quarter's policy rate, never the
submitted rate, for the gap; stress uses the move between the two preceding
quarters. Draw shocks in demand, food, fuel, energy order. Round the gap before
computing core and unemployment; use rounded inflation for migration. Follow
specs/central-bank-game/data-model.md under "Advancing one quarter" exactly.
Accept any finite policy rate from 0 to 20; do not impose a move limit.

Then run: uv run pytest -q
If anything fails, fix it and run it again until all tests pass.
When all tests pass, stop. Reply with the test line and one sentence. Do not
run anything else, and do not create any other file.
```

---

## What should happen

A form appears directly under the heading. Thirteen tests pass.

One of them is `test_new_quarter_uses_the_previous_rate`. That test exists
purely to catch the mistake described above. If it fails, `advance` is using the
wrong rate.

---

## Check before continuing

1. In the assistant's tab, its test run says `13 passed`.
2. In your browser, refresh the economy page. Under the heading: a policy-rate
   form, and a **Start again from the inherited economy** button.

---

## Now play it — this is the lesson

The application is still running from Step 1. In your browser, open
**the address from Row 15**, followed by `/economy`.

1. Inflation is 4.29% and core is 3.10%. Set the policy rate to **2.50** and submit.
2. Inflation falls to **3.57%**, while core rises to **3.48%**. Fuel and energy fade,
   but that quarter still answers to the inherited 2.00% policy rate.
3. Set **2.50** again and submit.
4. Inflation is **3.51%**, core **3.57%**, unemployment **4.54%**. The first policy
   decision is now affecting the economy. A falling inflation alone is not the whole story.

5. Keep going if you like. Try to get inflation to 2% and see what it costs.

- [ ] `13 passed`
- [ ] You set 2.50 twice and compared inflation with core

Do not open `04-score-and-rule.md` until both are true.
