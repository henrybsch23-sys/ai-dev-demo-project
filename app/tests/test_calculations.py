import pytest
from app.services.calculations import (
    bmi, bmr_mifflin_st_jeor, tdee, body_fat_navy, daily_water_intake_l
)

def test_bmi_ok():
    assert bmi(80, 1.80) == 24.69  # 80 / 3.24 = 24.691... → round 2

def test_bmi_height_must_be_positive():
    with pytest.raises(ValueError):
        bmi(80, 0)

def test_bmr_mifflin_st_jeor_male():
    assert bmr_mifflin_st_jeor("male", 70, 175, 30) == 1648.8

def test_bmr_invalid_sex():
    with pytest.raises(ValueError):
        bmr_mifflin_st_jeor("x", 70, 175, 30)

def test_tdee_known_activity():
    assert tdee(1600, "sedentary") == 1920.0

def test_tdee_unknown_activity():
    with pytest.raises(ValueError):
        tdee(1600, "super-saiyan")

def test_bodyfat_female_requires_hip():
    with pytest.raises(ValueError):
        body_fat_navy("female", 165, 34, 70, None)

def test_water_ok_and_rounding():
    # 35 ml/kg * 70 = 2450 ml; + 350 ml * 1.5 = 525 ml → 2975 ml → 2.98 L
    assert daily_water_intake_l(70, 1.5) == 2.98

def test_water_invalid_negative_activity():
    with pytest.raises(ValueError):
        daily_water_intake_l(70, -1)
