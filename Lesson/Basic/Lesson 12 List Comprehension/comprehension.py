# conprehension

squares = [n ** 2 for n in range(1, 6)]

evens = [n for n in range(20) if n % 2 == 0]

# condition if/else
labels = ["High" if s >= 50 else "Low" for s in [30, 70, 90]]

# Nested comprehension

matrix = [[1, 2, 3,], [4, 5, 6]]
flat = [x for row in matrix for x in row]
transpose = [[row[i] for row in matrix] for i in range(3)]

# Other comprehension

squares_map = {n: n ** 2 for n in range(4)}
unique = {ch for ch in "Hello"}
gen = (n ** 2 for n in range(10 ** 9))

# map / filter

nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
evens2 = list(filter(lambda x: x % 2 == 0, nums))

# zip and enumerate

names =["Alex", "Bill"]
scores = [80, 92]
for name, scores in zip(names, scores):
    print(f"{name}: {scores}")

for i, names in enumerate(name, start=1):
    print(i, names)