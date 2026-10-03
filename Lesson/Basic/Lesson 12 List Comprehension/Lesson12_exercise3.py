# Giveen 3 subjects, each with a name and a score, use zig()
# to pair them together and find the subject with the highest score
# (without using max() directly on the tuples)

subjects = ["Math", "Science", "English"]
scores = [78, 91, 85]
pairs = list(zip(scores, subjects))
best_score, best_subject = max(pairs)
print(f"Best: {best_subject} ({best_score})")