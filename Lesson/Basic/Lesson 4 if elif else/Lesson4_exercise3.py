# Exericse 4: Price of one item and quantity purchased - Buy 10 or more, get 10 % discoutL
# Buy 5-9, get 5% discount; calculate the actual payment amount.

price = float(input("price/piece: "))
qty = int(input("piece: "))

total = price * qty
if qty >= 10:
    total *= 0.90
elif qty >= 5:
    total *= 0.95

print(f"total: {total:.2f} b.")