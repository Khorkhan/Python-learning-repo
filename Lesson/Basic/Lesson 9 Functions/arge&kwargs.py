def total(*nums):
    return sum(nums)

print(total(1, 2, 3, 4))

def profile(**info):
    for k, v in info.items():
        print(f"{k}: {v}")

profile(name="Alex", age=(20))