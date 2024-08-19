stack_of_clothes = [int(element) for element in input().split()]
rack_capacity = int(input())

rack_counter = 1
sum_of_taken_out_clothes = 0

while stack_of_clothes:
    if len(stack_of_clothes) == 1:
        rack_counter += 1
    current_cloth = stack_of_clothes.pop()

    sum_of_taken_out_clothes += current_cloth

    if sum_of_taken_out_clothes <= rack_capacity:
        pass

    else:
        rack_counter += 1
        sum_of_taken_out_clothes = abs(sum_of_taken_out_clothes - rack_capacity)


print(rack_counter)












