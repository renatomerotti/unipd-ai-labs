"""Phase 5 — ready-made: do not change this file."""
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

from models import loss, rule_run, rng, TERM
from jinja2 import StrictUndefined
from app import templates


def test_taylors_numbers_are_the_default():
    assert rule_run(TERM) == rule_run(TERM, 1.5, 0.5)
    assert loss(rule_run(TERM)) == 1.048


def test_my_rule_is_read_from_the_page():
    old = templates.env.undefined
    templates.env.undefined = StrictUndefined
    try: page = client.get("/rules?a=1.5&b=0.5")
    finally: templates.env.undefined = old
    assert {"a","b","taylor_term","taylor_term_score","my_term","my_term_score"} <= page.context.keys()
    assert page.context["my_term_score"] == 1.048
    assert "1.048" in page.text and "4.91" in page.text
    assert "Your term:" not in page.text and 'class="sb-score"' not in page.text
    assert 'action="/rules#my-rule"' in page.text
    economy = client.get("/economy")
    assert "🧪 Ready for the board's question?" in economy.text
    assert '>Open the Rule lab.</a>' in economy.text
    assert 'href="/rules"' in economy.text and 'id="my-rule"' not in economy.text
    assert not {"a", "b", "my_term", "taylor_term"} & economy.context.keys()
    error = client.post("/decide", data={"rate": -1})
    assert error.status_code == 200 and "The policy rate must be between" in error.text
    assert "rule_history" in error.context and 'id="my-rule"' not in error.text
    for a,b,expected in [(3.0,0.5,(3.0,0.5)),(-10,99,(0.0,5.0))]:
        other = client.get(f"/rules?a={a}&b={b}")
        assert (other.context["a"],other.context["b"]) == expected
        assert other.context["my_term"] == rule_run(TERM,*expected)


def test_trying_a_rule_leaves_my_game_alone():
    client.post("/decide",data={"rate":2.5})
    played,shocks = list(history),rng.getstate()
    before = client.get("/economy").context
    import models
    saved = list(getattr(models, "previous_terms", []))
    page = client.get("/rules?a=3.0&b=0.0")
    assert history == played and rng.getstate() == shocks
    after = client.get("/economy").context
    assert (before["player_score"], before["rule_score"]) == (after["player_score"], after["rule_score"])
    assert list(getattr(models, "previous_terms", [])) == saved
    assert "Twenty quarters under each rule" in page.text and "1.048" in page.text
