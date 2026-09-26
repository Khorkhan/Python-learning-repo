full = input("Name-surname: ")
parts = full.split()
initials = ".".join(p[0].upper() for p in parts) + "."
print(initials)