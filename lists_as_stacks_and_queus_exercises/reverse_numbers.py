stack_of_nums = [int(num) for num in input().split()]

result = []

while stack_of_nums:
    result.append(stack_of_nums.pop())

print(*result)

