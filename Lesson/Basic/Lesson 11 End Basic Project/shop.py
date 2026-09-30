products = [
    {"name": "drinking water", "price": 10, "qty" : 20},
    {"name": "Snack", "price": 15, "qty": 12},
    {"name": "Milk", "price": 20, "qty": 8},
]
sales = 0.0

def show_products():
    print("\n --- Product's Store ---")
    for p in products:
        print(f"{p['name']}: {p['price']} b. (remaining: {p['qty']})")

def sell():
    global sales
    name = input("Product's name: ")
    for p in products:
        if p["name"] == name:
            n = int(input("qty: "))
            if n <= p["qty"]:
                p["qty"] -= n
                total = p["price"] * n
                sales += total
                print(f"Sale {n} pieces. = {total} b.")
            else:
                print("Out of Stock!")
            return
        print("Product not found!")

def restock():
    name = input("Product's name: ")
    for p in products:
        if p["name"] == name:
            p["qty"] += int(input("How many do you want to add more?: "))
            print("Add in Stock")
            return
    print("Product not found.")

while True:
    print("\n1) Show Product 2) Sale 3) Add Stock 4) Sale Total 5) Exit")
    choice = input("Pick: ")
    if choice == "1":
        show_products()
    elif choice == "2":
        sell()
    elif choice == "3":
        restock()
    elif choice == "4":
        print(f"Total sale: {sales:.0f} b.")
    elif choice == "5":
        print("Store close thanks")
        break
    else:
        print("Doesn't have this option")