text = input("Sentence: ").lower()
vowels = "aeiou"
count = sum(1 for ch in text if ch in vowels)
print(f"Has vowels {count}.")