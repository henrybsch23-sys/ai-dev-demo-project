from fastapi import FastAPI, HTTPException, Query
from src.services.calculations import (
    bmi,
    bmr_mifflin_st_jeor,
    tdee,
    body_fat_navy,
    daily_water_intake_l,
)
from src.services.recommendations import simple_recommendations

app = FastAPI(title="AI-Dev Demo API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/bmi")
def get_bmi(weight_kg: float = Query(..., gt=0), height_m: float = Query(..., gt=0)):
    return {"bmi": bmi(weight_kg, height_m)}


@app.get("/bmr")
def get_bmr(
    sex: str,
    weight_kg: float = Query(..., gt=0),
    height_cm: float = Query(..., gt=0),
    age: int = Query(..., gt=0),
):
    try:
        return {"bmr": bmr_mifflin_st_jeor(sex.lower(), weight_kg, height_cm, age)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/tdee")
def get_tdee(bmr_val: float = Query(..., gt=0), activity: str = "sedentary"):
    return {"tdee": tdee(bmr_val, activity)}


@app.get("/bodyfat")
def get_bodyfat(
    sex: str,
    height_cm: float,
    neck_cm: float,
    waist_cm: float,
    hip_cm: float | None = None,
):
    try:
        return {
            "body_fat_pct": body_fat_navy(
                sex.lower(), height_cm, neck_cm, waist_cm, hip_cm
            )
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/water")
def get_water(
    weight_kg: float = Query(..., gt=0), activity_hours: float = Query(0.0, ge=0.0)
):
    return {"liters": daily_water_intake_l(weight_kg, activity_hours)}


@app.get("/recommendations")
def get_recommendations(
    weight_kg: float = Query(..., gt=0),
    height_m: float = Query(..., gt=0),
    activity_hours: float = Query(0.0, ge=0.0),
):
    return {"tips": simple_recommendations(weight_kg, height_m, activity_hours)}
