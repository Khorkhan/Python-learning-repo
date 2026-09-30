# try / except

try:
    n = int(input("Input numbers: "))
    print(100 / n)
except ValueError:
    print("Numbers Only!")
except ZeroDivisionError:
    print("Can't devide by 0!")

# try to catch many types of errors and show detail

try:
    nums = [1, 2, 3]
    print(nums[10])
except (ValueError, IndexError) as e:
    print("Error: ", e)