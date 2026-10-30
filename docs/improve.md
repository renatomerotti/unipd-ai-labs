# Making it yours

The specifications stop at Phase 5. This is about what happens after: two
challenges, and the method for both.

It is not a list of features to add. It is a method, because "be creative" is
not an instruction and staring at a blank prompt box is not a plan.

---

## The method

### 1. One thing

Not five. A prompt asking for five changes produces five half-changes, and you
cannot tell which of them broke the tests.

### 2. Write three lines before you prompt

Actually write them. Not in your head.

```text
1. WHAT CHANGES:
   (one thing)

2. WHICH FILE:

3. HOW I WILL KNOW IT WORKED:
   (something I can run, or see)
```

### 3. Line 3 is the hard one, and it is the point

If you cannot say how you would know it worked, you do not yet know what you
want — and the agent has even less chance of guessing.

| Not a criterion | A criterion |
|---|---|
| The chart looks better | Each axis has a label and there is a legend naming all three lines |
| Make it clearer when I am losing | The score turns red when it is higher than the rule's |
| Add more economics | A second shock, twice the size, hits at one random quarter |

Notice what happened: writing line 3 forced you to decide what you actually
meant. That is most of the work, and it is why it comes before the prompt.

### 4. Prompt once, then check

Build the prompt from your three lines:

```text
Read specs/central-bank-game/data-model.md and models.py.

Change: <line 1>
File: <line 2>
Done when: <line 3>

Change only that. Do not change any existing test. All 21 must still pass.
Then run: uv run pytest -q

The application is already running and reloads by itself. Never start, stop or
restart it, never run pkill or kill, and never send requests to it — I will
check it in the browser.
```

Then check the result against line 3. Not against how it feels.

### 5. If it fails twice, fix the spec

Not the wording. The same request in new words is the same request. Go back to
your three lines and find which one was vague — it is almost always line 1 being
secretly two things, or line 3 being a feeling.

---

## Challenge 1 — add one thing

You are now changing your own version of the game. First add the real
interest rate; then choose your own change. Work on **Economy**, your game.

## 1️⃣ Everyone: the real interest rate

**⌨️ Send this in the opencode tab:**

```text
Read specs/central-bank-game/data-model.md and models.py.

Change: a new column in the table, "Real interest rate %": the policy rate minus inflation
File: templates/economy.html
Done when: for 2025-Q4 the column reads -2.29 (2.00 - 4.29), and all 21 tests still pass

Change only that. Do not change any existing test. All 21 must still pass.
Then run: uv run pytest -q

The application is already running and reloads by itself. Never start, stop or
restart it, never run pkill or kill, and never send requests to it — I will
check it in the browser.
```

> ✅ **Done when** the current test line says **21 passed** and, after refreshing
> **Economy**, a separate **Real interest rate %** header shows **-2.29** for
> **2025-Q4**, alongside the kept **Output gap % 0.70**. Check the header and
> both values; the test line alone does not prove the new column was added.

---

## 2️⃣ Your turn: your own three lines

**Your own change:** choose one other change, or one idea of your own.
Write your three lines before sending a prompt.

| Pick one | 1. What changes | 2. Which file | 3. How I will know it worked |
|---|---|---|---|
| 📉 **The worst quarter** | Next to each score: the highest unemployment and the largest miss from 2% | `app.py` and `templates/economy.html` | Before my first decision it reads **4.50** (2023-Q3) and **2.35** (2025-Q3), for both sides |
| 🌪️ **A difficulty setting** | A **Hard** checkbox that doubles the size of every shock | `models.py` and `templates/economy.html` | With Hard on, **Start again**, then 2.50: 2026-Q1 inflation reads **3.26**, not 3.57 |
| 🤖 **Play the rule's move for me** | A button that sets the policy rate the Taylor rule would choose | `app.py` and `templates/economy.html` | At the start, pressing it sets **2.50** |
| 🎨 **Make it yours** | Your own country, currency and central bank name on the home page | `templates/home.html` | The home page says *You are the central bank of Valdoria*, and still shows inflation 4.29% and the 2% target |

Write these down:

```text
1. WHAT CHANGES:
   (one thing)

2. WHICH FILE:

3. HOW I WILL KNOW IT WORKED:
   (something I can run, or see)
```

**Line 3 is the hard one, and it is the point.** Name something you can see
or check. Put your three lines in place of `<line 1>`, `<line 2>` and
`<line 3>` below. Every change must keep all 21 existing tests passing.

**⌨️ Send this in the opencode tab:**

