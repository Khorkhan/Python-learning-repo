# sorted()

students = [
    {"name": "Alex", "gpa": 3.2},
    {"name": "Bill", "gpa": 3.9},
]
by_gpa = sorted(students, key=lambda s: s["gpa"], reverse=True)
print(by_gpa[0]["name"])

words = ["Banana", "Fig", "apple"]
print(sorted(words, key=str.lower))

# any/ all
scores = [55, 80, 90]
print(any(s < 50 for s in scores))
print(all(s >= 50 for s in scores))