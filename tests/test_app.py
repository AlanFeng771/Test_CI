import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "加法計算器".encode("utf-8") in response.data


def test_add_success(client):
    response = client.get("/api/add?a=2&b=3")
    assert response.status_code == 200
    assert response.get_json() == {"result": 5.0}


def test_add_with_negative_numbers(client):
    response = client.get("/api/add?a=-1&b=-1")
    assert response.status_code == 200
    assert response.get_json() == {"result": -2.0}


def test_add_invalid_input(client):
    response = client.get("/api/add?a=foo&b=3")
    assert response.status_code == 400
    assert "error" in response.get_json()
