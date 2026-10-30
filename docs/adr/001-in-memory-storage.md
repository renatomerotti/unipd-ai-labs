# Architecture Decision Record (ADR) 001 — Keep everything in memory

**Status:** Accepted · 2026-09-10

## Context

The Central Bank Game needs to store a history of quarters that grows as the player makes
decisions. The obvious options are a database, a file on disk, or a list in
memory.

Students build this during the lab, on free-tier models with a daily
request limit, having installed nothing beforehand.

## Decision

The history is a module-level Python list. Nothing is persisted. Restarting the
application resets the game.

## Consequences

**Good.** No database to install, no schema, no migrations, no file paths to get
wrong, no object-relational mapper (ORM) for a weak model to misuse. The entire
data layer is one list and one dataclass, which a student can read at a glance.

**Bad.** Closing the terminal loses the run. For a game played in one sitting,
this is acceptable — and "previous terms" in the polished build shows
how persistence *would* be added without requiring it.

**Also.** Because the list is shared between tests, the test suite needs an
explicit reset fixture. That cost is real and is paid in Phase 3.
