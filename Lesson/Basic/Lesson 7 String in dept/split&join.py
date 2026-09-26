csv = "apple, banana, mango"
items= csv.split(",")
joined = " + ".join(items)

# example:
nums = [int(x) for x in input("Many nums: ").split()]
print(nums, sum(nums))

# check string 
print("123".isdigit())
print("abc".isalpha())
print("hi5".isalnum())
print(" ".isspace())