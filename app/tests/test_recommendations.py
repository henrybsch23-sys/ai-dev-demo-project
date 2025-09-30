from app.services.recommendations import simple_recommendations

def test_recommendations_underweight_and_water():
    tips = simple_recommendations(50, 1.80, 1.0)
    # BMI = 15.43
    assert any("BMI under 18.5" in t for t in tips)
    assert any("Suggested daily water intake" in t for t in tips)

def test_recommendations_normal_bmi():
    tips = simple_recommendations(70, 1.80, 0.0)
    # BMI = 21.6
    assert any("BMI in normal range" in t for t in tips)

def test_recommendations_overweight_bmi():
    tips = simple_recommendations(85, 1.75, 0.0)
    # BMI = 27.8
    assert any("BMI 25–30" in t for t in tips)

def test_recommendations_obese_bmi():
    tips = simple_recommendations(120, 1.70, 0.0)
    # BMI = 41.5
    assert any("BMI ≥ 30" in t for t in tips)
