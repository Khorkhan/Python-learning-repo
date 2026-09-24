age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Can enter")
    else:
        print("Must show ID card.")
else:
    print("Underage")

# condition with and/or

if age >= 18 and has_id:
    print("Can enter")

# ternary - if single line

status = "Adult" if age >= 18 else "Teen"
print(status)