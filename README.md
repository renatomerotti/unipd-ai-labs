# UniPD Artificial Intelligence (AI) Lab — you are going to build the Central Bank Game

You are going to build a working web application by telling an AI assistant what
to build. Along the way you will run a country's monetary policy, badly, and
find out why that is harder than it looks.

---

## What this lab asks of you

You will not write code here — the assistant writes every line. Your job is the
harder and more interesting one: decide what should be built, say it precisely
enough that a stranger could build it, and judge what comes back.

No prior Python is assumed, and you will not install it. What you do need is
short:

| You need to | Which means |
|---|---|
| Run short commands | Type them exactly as written and press enter |
| Tell whether the tests passed | The screen says `3 passed` or it does not |
| Tell whether the page loaded | You look at it in your browser |
| Copy an error message | Select it, copy it, paste it to the assistant |

That last one is the whole skill. It is covered below.

If you *do* know Python, you will still learn the thing this lab is about, which
is not Python.

---

## What you are building

**The Central Bank Game.** The **policy rate**, the interest rate the central
bank sets, stayed at the neutral 2.00% while a food and energy surge lifted
inflation to 4.29%. The target is 2%. Now you set the policy rate;
recommended steps are 0.25 or 0.50 percentage points. Watch core inflation and
jobs too. People leave when life gets hard and return when it gets better.

The catch: the economy responds to your decisions **late**. A policy-rate
choice changes demand next quarter; a move above 0.50 points adds financial
stress then too. Inflation can fall while core rises, because the food and
energy surge fades before its pressure has left core.

Across five phases, build the app, reveal the economy, make decisions, add
the scoreboard, then test your own rule. The smoothed Taylor benchmark faces
the same shocks and moves at most 0.50 points per quarter. The score charges
for inflation misses, unemployment misses and policy-rate moves. Can you beat it?

---

## What is in this folder

**This folder is your project.** You build inside it, and everything here is
either something to read or something the assistant will read.

| Where | What it is | When you need it |
|---|---|---|
| `docs/` | Why this exists, and everything explained | Throughout |
| `docs/privacy.md` | Security: the four rules, all in one place | **Before you make an account** |
| `docs/troubleshooting.md` | Questions to ask when something is wrong | The moment you are stuck |
| `docs/methodology.md` | Why we work this way | First session |
| `docs/glossary.md` | Terms about the assistant and the tools | Whenever a word is unfamiliar |
| `docs/economics.md` | Terms about the model you are running | From Phase 2 |
| `docs/improve.md` | The two closing challenges, and the method for both | Last, after Beat the rule |
| `specs/central-bank-game/` | What to build — the assistant reads these | Every phase |
| `templates/` | The page layout and the chart, ready-made | Built against from Phase 1 |
| `tests/` | How each phase is checked | Every phase |
| `later-tests/` | Phases 2–5, one file at a time | When a step says so |
| `pyproject.toml` | What the project needs. You will not edit it | Never, by hand |
| `start.py` | Starts the app and prints its address, ready-made | After Phase 1's tests |
| `stop.py` | Stops the app started by `start.py`, ready-made | When you want to stop it |

The prompts themselves are in the lab, one per step. Both `docs/` and `specs/`
start with a README explaining what each document is for, and which one wins if
two ever disagree.

Start with `uv run start.py`; stop with `uv run stop.py`, in the terminal
on Mac or Windows. Open the address `start.py` prints: usually port 8001,
with 8002 and 8003 as backups. Phase 1's assistant starts it for you.

## The order

1. Read `docs/privacy.md`. It comes first for a reason.
2. Work through the setup steps and get everything installed.
3. Read `docs/methodology.md` — it is short, and it explains why the rest works.
4. Work through the lab steps **in order**, one prompt at a time.
5. Do not start a step until the previous step's check has passed.

Each step ends with something to check. That check is not optional; it is how
you find out that step three went wrong before you reach step seven.

---

## When something is not working

It will. This is normal and it is not your fault.

**Do this:**

1. Copy the **whole** error message. All of it, including the parts that look
   like nonsense.
2. Paste it to the assistant and say: *"This is the error. Fix it."*
3. Run the check again.

Read the error yourself as you paste it — the useful line is usually the last
one, and recognising it is a skill worth having by the end of the day. Hand the
*fixing* to the assistant: it is faster, and the point of the exercise is to
direct it well, not to out-type it.

**Do not:**

* Edit the code by hand to make an error go away. You will not be able to tell
  whether you fixed it or hid it.
* Retype the same prompt hoping for a different answer. You will get a similar
  answer and you will have spent a request.
* Skip ahead to the next step. A broken step three makes step four incoherent.

If it fails twice in a row, the problem is not the wording — it is that the
instruction was ambiguous. Say what you actually want, more precisely, once.

---

## About your daily limit

Start with DeepSeek V4.1 Flash Free (OpenCode), then North Mini Code (free) on OpenRouter, then GLM-5.3-Flash Free (OpenCode), then the instructor. The quota for OpenCode's free models is unpublished; OpenRouter's daily allowance is shared across its free models. Switching models within one provider does not promise a fresh allowance.

One instruction from you often costs several requests, because the assistant
reads a file, writes code, runs the tests, reads the failure, and fixes it.

So: a precise instruction is cheaper than an argument. That is not a moral
point, it is arithmetic. `SETUP.md` explains what to do if you run out.

---

## If you get badly stuck

**Ask for a checkpoint.** There are working copies of the project at the end of
Phases 1 and 2, and the instructor has them. Copy the **contents** of the one
you are given into your project folder and carry on. Phases 3 and 4 have none —
if you are stuck there, ask anyway.

You will have learned less than the person next to you. You will not be stuck,
and you will finish. That trade is fine — take it rather than losing a session.