```text
Read specs/central-bank-game/data-model.md and models.py.

Change: <line 1>
File: <line 2>
Done when: <line 3>

Change only that. Do not change any existing test. All 21 must still pass.
Then run: uv run pytest -q

The application is already running and reloads by itself. Never start, stop or
restart it, never run pkill or kill, and never send requests to it — I will
check it in the browser.
```

> ✅ **Done when** your change passes the check you wrote in line 3, and
> the current test line says **21 passed**. Look at the changed part of
> Economy, or the page you named, before calling it complete.

---

**Failed twice?** Rewrite your three lines, not the prompt. Line 1 was secretly
two things, or line 3 was a feeling.

**Out of requests?** The three lines are still the exercise. Write them, and
bring them to the board.

Next to your score on the board, write **what you changed, and whether line 3
came true**.

- [ ] I wrote my three lines before I prompted (Part 2)
- [ ] My change passes the check I wrote
- [ ] All 21 tests still pass

**Time and requests left? Row 21 — Challenge 2.**

---

## Challenge 2 — answer a bigger question

One good game can be luck. Economists test a question before they believe the answer: predict, build, check.

## 1️⃣ Pick one question

| Question | You predict | You will see |
|---|---|---|
| 🎲 Is your win skill or luck? | Seed 42 was lucky or unlucky for Taylor? | Taylor’s scores for five sets of shocks and their average. |
| ⛽ What does a fuel shock do? | Who recovers faster from a fuel shock: you or Taylor? | Your economy and Taylor’s after the same fuel shock. |
| 🧠 What if people trust the 2% target? | If people trust the 2% target, does Taylor's score go up or down? | Taylor’s score after adding trust in the target. |
| 📉 What does disinflation cost? | Is your sacrifice ratio higher or lower than Taylor's? | The unemployment cost per point of inflation reduction, for you and Taylor. |
| 🏛️ Are two levers better than one? | With government spending as a second lever, can you beat Taylor with less unemployment: yes or no? | A government-spending control beside the policy rate, and the resulting economy. |

## 2️⃣ Write your prediction

Write your choice down before building. A prediction written down cannot quietly change afterwards.

## 3️⃣ Build it, one step at a time

### 🎲 Is your win skill or luck?

**Step 1**

**⌨️ Send this in the opencode tab:**

```text
Read specs/central-bank-game/data-model.md and models.py.

Step 1 of my plan: rule_run takes an optional seed, default 42
File: models.py
Done when: rule_run(20) still scores 1.048, and with seed 1 it scores 1.171

Do these in order:
1. Add one test to tests/test_challenge.py that checks the "Done when" line.
2. Run only that test: uv run pytest -q tests/test_challenge.py
   Show me that it fails. Change no other file before it does.
3. Only then change the code, until that test passes.
4. Run all the tests: uv run pytest -q
Do not change any existing test.

The application is already running and reloads by itself. Never start, stop or
restart it, never run pkill or kill, and never send requests to it — I will
check it in the browser.
```

> ✅ **Done when** rule_run(20) still scores 1.048, and with seed 1 it scores 1.171.

---

**Step 2**

**⌨️ Send this in the opencode tab:**

```text
Read specs/central-bank-game/data-model.md and models.py.

Step 2 of my plan: the page shows Taylor's score for seeds 1 to 5, and their average
File: app.py, templates/economy.html
Done when: it shows 1.171, 1.256, 1.307, 1.131, 1.354 and the average 1.244

Do these in order:
1. Add one test to tests/test_challenge.py that checks the "Done when" line.
2. Run only that test: uv run pytest -q tests/test_challenge.py
   Show me that it fails. Change no other file before it does.
3. Only then change the code, until that test passes.
4. Run all the tests: uv run pytest -q
Do not change any existing test.

The application is already running and reloads by itself. Never start, stop or
restart it, never run pkill or kill, and never send requests to it — I will
check it in the browser.
```

> ✅ **Done when** it shows 1.171, 1.256, 1.307, 1.131, 1.354 and the average 1.244.

---

### ⛽ What does a fuel shock do?

**Step 1**

**⌨️ Send this in the opencode tab:**

```text
Read specs/central-bank-game/data-model.md and models.py.

Step 1 of my plan: rule_run takes an optional fuel_quarter; in that quarter, add 20 points to fuel inflation after its normal update and before computing inflation and migration
File: models.py
Done when: with the fuel shock in quarter 3, Taylor's quarter-3 inflation reads 3.79 instead of 2.99, and without it Taylor still scores 1.048

Do these in order:
1. Add one test to tests/test_challenge.py that checks the "Done when" line.
2. Run only that test: uv run pytest -q tests/test_challenge.py
   Show me that it fails. Change no other file before it does.
3. Only then change the code, until that test passes.
4. Run all the tests: uv run pytest -q
Do not change any existing test.

The application is already running and reloads by itself. Never start, stop or
restart it, never run pkill or kill, and never send requests to it — I will
check it in the browser.
```

