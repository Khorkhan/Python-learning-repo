# Use a list comprehension to create a list of numbers 
# from 1 - 50 that are divisible by 3 or 5, then calculate their sum

nums = [n for n in range(1, 51) if n % 3 == 0 or n % 5 == 0]
print(sum(nums))