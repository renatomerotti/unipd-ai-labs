# How we are going to work

Read this before you build anything. It is short, and it explains why the rest
of the lab is shaped the way it is.

**Working with an agent** · [The one idea](#the-one-idea) · [Why not just chat](#why-not-just-chat-to-it) · [Writing it down](#writing-it-down) · [Why small steps](#why-small-steps) · [Why the prompts are files](#why-the-prompts-are-separate-files) · [Why tests](#why-we-check-with-tests) · [The two-failure rule](#the-two-failure-rule)

---

## The one idea

Everything below follows from one picture. If you remember nothing else,
remember this.

```text
The agent is a very fast, very literal junior developer
who has never met you, cannot see your screen,
and forgets everything the moment the conversation ends.
```

Not stupid. A **stranger with no memory**.

Think about how you would brief a competent stranger who starts on Monday and
leaves on Monday evening, having forgotten everything. You would write things
down. You would be specific. You would check their work.

That is the whole method.

---

## Why not just chat to it?

### In plain words

You *can* just chat. It is called **vibe coding**: "make it nicer", "no, not
like that", "try again". It feels productive because something is always
happening.

It goes wrong in a way that is hard to notice. Each message nudges the work a
little, nobody wrote down what "nicer" meant, and after twenty messages you have
something nobody chose.

### The real reason, for this lab

Two things make vibe coding fail here specifically.

**One: your free account has a daily limit on requests.** Not words —
*requests*. And one instruction from you costs several, because the agent reads
a file, writes code, runs the tests, reads the failure, and fixes it. Five
requests for one sentence.

An argument costs twenty requests and produces drift. A precise instruction
costs five and produces the thing you wanted. You have enough for the second and
not the first.

**Two: a free model is more literal than an expensive one.** A strong model
guesses well when you are vague. A free one does exactly what you wrote. That
sounds worse and is actually clarifying: it means vagueness has visible
consequences instead of hidden ones.

So the constraint is not really about money. It is that **being precise is
cheaper than being vague**, and here you can watch it happen.

---

## Writing it down

### In plain words

Imagine building a treehouse.

You could stand under the tree shouting instructions. Or you could draw it
first — how big, how many steps on the ladder, where the window goes — and then
build from the drawing.

Shouting works for a small treehouse and one afternoon. The drawing survives:
someone else can build from it, and you can tell whether what got built is what
you asked for.

### The real reason

This is called **spec-driven development**: decide what you want, write it down
precisely, then ask once.

The important property is not precision for its own sake. It is that **the
written thing survives the conversation.**

Start a new session — close the **opencode** tab and open it again — and the
assistant has no memory of the last one. (Switching model with `/models` is not
the same: the new model reads the same conversation.) But `specs/central-bank-game/tasks.md` is still there, and any
agent, on any day, can read it and carry on.

This is testable, and it gets tested. If a project breaks badly there is a
rebuild prompt — ask for it — that rebuilds the whole thing from `specs/` with
an assistant that has never seen the earlier work. It works. That is the
argument, and somebody in the room usually gets to run the experiment.

### Two documents, two jobs

```text
PRD                          Spec
What are we building,        Exactly how should
and why?                     it behave?
```

A **Product Requirements Document (PRD)** says: *"the player sets an interest
rate each quarter and tries to get inflation back to target."* It is about
people and purpose. In this lab that is `docs/prd.md`. (`docs/mission.md` is
shorter and sits behind it: not what we are building, but why it is worth
building at all.)

A **spec** says: *"`POST /decide` accepts a rate between 0 and 20, appends one
quarter to the history, and redirects with status 303."* It is about behaviour.
In this lab that is `specs/central-bank-game/tasks.md`.

You need both. A PRD without a spec produces something plausible that does the
wrong thing. A spec without a PRD produces something precise that nobody wanted.

---

## Why small steps

### In plain words

You would not hand a stranger a whole building and come back in a week.

### The real reason

Large requests drift. Not because the agent gets tired, but because a large
request has more places to be ambiguous, and each one is resolved by guessing.
Twenty guesses compound.

A small request has fewer places to go wrong, and — more importantly — you can
*check it*. A phase you can verify is a phase you can trust and build on.

This lab has four phases:

1. The application runs.
2. The economy you inherited is visible.
3. You can set a policy rate — and meet the delay.
4. You get a score, and something to lose to.

Each ends with a check. If the check fails, you fix it *there*, while the
mistake is one step old rather than four.

---

## Why the prompts are separate files

Because you will lose your place.

Not because you are careless — because a room is noisy, someone asks you a
question, your phone buzzes, and you look back at the screen. In one long
document you cannot tell where you were. In a numbered file you can: the name is
in the tab.

And skipping a step in a long document fails *silently*. The agent will happily
build step five against a project missing step three, and the error surfaces
much later as something incomprehensible.

Every prompt file therefore begins with a check. If it fails, you are in the
wrong file, and you know immediately.

---

## Why we check with tests

### In plain words

"It looks right" is not knowing. Especially when you did not write the code.

### The real reason

You cannot review code you did not write and may not read fluently. So you need
a signal that does not depend on your judgement.

A test is code that checks other code. Run one command and the screen says
`7 passed` or it does not. No interpretation required.

This matters more with an agent than without one, because an agent produces
**confident** output. It does not hedge. A test does not care how confident
anything was.

Every phase in this lab specifies its tests before you build it. That order is
deliberate: deciding how you will know it worked, *before* you build it, is what
stops "done" from meaning "I got bored".

---

## The two-failure rule

The most useful rule in this document.

> If the same instruction fails twice, the problem is not the wording. It is
> that the instruction was ambiguous. Fix the specification, not the prompt.

Rewording is the same request wearing a hat. It costs another request and gets a
similar answer, because the agent understood you fine — you just did not say
what you meant.

Stop. Work out what was underspecified. Say that instead. Once.

---

## What this looks like in your lab

| The idea | Where you meet it |
|---|---|
| Write it down | `specs/` — the agent reads these, not your chat history |
| PRD versus spec | `docs/prd.md` versus `specs/central-bank-game/tasks.md` |
| Small steps | Four phases, each with its own check |
| One prompt per step | the lab rows, numbered, in order |
| Check, do not guess | `uv run pytest -q` |
| Specs survive conversations | the rebuild prompt — `troubleshooting.md` X2 |
| Precision is cheaper | Your daily request allowance |

---

## The one sentence to take away

You are not learning to code with an AI. You are learning to **say what you want
precisely enough that someone who has never met you can build it** — which turns
out to be a general skill, and a rarer one than it sounds.
