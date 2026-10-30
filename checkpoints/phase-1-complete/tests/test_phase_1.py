"""Phase 1 — ready-made: do not change this file."""
from starlette.testclient import TestClient
from app import app
client = TestClient(app)


def test_home_page_loads():
    page = client.get("/")
    assert page.status_code == 200
    assert "You are the central bank of a country." in page.text


def test_home_states_the_target():
    page = client.get("/").text
    for text in ["2%", "2.00%", "3.10%", "4.22%", "food and energy surge"]:
        assert text in page


def test_home_states_current_inflation():
    page = client.get("/").text
    for text in ["4.29%", "10,000,000", "25,800", "🧳"]:
        assert text in page
