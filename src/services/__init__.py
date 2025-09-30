"""
Reusable business logic used by API and (future) background workers.
"""
from .calculations import (
    bmi,
    bmr_mifflin_st_jeor,
    tdee,
    body_fat_navy,
    daily_water_intake_l,
)
from .recommendations import simple_recommendations

__all__ = [
    "bmi",
    "bmr_mifflin_st_jeor",
    "tdee",
    "body_fat_navy",
    "daily_water_intake_l",
    "simple_recommendations",
]
