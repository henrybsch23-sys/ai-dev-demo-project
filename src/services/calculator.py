from __future__ import annotations

def bmi(weight_kg: float, height_m: float) -> float:
    if height_m <= 0:
        raise ValueError("height_m must be > 0")
    return round(weight_kg / (height_m ** 2), 2)

def bmr_mifflin_st_jeor(sex: str, weight_kg: float, height_cm: float, age: int) -> float:
    """Basal Metabolic Rate (Mifflin–St Jeor).
    sex: "male" | "female"
    """
    if sex not in {"male", "female"}:
        raise ValueError("sex must be 'male' or 'female'")
    if any(v <= 0 for v in [weight_kg, height_cm]) or age <= 0:
        raise ValueError("inputs must be positive")

    if sex == "male":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    return round(bmr, 1)

_ACTIVITY_FACTORS = {
    "sedentary": 1.2,
    "light": 1.375,
    "moderate": 1.55,
    "active": 1.725,
    "very_active": 1.9,
}

def tdee(bmr: float, activity: str = "sedentary") -> float:
    """Total Daily Energy Expenditure."""
    if activity not in _ACTIVITY_FACTORS:
        raise ValueError(f"unknown activity '{activity}'")
    return round(bmr * _ACTIVITY_FACTORS[activity], 1)

def body_fat_navy(sex: str, height_cm: float, neck_cm: float, waist_cm: float, hip_cm: float | None = None) -> float:
    """US Navy method (rough estimate)."""
    import math
    if sex not in {"male", "female"}:
        raise ValueError("sex must be 'male' or 'female'")
    if any(v <= 0 for v in [height_cm, neck_cm, waist_cm]) or (sex == "female" and (hip_cm is None or hip_cm <= 0)):
        raise ValueError("all measures must be positive (hip required for females)")

    if sex == "male":
        bf = 495 / (1.0324 - 0.19077 * math.log10(waist_cm - neck_cm) + 0.15456 * math.log10(height_cm)) - 450
    else:
        bf = 495 / (1.29579 - 0.35004 * math.log10(waist_cm + hip_cm - neck_cm) + 0.22100 * math.log10(height_cm)) - 450
    return round(bf, 2)

def daily_water_intake_l(weight_kg: float, activity_hours: float = 0.0) -> float:
    """Rule of thumb: 35 ml/kg + 350 ml per hour of activity."""
    if weight_kg <= 0 or activity_hours < 0:
        raise ValueError("invalid inputs")
    ml = 35 * weight_kg + 350 * activity_hours
    return round(ml / 1000.0, 2)
