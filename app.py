# simple starter file the AI can extend
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    if height_m <= 0:
        raise ValueError("height_m must be > 0")
    return round(weight_kg / (height_m ** 2), 2)

if __name__ == "__main__":
    print("BMI(70, 1.75) =", calculate_bmi(70, 1.75))
