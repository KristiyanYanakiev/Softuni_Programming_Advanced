first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(i) for i in input().split()])

n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == "Add" and command[1] == "First":
        nums_to_add = [int(el) for el in command[2::]]
        for num in nums_to_add:
            first_sequence.add(num)

    elif command[0] == "Add" and command[1] == "Second":
        nums_to_add = [int(el) for el in command[2::]]
        for num in nums_to_add:
            second_sequence.add(num)

    elif command[0] == "Remove" and command[1] == "First":
        nums_to_remove = [int(el) for el in command[2::]]
        for num in nums_to_remove:
            if num in first_sequence:
                first_sequence.remove(num)

    elif command[0] == "Remove" and command[1] == "Second":
        nums_to_remove = [int(el) for el in command[2::]]
        for num in nums_to_remove:
            if num in second_sequence:
                second_sequence.remove(num)

    elif command[0] == "Check":
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print("True")
        else:
            print("False")

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")

