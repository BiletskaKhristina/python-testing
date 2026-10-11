import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


@pytest.mark.integration
def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Application is working"


@pytest.mark.integration
def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]["name"] == "Anna"


@pytest.mark.integration
def test_not_found(client):
    response = client.get("/unknown")
    assert response.status_code == 404