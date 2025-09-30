import pytest
from app.services.calculator import (
    bmi, bmr_mifflin_st_jeor, tdee, body_fat_navy, daily_water_intake_l
)

def test_bmi():
    assert bmi(70, 1.75) == 22.86

def test_bmr_male():
    assert bmr_mifflin_st_jeor("male", 70, 175, 30) == pytest.approx(1648.8, 0.1)

def test_tdee_moderate():
    val = tdee(1600, "moderate")
    assert val == 2480.0

def test_body_fat_inputs():
    with pytest.raises(ValueError):
        body_fat_navy("male", 175, 40, -1)

def test_water():
    assert daily_water_intake_l(70, 1) == 2.8
