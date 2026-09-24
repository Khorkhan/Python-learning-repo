# while

count = 1
while count <= 5:
    print("Round", count)
    count += 1

# for range

for i in range(5):
    print(i)

for i in range(2, 11, 2):
    print(i)

for c in "Python":
    print(c)

# break continue
for i in range(1, 10):
    if i == 5:
        break
    print(i)

for i in range(1,6):
    if i == 3:
        continue
    print(i)

# for else

n = 13
for i in range(2, n):
    if n % i == 0:
        print("Not unique number")
        break
else:
    # end loop without break
    print("Is unique number")

# loop in loop
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row}x{col}={row*col}", end=" ")
    print()