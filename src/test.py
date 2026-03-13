from fastapi.testclient import TestClient

from api import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data.get("message") == "Hello from FastAPI!"


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data.get("status") == "ok"

