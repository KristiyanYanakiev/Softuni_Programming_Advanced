num_of_lines = int(input())

stack = []

for _ in range(num_of_lines):
    command = input().split()

    if "1" == command[0]:
        stack.append(int(command[1]))

    elif "2" == command[0]:
        if stack:
            stack.pop()

    elif "3" == command[0]:
        if stack:
            print(max(stack))

    else:
        if stack:
            print(min(stack))

print(*stack[::-1], sep=", ")


