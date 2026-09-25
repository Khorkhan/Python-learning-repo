fruits = ["Banana", "Orange", "Mango"]
print(fruits[0])
print(fruits[-1])

fruits.append("Grape")           # add behind
fruits.insert(1, "Apple")           # insert position 1
fruits.remove("Orange")         # Delete
last = fruits.pop()         # pull last one out
print(fruits, "| pop: ", last)