# exercise 2 ibm

def bmi(weight, height_cm):
    h = height_cm / 100
    value = weight / (h ** 2)
    if value < 18.5:
        level = "Skinny"
    elif value < 25:
        level = "Normal"
    else:
        level = "Fat"
    return value, level

b, level = bmi(65, 170)
print(f"BMI = {b:.1f} -> {level}")