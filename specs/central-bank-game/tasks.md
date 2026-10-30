# Tasks

Five phases. Each ends with a page you can see and a check you run yourself.
Do not skip a phase. Read `specs/central-bank-game/data-model.md` before Phase 2.

The layout, price cards, people panel, legend, scoreboard, chart, own-rule form,
not-built page and tests are ready-made. **Never change them.**
The files are `templates/base.html`, `_summary.html`, `_prices.html`, `_people.html`, `_legend.html`,
`_scoreboard.html`, `_chart.html`, `_my_rule.html`, `not_built.html` in that folder,
and one test file per phase. Keep `pyproject.toml`, `start.py`, `stop.py` and
`opencode.json` unchanged. Add no script header to `app.py`.

---

## Phase 1 — The application runs

### Files to create

`app.py` and `templates/home.html`. The ready-made Phase 1 test is already in `tests/`.

### app.py

1. Import `FastAPI`, `Request`, `HTMLResponse` and `Jinja2Templates` from the usual
   FastAPI modules. Create `app = FastAPI()` and
   `templates = Jinja2Templates(directory="templates")`.
2. Add a plain `def home(request: Request)` route for `GET /`, with
   `response_class=HTMLResponse`; return
   `templates.TemplateResponse(request, "home.html", {})`.
3. Add the plain `def not_built(request: Request, exc)` 404 handler returning
   `templates.TemplateResponse(request, "not_built.html", {}, status_code=404)`.
4. Under `if __name__ == "__main__":`, import uvicorn and call
   `uvicorn.run("app:app", host="127.0.0.1", port=8001, reload=True)`.
   Do not start it while building.

### templates/home.html

Extend `base.html`, put everything in its content block, and show:

- `You are the central bank of a country.`
- A food and energy surge lifted inflation to **4.29%**, against the **2%** target;
  core is **3.10%**. Keep the words `food and energy surge` together.
- `Before you, the policy rate was held at 2.00% for ten quarters.`
- 👷 Unemployment **4.22%**; 👥 population **10,000,000**;
  🧳 **25,800** people left last quarter.
- The policy rate is the interest rate the central bank sets; it affects the next
  quarter after the one where it is recorded.
- A link to `/economy`, labelled `See the economy you inherited`.

Use Bootstrap cards or short paragraphs; no explanatory toggles.
No ready-made template in this phase needs an application context variable.

### Check before continuing

`uv run pytest -q` → **3 passed**. At the end of the phase prompt, run
`uv run start.py` once and give the address it prints. The student opens it.

---

## Phase 2 — The economy you inherited

### Files to create or change

`models.py`, `app.py`, `templates/economy.html`. First move only
`later-tests/test_phase_2.py` into `tests/`; never change a test.

### models.py

Copy this code literally. The dataclass fields and every inherited value matter.
Inflation is a function, not a stored field. No external file is loaded.

```python
from dataclasses import dataclass
import random

TARGET = 2.0
NEUTRAL_RATE = 2.0
NATURAL_UNEMP = 4.5
SEED = 42
WEIGHTS = {"core": 0.70, "food": 0.20, "fuel": 0.04, "energy": 0.06}
PERSIST = {"food": 0.6, "fuel": 0.4, "energy": 0.6}
SHOCK_RANGE = {"demand": 0.3, "food": 1.0, "fuel": 4.0, "energy": 2.0}
SHOCK_ORDER = ("demand", "food", "fuel", "energy")
STRESS_FREE = 0.5
STRESS_K = 0.5
POPULATION_START = 10_029_600
MIGRATION_PER_POINT = 20_000
MISERY_NEUTRAL = 1.0
rng = random.Random(SEED)


@dataclass
class Quarter:
    label: str
    rate: float
    core: float
    food: float
    fuel: float
    energy: float
    gap: float
    unemployment: float
    stress: float
    migration: int
    population: int


def headline(quarter: Quarter) -> float:
    return round(sum(weight * getattr(quarter, name) for name, weight in WEIGHTS.items()), 2)


history: list[Quarter] = [
    Quarter('2023-Q3', 2.0, 2.0, 2.0, 2.0, 2.0, 0.0, 4.5, 0.0, 20000, 10049600),
    Quarter('2023-Q4', 2.0, 2.0, 2.2, 1.5, 2.1, 0.1, 4.46, 0.0, 19400, 10069000),
    Quarter('2024-Q1', 2.0, 2.1, 2.4, 3.0, 2.5, 0.2, 4.42, 0.0, 15600, 10084600),
    Quarter('2024-Q2', 2.0, 2.2, 2.6, 4.0, 3.0, 0.3, 4.38, 0.0, 12000, 10096600),
    Quarter('2024-Q3', 2.0, 2.3, 3.0, 6.0, 4.0, 0.4, 4.34, 0.0, 6200, 10102800),
    Quarter('2024-Q4', 2.0, 2.4, 4.0, 10.0, 7.0, 0.5, 4.3, 0.0, -6000, 10096800),
    Quarter('2025-Q1', 2.0, 2.5, 5.0, 14.0, 10.0, 0.5, 4.3, 0.0, -18200, 10078600),
    Quarter('2025-Q2', 2.0, 2.7, 6.0, 12.0, 12.0, 0.6, 4.26, 0.0, -25800, 10052800),
    Quarter('2025-Q3', 2.0, 2.9, 6.5, 9.0, 11.0, 0.6, 4.26, 0.0, -27000, 10025800),
    Quarter('2025-Q4', 2.0, 3.1, 6.0, 8.0, 10.0, 0.7, 4.22, 0.0, -25800, 10000000),
]
INITIAL = list(history)

```

