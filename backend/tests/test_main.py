from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert data["data"]["status"] == "ok"
    assert data["message"] == "Service is healthy"


