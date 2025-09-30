from app import calculate_bmi
import pytest

def test_bmi_nominal():
    assert calculate_bmi(70, 1.75) == 22.86

def test_bmi_bad_height():
    with pytest.raises(ValueError):
        calculate_bmi(70, 0)
