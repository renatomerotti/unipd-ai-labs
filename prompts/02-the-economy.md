# Step 2 — Phase 2: the economy you inherited

**You will finish with:** a table of the ten quarters before you took
over.

---

## Read this first

Open `specs/central-bank-game/data-model.md` and read the section **The inherited history**. You
are taking over an economy where inflation has drifted from 2.00% to 4.29%.

---

## The prompt

```text
Implement Phase 2 from specs/central-bank-game/tasks.md exactly as written, and nothing beyond it.

Do these in order:
1. Move only later-tests/test_phase_2.py into tests/. Do not change any test.
2. Create models.py with the exact eleven-field Quarter dataclass, all ten
   inherited quarters and headline(quarter). Inflation is computed, not stored.
3. Add GET /economy and economy_context. Pass history, headline, current,
   previous, current_headline, previous_headline, term_start_population and
   error, exactly as tasks.md defines them.
4. Create templates/economy.html: nine-column record, _summary.html, _prices.html,
   _people.html and _legend.html in the specified order. These templates
   already exist; do not change them. Add no form or chart yet.

The application is already running and reloads by itself. Never start, stop or
restart it, never run pkill or kill, and never send requests to it — I will
check it in the browser.

Then run: uv run pytest -q
If anything fails, fix it and run it again until all tests pass.
When all tests pass, stop. Reply with the test line and one sentence. Do not
run anything else, and do not create any other file.
```

---

## What should happen

`models.py` appears with ten quarters in it, and `/economy` shows them as a
table.

---

## Check before continuing

1. In the assistant's tab, its test run says `7 passed`.
2. In your browser, click **See the economy you inherited**: ten rows, the last
   showing inflation 4.29.

Check one row yourself. For `2025-Q4`, the gap is 0.70, so unemployment is
`4.5 − 0.4 × 0.70 = 4.22`. Anything wrong: `docs/troubleshooting.md`.

- [ ] `7 passed`
- [ ] Ten rows, the last showing inflation 4.29

Do not open `03-set-a-policy-rate.md` until both are true.