### app.py and the template contract

Import `INITIAL`, `history` and `headline` from `models`. Add `GET /economy` as a
plain `def economy(request: Request)`, returning `economy.html`.
Use a plain helper `economy_context(error=None)` to return the following dictionary.
The names stay unchanged in later phases; `request` is supplied by TemplateResponse.

| Context name | Meaning / consumer |
|---|---|
| `history` | The real list of quarters; record |
| `headline` | The `headline(quarter)` function; record, later scoreboard |
| `current` | `history[-1]`; prices, people, form |
| `previous` | `history[-2]`; price arrows, latest-move warning |
| `current_headline` | `headline(current)`; price heading |
| `previous_headline` | `headline(previous)`; heading arrow |
| `term_start_population` | `INITIAL[-1].population`, 10,000,000; people change |
| `error` | `None` or exact error text; form from Phase 3 |

### templates/economy.html

1. Extend `base.html`; heading `The economy you inherited · 2025-Q4` while `history|length == 10`, then `Your economy · <quarter>` with the latest label after the first decision.
2. Include `_summary.html`, then `_prices.html` and `_people.html`.
3. Show one row per quarter, oldest first, with exactly these nine columns:
   Quarter, Policy rate %, 📊 Inflation %, 🧺 Core inflation %, 🍞 Food %, ⛽ Fuel %, 💡 Energy %, 👷 Unemployment %, Output gap %. Give core, food, fuel and energy their card colours (slate #475569, amber #9a6700, red #b4232a, yellow #856600).
   Compute inflation with the passed `headline` function, show economic values to
   two decimals. Wrap the table in `class="table-responsive"`; let words wrap at
   390 px without widening the page. Give it `aria-label="Policy record table"`.
   Add `economy-record` to the table class, and a `data-label` attribute on each
   cell containing its column heading; the supplied layout makes each row a
   labelled card on narrow screens.
4. Mark a row `table-warning` when `headline(quarter) > 2.50` or `< 1.50`.
5. Include `_legend.html` after the table. No form, chart or scoreboard yet.

`_summary.html` reads only `current`, `previous`, `current_headline`, `previous_headline`; it shows Policy rate, Inflation, Unemployment and Output gap cards, each with a last-quarter arrow.
`_prices.html` reads `current`, `previous`, `current_headline`, `previous_headline`.
`_people.html` reads `current`, `term_start_population`.
`_legend.html` reads no context variables. Preserve their bytes.

### Check before continuing

`uv run pytest -q` → **7 passed**. Ten rows; inflation ends at 4.29%, core at 3.10%,
people show 10,000,000 with 25,800 leaving. The inherited output gap 0.70 gives
`4.5 - 0.4 * 0.70 = 4.22` unemployment.

---

## Phase 3 — Set a policy rate, and meet the lag

### Files to change

`models.py`, `app.py`, `templates/economy.html`. First move only
`later-tests/test_phase_3.py` into `tests/`.

### models.py — next_label, advance_quarter, advance and reset

`advance_quarter` takes a list and a generator so the benchmark can reuse the
same arithmetic later. `advance(rate)` uses the real history and generator.
Add this literal code after `INITIAL`:

```python
def next_label(label: str) -> str:
    year, quarter = label.split("-Q")
    year, quarter = int(year), int(quarter)
    return f"{year + 1}-Q1" if quarter == 4 else f"{year}-Q{quarter + 1}"


def advance_quarter(quarters: list[Quarter], rate: float, generator: random.Random) -> Quarter:
    previous, before = quarters[-1], quarters[-2]
    shocks = {name: generator.uniform(-SHOCK_RANGE[name], SHOCK_RANGE[name]) for name in SHOCK_ORDER}
    move = abs(previous.rate - before.rate)
    stress = round(STRESS_K * max(0.0, move - STRESS_FREE), 2)
    gap = round(-0.5 * (previous.rate - NEUTRAL_RATE) + shocks["demand"] - stress, 2)
    energy_push = 0.4 * (previous.fuel - TARGET) + 0.6 * (previous.energy - TARGET)
    core = round(previous.core + 0.3 * gap + 0.05 * energy_push, 2)
    prices = {name: round(TARGET + PERSIST[name] * (getattr(previous, name) - TARGET) + shocks[name], 2)
              for name in ("food", "fuel", "energy")}
    unemployment = round(NATURAL_UNEMP - 0.4 * gap, 2)
    quarter = Quarter(next_label(previous.label), rate, core, prices["food"], prices["fuel"],
                      prices["energy"], gap, unemployment, stress, 0, 0)
    misery = abs(headline(quarter) - TARGET) + max(0.0, unemployment - NATURAL_UNEMP)
    quarter.migration = int(round(-MIGRATION_PER_POINT * (misery - MISERY_NEUTRAL), -2))
    quarter.population = previous.population + quarter.migration
    quarters.append(quarter)
    return quarter


def advance(rate: float) -> None:
    advance_quarter(history, rate, rng)


def reset() -> None:
    history[:] = list(INITIAL)
    rng.seed(SEED)
```

### app.py

1. Import `Form`, `RedirectResponse`, `advance`, `reset` and `math`.
2. Add `POST /decide`, a plain `def decide(request: Request, rate: float = Form(...))`.
   If the value is outside 0–20 or `not math.isfinite(rate)`, render `economy.html`
   with the full `economy_context("The policy rate must be between 0% and 20%.")`.
   Otherwise call `advance(rate)` and redirect to `/economy` with status 303.
3. Add `POST /reset`, a plain `def start_again()`, that calls `reset()` and redirects
   to `/economy` with 303.

### templates/economy.html and context

Keep every Phase 2 context variable. No new context variable is needed:
`error` displays the error; `current`, `previous` supply the warning and stress.
Directly below the heading (below the scoreboard from Phase 4), before the chart, summary, prices, people and record:

1. Show `Your policy rate appears in the new row; its effect shows in the row after. Watch what happens.`
2. Display `error` in an alert when present.
3. Add a form posting to `/decide`, with one required number input `id="rate"`,
   `name="rate"`, `step="any"`, `min="0"`, `max="20"`, label
   `Policy rate for next quarter (%)`, and button `Set the policy rate`.
   The hint says `Central banks usually move 0.25 or 0.50 a quarter.`
4. When `abs(current.rate - previous.rate) > 0.50`, show the stateless warning
   from `data-model.md`, formatting that absolute move to two decimals.
5. When `current.stress > 0`, show a red badge `💥 Financial stress` and its
   value to two decimals. Do not show a stress badge otherwise.
6. Add a second form posting to `/reset`, with a button
   `Start again from the inherited economy`.

### Check before continuing

`uv run pytest -q` → **13 passed**. The test
`test_new_quarter_uses_the_previous_rate` pins the lag: set 2.50 twice;
inflation is 3.57 then 3.51, while core is 3.48 then 3.57.
A move to 12.00 shows a 10.00-point warning; the following quarter has stress 4.75.
Prefix the quarter label in every record row with `💥 ` when that quarter's stress is positive; the marker stays in the record.
Reset restores both inherited values and the random generator.

---

## Phase 4 — Chart, score, and your opponent

### Files to change

`models.py`, `app.py`, `templates/economy.html`. First move only
`later-tests/test_phase_4.py` into `tests/`.

### models.py — constants, loss, rule_rate and rule_run

Add the following after the Phase 3 functions:

```python
LAMBDA = 0.5
NU = 0.25
TERM = 20


def loss(quarters: list[Quarter]) -> float:
    total = 0.0
    for i, quarter in enumerate(quarters):
        move = quarter.rate - quarters[i - 1].rate if i else 0.0
        total += ((headline(quarter) - TARGET) ** 2
                  + LAMBDA * (quarter.unemployment - NATURAL_UNEMP) ** 2 + NU * move ** 2)
    return round(total / len(quarters), 3)


def rule_rate(quarter: Quarter) -> float:
    target = NEUTRAL_RATE + 1.5 * (headline(quarter) - TARGET) + 0.5 * quarter.gap
    move = max(-0.5, min(0.5, round((target - quarter.rate) * 4) / 4))
    return max(0.0, min(20.0, round(quarter.rate + move, 2)))


def rule_run(n_quarters: int) -> list[Quarter]:
    rule_history = list(INITIAL)
    rule_rng = random.Random(SEED)
    for _ in range(n_quarters):
        advance_quarter(rule_history, rule_rate(rule_history[-1]), rule_rng)
    return rule_history

```

The score includes all inherited rows. The benchmark moves at most 0.50, rounded
to 0.25 steps. It shares no mutable history or generator with the player.

### app.py and the template contract

Keep all Phase 2 context variables, then add these to `economy_context`.
Both `GET /economy` and every `POST /decide` error path call that helper.

| Additional context name | Meaning / consumer |
|---|---|
| `rule_history` | `rule_run(len(history) - len(INITIAL))`; scoreboard |
| `player_score` | `loss(history)`; scoreboard |
| `rule_score` | `loss(rule_history)`; scoreboard |
| `term` | `TERM`, 20; scoreboard and form visibility |
| `labels` | All `quarter.label` in history order; chart |
| `player_inflation` | All `headline(quarter)` for player; chart |
| `rule_inflation` | All `headline(quarter)` for Taylor; chart |
| `player_core` | All player `quarter.core`; chart |

The scoreboard reads `history`, `rule_history`, `player_score`, `rule_score`,
`term`, `headline`. Its ready-made diagnosis names the largest average cost
disadvantage and any offsetting saving, or a tie, without suggesting a policy.
The ready-made `_policy_comparison.html` uses existing context only: played
quarters, your policy rate and Taylor's policy rate, aligned by quarter.
It shows an empty state before the first decision and never future choices. The chart reads `labels`, `player_inflation`, `rule_inflation`,
`player_core`. All four chart arrays align with the complete history, inherited included.

After input validation, refuse a decision when `len(history) - len(INITIAL) >= TERM`.
Render the full economy context with
`Your term is over. Press Start again from the inherited economy to serve another term.`
Add nothing. Otherwise advance as before.

### templates/economy.html

Order: heading → `_scoreboard.html` → policy-rate form and Start again → `_chart.html` → `_policy_comparison.html` → `_summary.html` → `_prices.html` → `_people.html` → table → `_legend.html`. Keep all content visible.
Hide the policy-rate form when `(history | length) - 10 >= term`.
Keep the warning and stress display; never write separate scoreboard or chart code.

### Check

`uv run pytest -q` → **18 passed**. A fresh inherited score is 2.220 on both sides.
The twenty-quarter Taylor score is 1.048, final inflation 1.78%, worst unemployment
4.91%, population 10,177,000. Unlike the old model, different first moves may
already have different scores: the move term is charged immediately.

---

## Phase 5 — Beat the rule

### Files to change

`models.py`, `app.py`, `templates/economy.html`; create `templates/rules.html`. First move only
`later-tests/test_phase_5.py` into `tests/`.

### models.py

Add optional `a=1.5, b=0.5` to both signatures, preserving the Phase 4 defaults:

```python
def rule_rate(quarter: Quarter, a=1.5, b=0.5) -> float:
    target = NEUTRAL_RATE + a * (headline(quarter) - TARGET) + b * quarter.gap
    move = max(-0.5, min(0.5, round((target - quarter.rate) * 4) / 4))
    return max(0.0, min(20.0, round(quarter.rate + move, 2)))


def rule_run(n_quarters: int, a=1.5, b=0.5) -> list[Quarter]:
    rule_history = list(INITIAL)
    rule_rng = random.Random(SEED)
    for _ in range(n_quarters):
        advance_quarter(rule_history, rule_rate(rule_history[-1], a, b), rule_rng)
    return rule_history
```

### app.py and the template contract

Add `GET /rules` with query numbers `a: float = 1.5`, `b: float = 0.5`, each
clamped to 0–5. Its separate rule context has exactly these six values.
Keep every Phase 4 game context variable on Economy and every decision error:

| Context name | Meaning |
|---|---|
| `a` | Clamped inflation-response coefficient |
| `b` | Clamped output-gap coefficient |
| `taylor_term` | `rule_run(TERM)` |
| `taylor_term_score` | `loss(taylor_term)` |
| `my_term` | `rule_run(TERM, a, b)` |
| `my_term_score` | `loss(my_term)` |

`_my_rule.html` reads these six, and no other application context variables.
Game error paths use the unchanged complete Phase 4 economy context.

### templates/economy.html

After `_legend.html`, show only the linked line:
“🧪 Ready for the board's question? Open the Rule lab.” Link it to `/rules`.
Keep all earlier game includes, including `_policy_comparison.html`.

### templates/rules.html

Create this page, extending `base.html`, titled Rule lab, and include the
ready-made `_my_rule.html`. Do not change a ready-made file. The menu is
Home · Economy · Rule lab. It submits A/B to `/rules#my-rule`; comparing rules
never changes the player's history, generator, scores or game.
Earlier phases keep their existing not-built response for this route.

### Check

`uv run pytest -q` → **21 passed**. Taylor's row reads 1.048 and 4.91.
Open Rule lab, change one coefficient, submit, and compare without changing your Economy game.

## The challenges

The five phases end here. Keep all 21 tests passing when making a change of your
own; `docs/improve.md` describes the method.
