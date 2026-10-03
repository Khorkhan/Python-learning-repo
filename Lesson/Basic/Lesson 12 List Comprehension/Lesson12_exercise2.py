# giveen the list ["apple", "fig", "banana", "wiki"]
# create a new list containing only the words that have more than 3 characters,
# then convert them to uppercase.

words = ["apple", "fig", "banana", "kiwi"]
result = [w.upper() for w in words if len(w) > 3]
print(result)