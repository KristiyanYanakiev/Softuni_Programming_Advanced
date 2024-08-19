from functools import reduce

nums = input().split()

index = 0

functions = {
    "*": lambda i: reduce(lambda x, y: x * y, map(int, nums[:i])),
    "+": lambda i: reduce(lambda x, y: x + y, map(int, nums[:i])),
    "/": lambda i: reduce(lambda x, y: x // y, map(int, nums[:i])),
    "-": lambda i: reduce(lambda x, y: x - y, map(int, nums[:i]))
}

while index < len(nums):
    element = nums[index]



    if element in "*+-/":
        nums[0] = functions[element](index)
        [nums.pop(1) for _ in range(index)]
        index = 1

    index += 1

print(nums[0])
