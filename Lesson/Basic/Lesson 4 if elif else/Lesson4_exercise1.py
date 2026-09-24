# Excercise 1: Receive 3 numbers and find the largest value using if-elif-else
# do not use max()

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a >= b and a >= c:
    print(f"Largest is {a}")
elif b >= a and b >= c:
    print(f"Largest is {b}")
else:
    print(f"Largest is {c}")