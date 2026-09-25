fruits = ["Banana", "Orange", "Mango"]

fruits.append("Grape")
fruits.insert(1, "Apple")
fruits.remove("Orange")

for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):
    print(i, fruit)