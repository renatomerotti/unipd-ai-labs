# Glossary — the assistant, and how we work

Plain language first. Nothing here assumes you have used an artificial intelligence (AI) assistant or
written code before.

The economics is in [economics.md](economics.md) — you need it from Phase 2.

**Working with an agent** — Agent · Prompt · Context · Model · Provider · Token · Request · Quota · Application Programming Interface (API) key · Hallucination

**Writing it down** — Vibe coding · Spec-driven development · Product Requirements Document (PRD) · Spec · Mission · Roadmap · Tech stack · Phase · Acceptance criteria · Test · Checkpoint

**Tools and what you see** — Integrated Development Environment (IDE) · Extension · Terminal · Command · Traceback · localhost · Port · Function · Import · Repository · Commit · Route · Template · Dataclass · Dependency

---

## Start with one idea

```text
The agent is a very fast, very literal junior developer
who has never met you, cannot see your screen,
and forgets everything the moment the conversation ends.
```

That is why you write instructions down instead of chatting. Why you work in
small steps. Why you name the exact file. Not because it is stupid — because it
is a stranger with no memory.

---

## The pairs that cause the most confusion

```text
PRD                          Spec
What are we building,        Exactly how should
and why?                     it behave?
```

```text
Prompt                       Spec
What you say right now.      What stays true after
                             the conversation ends.
```

```text
Model                        Provider
The AI itself.               The company you get it from.
```

```text
Token                        Request
A piece of text,             One round trip to the model.
about ¾ of a word.           Your daily limit counts these.
```

```text
Vibe coding                  Spec-driven development
"Make it nicer."             Decide what "nicer" means.
"No, not like that."         Write it down. Ask once.
```

```text
Test                         Acceptance criteria
Code that checks             The sentence saying what
the app works.               "works" means.
```

---

## Working with an agent

**Agent** — an AI that does not just answer but *acts*: reads your files, writes
new ones, runs commands, reads the errors, tries again. A chatbot tells you what
to type; an agent types it. *In the lab:* OpenCode, inside VS Code.

**Prompt** — what you say to the agent. Closer to a work order than a question:
which file, which behaviour, and how you will know it worked.

**Context** — everything the agent can see right now: your prompt, the files it
has opened, what was said earlier. **It is not memory.** Close the conversation
and it is gone — which is why your project's knowledge belongs in `specs/`.

**Model** — the AI itself. *In the lab:* a free one. Capable, but literal: it
does what you wrote, not what you meant.

**Provider** — the company serving the model. The same model is often sold by
several at different prices. *In the lab:* OpenRouter.

**OpenCode's free models** — OpenCode's makers run these models; no account and no key are needed.

**Token** — a chunk of text, roughly ¾ of a word. Models read and write in
tokens, and paid models are priced per million.

**Request** — one round trip to the model, and the unit your daily limit counts.
One instruction from you often costs several: read a file (one), write code
(two), run tests (three), read the failure (four), fix it (five). This is why a
precise prompt is cheaper than an argument.

**Quota** — your cap on requests. Two things surprise people: it resets
**daily** on OpenRouter, where it belongs to your **account**, not to a model. The quota for OpenCode's free models is unpublished; switching between its models does not promise another allowance. The lab starts on DeepSeek V4.1 Flash Free (OpenCode), then North Mini Code (free) on OpenRouter, then GLM-5.3-Flash Free (OpenCode), then the instructor.

**API key** *(Application Programming Interface key)* — a long secret string
proving a request is yours. Treat it as a password; anyone holding it can spend
your quota. Never paste it into a file, a screenshot or a message.

**Hallucination** — a model stating something false with complete confidence: a
function that does not exist, a library nobody wrote. It is not lying; it has no
notion of true. This is why every phase ends with a check you run yourself.

---

## Writing it down

**Vibe coding** — steering by feel. "Make it look better." "Hmm, try again."
Sometimes fine with a strong model and a tiny task. With a free model and a
daily limit it fails twice: results drift, and you run out of requests arguing.

**Spec-driven development (SDD)** — decide what you want, write it down
precisely, ask once. Prompts are disposable; the written spec is what lets a
different model, on a different day, continue your work.

**PRD** *(Product Requirements Document)* — the thing from the user's point of
view. What problem, for whom, why it matters, what they can do, what is in and
out of scope, how we know it worked. It does not name files or functions.
*In the lab:* `docs/prd.md`.

