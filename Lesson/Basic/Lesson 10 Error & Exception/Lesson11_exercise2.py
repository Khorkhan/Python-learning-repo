fruits = ["Apple", "Banana", "Orange", "Mango", "Grape"]
try:
    i = int(input("index 0 - 4: "))
    print(fruits[i])
except ValueError:
    print("Must be numbers")
except IndexError:
    print("No index here.")