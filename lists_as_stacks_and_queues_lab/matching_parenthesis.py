string = input()

stack_with_indexes = []

for current_index in range(len(string)):
    if string[current_index] == "(":
        stack_with_indexes.append(current_index)

    elif string[current_index] == ")":
        print(string[stack_with_indexes.pop():current_index + 1])

