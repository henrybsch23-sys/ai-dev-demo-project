from app.services.recommendations import simple_recommendations

def test_recommendations_contains_water_tip():
    tips = simple_recommendations(70, 1.75, 1)
    assert any("water" in t.lower() for t in tips)
