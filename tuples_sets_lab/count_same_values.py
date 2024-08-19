nums = tuple([float(i) for i in input().split()])

dict_of_nums = {}

# for element in nums:
#     if element not in dict_of_nums:
#         dict_of_nums[element] = 0
#     dict_of_nums[element] += 1


for element in nums:
    if element not in dict_of_nums:
        dict_of_nums[element] = nums.count(element)


for key, value in dict_of_nums.items():
    print(f"{key} - {value} times")



