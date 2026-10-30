"""Phase 4 — ready-made: do not change this file."""
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
from models import advance, headline, loss, rule_run, reset, TERM, rng


def test_loss_and_moves_match_the_reference_strategies():
    for rates, score, final, population in [([2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0], 1.492, 2.72, 9978400), ([2.5, 3, 3.5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 2.33, -0.95, 9769400), ([12, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 8.215, -2.11, 9114200)]:
        reset()
        for rate in rates: advance(rate)
        assert (loss(history),headline(history[-1]),history[-1].population) == (score,final,population)


def test_rule_run_returns_requested_length():
    run = rule_run(TERM)
    assert len(run) == 30
    assert (loss(run),headline(run[-1]),max(q.unemployment for q in run[10:]),run[-1].population) == (1.048,1.78,4.91,10_177_000)
    assert [q.rate for q in run[10:]] == [2.5, 3.0, 3.5, 3.25, 2.75, 2.5, 2.75, 2.25, 2.5, 2.75, 3.0, 2.5, 2.0, 1.5, 2.0, 2.0, 2.25, 2.25, 1.75, 1.75]


def test_rule_run_does_not_change_history():
    original, shocks = list(history), rng.getstate()
    assert loss(rule_run(TERM)) == 1.048
    assert history == original and rng.getstate() == shocks


def test_scoreboard_and_chart_context_is_complete():
    from html.parser import HTMLParser

    class Choices(HTMLParser):
        def __init__(self):
            super().__init__()
            self.rows, self.row, self.cell = [], None, None
        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if tag == "tr" and "data-policy-quarter" in attrs:
                self.row = []
            elif tag == "td" and self.row is not None:
                self.cell = ""
        def handle_data(self, value):
            if self.cell is not None:
                self.cell += value
        def handle_endtag(self, tag):
            if tag == "td" and self.cell is not None:
                self.row.append(self.cell.strip())
                self.cell = None
            elif tag == "tr" and self.row is not None:
                self.rows.append(self.row)
                self.row = None

    old = templates.env.undefined
    templates.env.undefined = StrictUndefined
    try:
        page = client.get("/economy")
        assert {"history","headline","rule_history","player_score","rule_score","term","labels","player_inflation","rule_inflation","player_core"} <= page.context.keys()
        assert page.context["player_inflation"][-1] == 4.29
        for text in ["Score breakdown", "moves", "👥", "2.220", "inflationChart", "Your core inflation"]:
            assert text in page.text
        for rates, lagging, component in [
            ([], "Neither", ""),
            ([2.0], "Taylor", "policy-rate moves"),
            ([12.0], "You", "policy-rate moves"),
            ([2.5] * 6 + [2.0, 2.0, 2.0, 3.0], "You", "inflation misses"),
        ]:
            reset()
            for rate in rates:
                advance(rate)
            played, shocks = list(history), rng.getstate()
            page = client.get("/economy")
            benchmark = rule_run(len(rates))
            parser = Choices()
            parser.feed(page.text)
            assert parser.rows == [[q.label, f"{q.rate:.2f}", f"{r.rate:.2f}"]
                                   for q, r in zip(history[10:], benchmark[10:])]
            assert history == played and rng.getstate() == shocks
            assert f'data-lagging="{lagging}"' in page.text
            assert f'data-component="{component}"' in page.text
            if not rates:
                assert "No policy decisions yet" in page.text
            assert page.text.index('<form method="post"') < page.text.index('id="inflationChart"')
            assert page.text.index('id="inflationChart"') < page.text.index('id="policy-comparison"')
            if len(rates) == 10:
                assert (page.context["player_score"], page.context["rule_score"]) == (1.673, 1.536)
                assert "0.137" in page.text
    finally:
        templates.env.undefined = old


def test_the_term_ends_after_twenty_quarters():
    assert TERM == 20
    for _ in range(TERM): client.post("/decide",data={"rate":2.0})
    assert loss(history) == 1.492
    played = list(history)
    page = client.post("/decide",data={"rate":2.0})
    assert "Your term is over" in page.text and history == played
