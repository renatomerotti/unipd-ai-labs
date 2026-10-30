# Non-functional requirements

What must be true beyond the features. These constrain every phase, and several
of them outrank the features when the two conflict.

## Constraints that come from the room

| | Requirement | Why |
|---|---|---|
| N1 | The whole build must fit inside a free-tier daily request allowance | Students cannot be asked to pay. Exceeding it ends their session with no recovery |
| N2 | Setup must need no administrator rights | Some students are on managed university machines |
| N3 | Nothing may require prior Python knowledge | It is nominally expected and cannot be assumed |
| N4 | Every check must be readable by a non-programmer | `7 passed` is a check. "Does this look right?" is not |
| N5 | No step may depend on homework being done | It will not be |

## Constraints that come from the model

| | Requirement | Why |
|---|---|---|
| N6 | Every number must be verifiable by hand | Otherwise a student cannot distinguish correct from plausible |
| N7 | Randomness must be seeded | Tests must be repeatable, and no player may blame their shocks |
| N8 | Specifications must be unambiguous to a weak model | A free model does what you wrote, not what you meant |

## Constraints on the application

| | Requirement |
|---|---|
| N9 | Runs locally with two commands and no install step |
| N10 | Every figure is generated, not fetched. The only network requests at runtime are the page loading Bootstrap and Chart.js from the jsDelivr content delivery network (CDN) |
| N11 | Usable down to 380px wide, with visible keyboard focus |
| N12 | None of the student's data leaves the machine: the CDN receives ordinary requests for two public files, never a policy rate or a score |

## The one that is easy to lose

**N8 outranks elegance.** A shorter, more graceful specification that leaves a
choice open is worse than a blunt one that does not. Four pilot rounds against a
different model exist to enforce this — see
[`../specs/central-bank-game/clarifications.md`](../specs/central-bank-game/clarifications.md).
