# AGENTS.md — UniPD AI Labs

> Canonical project context. `CLAUDE.md` is a thin import of this file.

## What this is

Course material for the AI lab of the Master's in Applied Economics, University
of Padua, 2026.

Students build the **Central Bank Game**, a monetary policy simulator, by directing an AI
coding agent from written specifications. Three one-hour sessions across two
days, using free-tier models.

## Where to start

| You are | Read |
| --- | --- |
| A student, before the first session | `README.md`, then `SETUP.md` |
| A student, during a session | `prompts/` — one numbered file per step, in order |
| An agent asked to build the app | `docs/mission.md`, `docs/tech-stack.md`, `specs/central-bank-game/tasks.md`, `specs/central-bank-game/data-model.md` |

Students do **not** work inside this repository. Create a separate project
folder and copy from `starter/`. Nothing a student writes belongs here.

## Structure

```
README.md        What this is, where to start
SETUP.md         VS Code, OpenCode, OpenRouter, uv, first prompt
docs/            Project context — mission, PRD, roadmap, tech stack,
                 architecture, non-functional requirements, ADRs,
                 plus privacy, methodology, glossary, economics,
                 troubleshooting and improve
specs/central-bank-game/  The feature — spec, plan, data model, tasks,
                 validation, clarifications
prompts/         One numbered prompt per step, each gating the next
starter/         Ready-made files to copy: pyproject.toml, a gitignore
                 template, opencode.json, templates/ (layout, legend, chart
                 and scoreboard), tests/ (Phase 1), and phase-2/ to phase-4/
                 (one test file each)
data/            initial_economy.csv — reference only, not loaded
checkpoints/     Phase recovery states
```

Source of truth, when documents disagree: `specs/central-bank-game/data-model.md`, then
`spec.md`, then `tasks.md`. Everything else explains and is never authoritative.
Report contradictions rather than choosing a side.

## Repository rules

This repository is intended to become public. History is permanent once
published: deleting a file adds a commit, it does not remove the earlier ones.

| Rule | Enforced by |
| --- | --- |
| Never commit `.claude/` or `.agents/` | `.gitignore`, plus a `pre-commit` and a `pre-push` hook |
| Never commit a secret — `.env`, `*.key`, `*.pem` | Same |
| Never commit an absolute filesystem path in a tracked file | Review. Pasted terminal output leaks usernames and directory structure. |
| Commits need the maintainer's explicit go-ahead | Convention |

Instructor material — lab design, solutions, the reference build — is kept in a
separate private repository and is deliberately absent here. Nothing in this
repository is confidential; the guards above exist to keep secrets and local
tooling config out, not to hide course content.

Hooks are versioned in `.githooks/` rather than `.git/hooks/`, so they travel
with a clone. Git will not enable them automatically — that would mean cloning
any repository executes its author's code — so run this once after cloning:

```bash
git config core.hooksPath .githooks
```

Verify at any time:

```bash
git ls-files | sort                      # exactly what would be published
git status --short                       # nothing private staged
```

## Writing rules

* **English, correct and plain.** Student-facing material is graded work.
  Grammar errors are defects.
* **Specifications are written for a weak model:** exact filenames, exact
  routes, exact identifiers, exact import lines. Ambiguity is a defect, not a
  style choice.
* **One prompt per file** under `prompts/`, numbered, each ending in a
  verification step that must pass before the next file is opened.
* **`[REPO_URL]`** is the placeholder for this repository's address until it is
  decided. Keep it greppable.
* **No secrets in any example or screenshot** — placeholders only.

* **`docs/troubleshooting.md` holds questions, not answers.** Each entry asks a
  student to check something and carries a stable code (`S1`, `F2`, `T3`) so an
  instructor can name it. Fixes and explanations stay in the document that owns
  them; a question points at a check and so never goes stale.

* **Never add anything to this repository that asks a student for personal
  data.** The lab runs on invented figures and needs none. Any new material
  that touches accounts, keys or files leaving the machine must agree with
  [`docs/privacy.md`](docs/privacy.md), which is the source of truth for it.

## Working agreements

* Verify before claiming done: run the command, quote the output.
* Surgical edits: touch only what the task requires; match the existing style.
* No installs, no deletions and no commits without explicit approval.