> ✅ **Done when** with the fuel shock in quarter 3, Taylor's quarter-3 inflation reads 3.79 instead of 2.99, and without it Taylor still scores 1.048.

---

**Step 2**

**⌨️ Send this in the opencode tab:**

```text
Read specs/central-bank-game/data-model.md and models.py.

Step 2 of my plan: a checkbox Fuel shock in quarter 3 that applies it to my game and to Taylor's
File: models.py, app.py, templates/economy.html
Done when: with it on, my third new quarter's inflation is exactly 0.80 points higher than with it off, for the same policy rates

Do these in order:
1. Add one test to tests/test_challenge.py that checks the "Done when" line.
2. Run only that test: uv run pytest -q tests/test_challenge.py
   Show me that it fails. Change no other file before it does.
3. Only then change the code, until that test passes.
4. Run all the tests: uv run pytest -q
Do not change any existing test.

The application is already running and reloads by itself. Never start, stop or
restart it, never run pkill or kill, and never send requests to it — I will
check it in the browser.
```

> ✅ **Done when** with it on, my third new quarter's inflation is exactly 0.80 points higher than with it off, for the same policy rates.

---

### 🧠 What if people trust the 2% target?

**Step 1**

**⌨️ Send this in the opencode tab:**

```text
Read specs/central-bank-game/data-model.md and models.py.

Step 1 of my plan: a setting TRUST = 0.0; subtract TRUST × (previous core − 2) from the existing core update before rounding; keep the gap and energy pass-through terms
File: models.py
Done when: with TRUST = 0.0 Taylor still scores 1.048, and with TRUST = 0.1 it scores 0.959

Do these in order:
1. Add one test to tests/test_challenge.py that checks the "Done when" line.
2. Run only that test: uv run pytest -q tests/test_challenge.py
   Show me that it fails. Change no other file before it does.
3. Only then change the code, until that test passes.
4. Run all the tests: uv run pytest -q
Do not change any existing test.

The application is already running and reloads by itself. Never start, stop or
restart it, never run pkill or kill, and never send requests to it — I will
check it in the browser.
```

> ✅ **Done when** with TRUST = 0.0 Taylor still scores 1.048, and with TRUST = 0.1 it scores 0.959.

---

**Step 2**

**⌨️ Send this in the opencode tab:**

```text
Read specs/central-bank-game/data-model.md and models.py.

Step 2 of my plan: set TRUST = 0.1
File: models.py
Done when: the Twenty quarters table's 🤖 Taylor row reads 0.959. Then try a gentler rule in its form, such as A = 1.0, and see whether it beats Taylor

Do these in order:
1. Add one test to tests/test_challenge.py that checks the "Done when" line.
2. Run only that test: uv run pytest -q tests/test_challenge.py
   Show me that it fails. Change no other file before it does.
3. Only then change the code, until that test passes.
4. Run all the tests: uv run pytest -q
Do not change any existing test.

The application is already running and reloads by itself. Never start, stop or
restart it, never run pkill or kill, and never send requests to it — I will
check it in the browser.
```

> ✅ **Done when** the Twenty quarters table's 🤖 Taylor row reads 0.959. Then try a gentler rule in its form, such as A = 1.0, and see whether it beats Taylor.

---

### 📉 What does disinflation cost?

**Step 1**

**⌨️ Send this in the opencode tab:**

```text
Read specs/central-bank-game/data-model.md and models.py.

Step 1 of my plan: a function sacrifice_ratio(quarters): add up unemployment above 4.5 over the played quarters, and divide by how far inflation fell from 4.29
File: models.py
Done when: for Taylor's twenty quarters it returns 0.73 (1.83 ÷ 2.51); return “not defined” if inflation did not fall

Do these in order:
1. Add one test to tests/test_challenge.py that checks the "Done when" line.
2. Run only that test: uv run pytest -q tests/test_challenge.py
   Show me that it fails. Change no other file before it does.
3. Only then change the code, until that test passes.
4. Run all the tests: uv run pytest -q
Do not change any existing test.

The application is already running and reloads by itself. Never start, stop or
restart it, never run pkill or kill, and never send requests to it — I will
check it in the browser.
```

> ✅ **Done when** for Taylor's twenty quarters it returns 0.73 (1.83 ÷ 2.51); return “not defined” if inflation did not fall.

---

**Step 2**

**⌨️ Send this in the opencode tab:**

