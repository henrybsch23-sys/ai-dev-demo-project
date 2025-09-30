from src.services.calculations import bmi, daily_water_intake_l


def simple_recommendations(weight_kg: float, height_m: float, activity_hours: float = 0.0) -> list[str]:
    tips: list[str] = []
    bmi_val = bmi(weight_kg, height_m)

    if bmi_val < 18.5:
        tips.append("BMI under 18.5: consider increasing calorie intake with nutrient-dense foods.")
    elif bmi_val < 25:
        tips.append("BMI in normal range: maintain current habits and regular activity.")
    elif bmi_val < 30:
        tips.append("BMI 25–30: moderate weight management strategies may help.")
    else:
        tips.append("BMI ≥ 30: consult a professional for a personalized plan.")

    water = daily_water_intake_l(weight_kg, activity_hours)
    tips.append(f"Suggested daily water intake: ~{water} L")

    return tips
