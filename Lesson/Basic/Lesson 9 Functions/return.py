def analyze(nums):
    return min(nums), max(nums), sum(nums) / len(nums)

lo, hi, avg = analyze([3, 7, 1, 9])
print(lo, hi, avg)