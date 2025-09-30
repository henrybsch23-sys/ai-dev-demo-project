from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_bmi_endpoint():
    resp = client.get("/bmi", params={"weight_kg": 70, "height_m": 1.75})
    assert resp.status_code == 200
    assert resp.json()["bmi"] == 22.86
