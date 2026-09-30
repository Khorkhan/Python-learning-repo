def set_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")
    print("Age = ", age)

try:
    set_age(-5)
except ValueError as e:
    print("Error: ", e)