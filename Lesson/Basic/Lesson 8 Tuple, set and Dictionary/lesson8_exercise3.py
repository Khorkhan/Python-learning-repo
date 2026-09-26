fruits = {"Apple": 25, "Banana": 10, "Orange": 15}
name = input("fruit's name: ")
price = fruits.get(name)
if price is None:
    print("fruit not found")
else:
    print(f"{name} price {price} bath.")