**Spec** — exactly how it must behave. Where a PRD says *"the user can set the
policy rate"*, a spec says *"`POST /decide` accepts a policy rate between 0 and 20,
appends one quarter, and redirects with 303."* *In the lab:* `specs/central-bank-game/tasks.md`.

**Mission** — the shortest statement of what the project is for, so later
decisions have something to be measured against.

**Roadmap** — the order the work happens in, broken into phases.

**Tech stack** — the tools and versions, written down so nobody guesses.

**Phase** — one self-contained piece of work with a visible result and a check
at the end. Small requests succeed; large ones drift. *In the lab:* five.

**Acceptance criteria** — the sentence that decides whether something is done.
"Better charts" is not one. "The chart shows a dashed line at 2% and the axis is
labelled in quarters" is. If you cannot write the criterion, you do not yet know
what you want — and neither will the agent.

**Test** — code that checks the app still behaves, run by a command rather than
by eye. *In the lab:* `uv run pytest -q`

**Checkpoint** — a saved working copy at the end of a phase. If your files break
or your quota runs out, copy it and carry on. You will have learned less; you
will not be stuck.

---

## Tools and what you see

**IDE** *(Integrated Development Environment)* — the program you write code in.
*In the lab:* Visual Studio Code.

**Extension** — an add-on giving the editor a new ability. *In the lab:*
OpenCode, which puts an agent inside VS Code.

**Terminal** — the text window where you type commands instead of clicking.

**Command** — a line you type there. *In the lab:* `uv run start.py` starts
the app, `uv run stop.py` stops it, and `uv run pytest -q` checks the tests.
Type them exactly, dashes included.

**Traceback** — the long alarming block that appears when something goes wrong,
listing which line failed and what called it. **It is not addressed to you.**
Copy the whole thing and give it to the agent, which reads these better than you
do. Learning to do this is the single most useful habit in the lab.

**localhost** — your own computer, addressed as if it were a website.
`http://127.0.0.1:8001` means *this machine, port 8001*. Nobody else can reach
it; nothing is on the internet.

**Port** — a numbered door a program listens at. *In the lab:* usually 8001;
`start.py` can use 8002 or 8003 if needed. Open the address it prints.
`uv run stop.py` stops the app that `start.py` started.

**Function** — a named piece of code you can run, sometimes with values passed
in. *In the lab:* `advance(rate)` adds one quarter to the history.

**Import** — a line at the top of a file bringing in code from elsewhere.
Getting one wrong is the commonest reason a small program refuses to start,
which is why the specs write them out exactly.

**Repository** — a folder whose whole history is tracked, so any change can be
seen and undone.

**Commit** — a saved point in that history, with a note on what changed.

**Route** — a web address your application answers. `GET /economy` means: when a
browser asks for `/economy`, run this code.

**Template** — a Hypertext Markup Language (HTML) page with gaps, filled with
real values before being sent to the browser. *In the lab:* Jinja2, in
`templates/`.

**Dataclass** — a small Python structure holding named values. *In the lab:*
`Quarter`, holding eleven fields, including policy rate, core, food, fuel and energy
inflation, unemployment, gap, stress, migration and population. Inflation
inflation is computed from the four price components.

**Dependency** — an external library your code needs. *In the lab:* declared in
`pyproject.toml`, so `uv run` fetches them. No install step.


## The economy's new terms

**Policy rate**: the interest rate set by the central bank. This game's neutral
policy rate is 2%.

**Inflation**: the price rise across the whole basket, combining 70%
core, 20% food, 4% fuel and 6% energy. The target is 2%.

**Core inflation**: price rises outside food, fuel and energy. In the game it
responds to demand and earlier fuel and energy pressure.

**Financial stress**: disruption from an abrupt policy-rate move. A move above
0.50 points reduces the following quarter's output gap; smaller moves still
carry a cost in the score.

**Migration**: people arriving or leaving as hardship changes. Population
includes these movements and is shown but not scored.

**Interest-rate smoothing**: moving gradually toward a formula's recommended
policy rate. The game's Taylor rule rounds moves to 0.25 points and moves at
most 0.50 per quarter.

See [economics.md](economics.md) for worked figures and the exact distinctions.
