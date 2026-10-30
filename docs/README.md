# docs — project context

These explain **what** we are building and **why**. They are written for people
and read once.

The instructions the assistant works from are in [`../specs/central-bank-game/`](../specs/central-bank-game/).

| Document | Answers |
|---|---|
| [mission.md](mission.md) | Why does this project exist? |
| [prd.md](prd.md) | What are we building, for whom, and how will we know it worked? |
| [roadmap.md](roadmap.md) | In what order does it get built? |
| [tech-stack.md](tech-stack.md) | What tools and versions, and how do I run it? |
| [architecture.md](architecture.md) | How do the pieces fit together? |
| [non-functional-requirements.md](non-functional-requirements.md) | What must be true beyond the features? |
| [adr/](adr/) | Which decisions were made, and why? |

And for reading alongside the lab:

| Document | |
|---|---|
| [privacy.md](privacy.md) | Security: the four rules, all in one place — read before you make an account |
| [troubleshooting.md](troubleshooting.md) | Questions to ask yourself when something is wrong |
| [methodology.md](methodology.md) | How we work, and why it is done this way |
| [glossary.md](glossary.md) | Terms about the assistant and the tools |
| [economics.md](economics.md) | Terms about the model you are running |
| [improve.md](improve.md) | How to take it further once the phases are done |

## Why the split

A **mission** says why the project exists. A **Product Requirements Document
(PRD)** says what it must do from the user's side. A **spec** says exactly how
it behaves. **Tasks** say what to do next.

Keeping them apart means each answers one question, and a change to one does not
force edits to the other three. When the same fact lives in two documents, the
two eventually disagree.
