scores = []
for i in range(5):
    s = float(input(f"Subject Score {i+1}: "))
    scores.append(s)
scores.sort(reverse=True)
print(scores)