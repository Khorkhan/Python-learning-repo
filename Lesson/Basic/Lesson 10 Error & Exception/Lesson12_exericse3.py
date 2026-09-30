def divide(a, b):
    if b == 0:
        raise ValueError("Can't devide by 0")
    return a / b

try:
    print(divide(10, 2))
    print(divide(1, 0))
except ValueError as e:
    print("error: ", e)
