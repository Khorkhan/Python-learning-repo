# Exercise 2: Input a year A.D. and check whether it is a leap year
# divisible by 4, but if divisible by 100, it must also be divisible by 400.

year = int(input("year A.D.: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year.")
else:
    print("Not leap year.")