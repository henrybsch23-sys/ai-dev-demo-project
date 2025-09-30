from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_bmi_endpoint():
    resp = client.get("/bmi", params={"weight_kg": 70, "height_m": 1.75})
    assert resp.status_code == 200
    assert resp.json()["bmi"] == 22.86


def test_tdee_ok_sedentary():
    r = client.get("/tdee", params={"bmr_val": 1600, "activity": "sedentary"})
    assert r.status_code == 200
    assert "tdee" in r.json()


def test_tdee_rejects_unknown_activity():
    r = client.get("/tdee", params={"bmr_val": 1600, "activity": "super-saiyan"})
    assert r.status_code == 400