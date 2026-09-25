nums = [1, 3, 3, 5, 1, 7, 7, 7]
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
print(unique)