text = "cat like fish cat like sleep cat"
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
print(counts)