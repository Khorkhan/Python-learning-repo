s = input("Words: ").lower().replace(" ", "")
if s == s[::-1]:
    print("Is palindrome")
else:
    print("Not palindrome")