```text
Read specs/central-bank-game/data-model.md and models.py.

Step 2 of my plan: the page shows the sacrifice ratio for me and for Taylor's rule, side by side
File: app.py, templates/economy.html
Done when: Taylor's reads 0.73

Do these in order:
1. Add one test to tests/test_challenge.py that checks the "Done when" line.
2. Run only that test: uv run pytest -q tests/test_challenge.py
   Show me that it fails. Change no other file before it does.
3. Only then change the code, until that test passes.
4. Run all the tests: uv run pytest -q
Do not change any existing test.

The application is already running and reloads by itself. Never start, stop or
restart it, never run pkill or kill, and never send requests to it — I will
check it in the browser.
```

> ✅ **Done when** Taylor's reads 0.73.

---

### 🏛️ Are two levers better than one?

**Step 1**

**⌨️ Send this in the opencode tab:**

```text
Read specs/central-bank-game/data-model.md and models.py.

Step 1 of my plan: advance(rate, spending=0.0); spending is added to the new quarter's output gap before rounding
File: models.py
Done when: with spending 0 all 21 tests still pass, and a new test shows spending 1.0 makes the new quarter's gap exactly 1.00 higher

Do these in order:
1. Add one test to tests/test_challenge.py that checks the "Done when" line.
2. Run only that test: uv run pytest -q tests/test_challenge.py
   Show me that it fails. Change no other file before it does.
3. Only then change the code, until that test passes.
4. Run all the tests: uv run pytest -q
Do not change any existing test.

The application is already running and reloads by itself. Never start, stop or
restart it, never run pkill or kill, and never send requests to it — I will
check it in the browser.
```

> ✅ **Done when** with spending 0 all 21 tests still pass, and a new test shows spending 1.0 makes the new quarter's gap exactly 1.00 higher.

---

**Step 2**

**⌨️ Send this in the opencode tab:**

```text
Read specs/central-bank-game/data-model.md and models.py.

Step 2 of my plan: a Government spending box next to the policy rate
File: app.py, templates/economy.html
Done when: from the start, 2.50 with spending 1.0 gives a 2026-Q1 output gap of 1.08 instead of 0.08

Do these in order:
1. Add one test to tests/test_challenge.py that checks the "Done when" line.
2. Run only that test: uv run pytest -q tests/test_challenge.py
   Show me that it fails. Change no other file before it does.
3. Only then change the code, until that test passes.
4. Run all the tests: uv run pytest -q
Do not change any existing test.

The application is already running and reloads by itself. Never start, stop or
restart it, never run pkill or kill, and never send requests to it — I will
check it in the browser.
```

> ✅ **Done when** from the start, 2.50 with spending 1.0 gives a 2026-Q1 output gap of 1.08 instead of 0.08.

---

**The test must fail first.** A test that passes before the code exists checks
nothing.

**Touching** `advance()`**?** Every number in the app depends on it. Change one
thing at a time.

### A question of your own

**⌨️ Send this in the opencode tab:**

```text
Read specs/central-bank-game/data-model.md and models.py.

Step <n> of my plan: <line 1>
File: <line 2>
Done when: <line 3>

Do these in order:
1. Add one test to tests/test_challenge.py that checks the "Done when" line.
2. Run only that test: uv run pytest -q tests/test_challenge.py
   Show me that it fails. Change no other file before it does.
3. Only then change the code, until that test passes.
4. Run all the tests: uv run pytest -q
Do not change any existing test.

The application is already running and reloads by itself. Never start, stop or
restart it, never run pkill or kill, and never send requests to it — I will
check it in the browser.
```

> ✅ **Done when** <line 3>.

---

## 4️⃣ Answer the question

Was your prediction right? If not, **what did the model know that you did
not?** That sentence goes on the board.

**It costs more requests than anything else in the lab.** If you run out
halfway, your prediction and your plan are still an answer worth bringing.

- [ ] I wrote my prediction before building anything
- [ ] Each step started with a failing test
- [ ] I can say whether my prediction was right, and why

---

## Two warnings

**Do not touch `advance()` lightly.** Every other number in
the application depends on it. If you change the model, change one coefficient
at a time and watch what happens — that is an experiment. Changing three at once
is not.

**Keep the tests passing.** If your change breaks an existing test, one of two
things is true: you broke something, or the test was checking behaviour you
deliberately changed. Work out which, and say so in your next prompt. Deleting a
failing test to make the screen green is how software gets bad.

---

## After the course

Everything here applies to any project with any agent, and none of it is about
this simulation.

Write down what you want. Break it into steps you can check. Decide how you will
know it worked before you start. When it fails twice, fix the specification.

The rest is practice.
