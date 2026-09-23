total = int(input("Secound: "))
h = total // 3600
m = (total & 3600) // 60
s = total % 60
print(f"{h} hours. {m} minute. {s} secound.")