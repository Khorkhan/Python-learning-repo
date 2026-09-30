while True:
    try:
        a = float(input("No.1: "))
        b = float(input("No.2: "))
        print("Plus Result = ", a + b)
        break
    except ValueError:
        print("Input correct Numbers!")