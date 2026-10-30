"""Phase 2 — ready-made: do not change this file."""
from starlette.testclient import TestClient
from app import app
client = TestClient(app)

import pytest
from models import history, INITIAL

@pytest.fixture(autouse=True)
def fresh_history():
    history[:] = list(INITIAL)
    import models
    models.rng.seed(42)
    yield
    history[:] = list(INITIAL)
    models.rng.seed(42)

from jinja2 import StrictUndefined
from app import templates
from models import headline


def test_economy_page_loads():
    old = templates.env.undefined
    templates.env.undefined = StrictUndefined
    try:
        page = client.get("/economy")
    finally:
        templates.env.undefined = old
    assert page.status_code == 200
    assert "The economy you inherited · 2025-Q4" in page.text
    columns = ["Quarter", "Policy rate %", "📊 Inflation %", "🧺 Core inflation %", "🍞 Food %", "⛽ Fuel %", "💡 Energy %", "👷 Unemployment %", "Output gap %"]
    header = page.text.split("<thead>", 1)[1].split("</thead>", 1)[0]
    assert header.count("<th>") == 9
    assert [header.index(c) for c in columns] == sorted(header.index(c) for c in columns)
    assert page.text.index('aria-label="Economy summary"') < page.text.index('aria-label="Prices this quarter"')
    assert {"history", "headline", "current", "previous", "current_headline", "previous_headline", "term_start_population"} <= page.context.keys()
    for text in ["4.29", "3.10", "10,000,000", "25,800", "🍞", "⛽", "💡", "🧺", "👥"]:
        assert text in page.text


def test_economy_shows_first_quarter():
    page = client.get("/economy").text
    assert "2023-Q3" in page and "2.00" in page and "2025-Q4" in page
    assert headline(history[0]) == 2.00


def test_economy_shows_inherited_inflation():
    page = client.get("/economy").text
    assert "4.29" in page and "4.22" in page
    assert headline(history[-1]) == 4.29
    assert history[-1].population == 10_000_000


def test_history_starts_with_ten_quarters():
    assert len(history) == 10
    assert [(q.label, q.rate, q.core, q.food, q.fuel, q.energy, q.gap, q.unemployment, q.stress, q.migration, q.population) for q in history] == [('2023-Q3', 2.0, 2.0, 2.0, 2.0, 2.0, 0.0, 4.5, 0.0, 20000, 10049600), ('2023-Q4', 2.0, 2.0, 2.2, 1.5, 2.1, 0.1, 4.46, 0.0, 19400, 10069000), ('2024-Q1', 2.0, 2.1, 2.4, 3.0, 2.5, 0.2, 4.42, 0.0, 15600, 10084600), ('2024-Q2', 2.0, 2.2, 2.6, 4.0, 3.0, 0.3, 4.38, 0.0, 12000, 10096600), ('2024-Q3', 2.0, 2.3, 3.0, 6.0, 4.0, 0.4, 4.34, 0.0, 6200, 10102800), ('2024-Q4', 2.0, 2.4, 4.0, 10.0, 7.0, 0.5, 4.3, 0.0, -6000, 10096800), ('2025-Q1', 2.0, 2.5, 5.0, 14.0, 10.0, 0.5, 4.3, 0.0, -18200, 10078600), ('2025-Q2', 2.0, 2.7, 6.0, 12.0, 12.0, 0.6, 4.26, 0.0, -25800, 10052800), ('2025-Q3', 2.0, 2.9, 6.5, 9.0, 11.0, 0.6, 4.26, 0.0, -27000, 10025800), ('2025-Q4', 2.0, 3.1, 6.0, 8.0, 10.0, 0.7, 4.22, 0.0, -25800, 10000000)]
