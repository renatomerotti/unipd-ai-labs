"""Phase 3 — ready-made: do not change this file."""
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

from models import headline


def test_valid_rate_redirects():
    page = client.post("/decide", data={"rate": 2.5}, follow_redirects=False)
    assert page.status_code == 303
    assert headline(history[-1]) == 3.57 and history[-1].core == 3.48
    assert "Your economy · 2026-Q1" in client.get("/economy").text


def test_valid_rate_adds_one_quarter():
    client.post("/decide", data={"rate": 12})
    assert len(history) == 11
    assert headline(history[-1]) == 3.57
    page = client.get("/economy").text
    assert "💥 You moved 10.00 points in one quarter. Markets will feel it next quarter." in page
    page = client.post("/decide", data={"rate": 3}).text
    assert history[-1].stress == 4.75
    assert "💥 Financial stress" in page and "4.75" in page
    assert "💥 2026-Q2" in page


def test_rate_too_high_is_rejected():
    for invalid in [99, -1]:
        page = client.post("/decide", data={"rate": invalid})
        assert page.status_code == 200
        assert "The policy rate must be between 0% and 20%." in page.text
        assert "10,000,000" in page.text and "4.29" in page.text


def test_rate_too_high_does_not_change_history():
    original = list(history)
    client.post("/decide", data={"rate": 99})
    assert history == original
    assert headline(history[-1]) == 4.29
    for boundary in [0, 20]:
        client.post("/reset")
        assert client.post("/decide", data={"rate": boundary}, follow_redirects=False).status_code == 303
        assert history[-1].rate == boundary and headline(history[-1]) == 3.57


def test_new_quarter_uses_the_previous_rate():
    client.post("/decide", data={"rate": 2.5})
    assert history[-1].gap == 0.08 and history[-1].core == 3.48
    client.post("/decide", data={"rate": 2.5})
    assert (history[-1].gap, history[-1].core, headline(history[-1]), history[-1].unemployment) == (-0.11, 3.57, 3.51, 4.54)


def test_reset_starts_again_from_the_inherited_economy():
    client.post("/decide", data={"rate": 2.5})
    first = history[-1]
    assert first.population == 9_988_600
    assert client.post("/reset", follow_redirects=False).status_code == 303
    assert history == INITIAL
    client.post("/decide", data={"rate": 2.5})
    assert history[-1] == first
