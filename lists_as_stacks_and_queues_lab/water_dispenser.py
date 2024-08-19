from collections import deque

starting_quantity_of_water = int(input())

line_of_people = deque([])

while True:
    command = input()

    if command == "Start":
        break

    name = command
    line_of_people.append(name)

while True:
    command = input()

    if command == "End":
        break

    command_as_list = command.split()
    if len(command_as_list) == 1:
        litters = int(command_as_list[0])

        if litters <= starting_quantity_of_water:
            person_name = line_of_people.popleft()
            print(f"{person_name} got water")
            starting_quantity_of_water -= litters

        else:
            person_name = line_of_people.popleft()
            print(f"{person_name} must wait")

    else:
        litters = int(command_as_list[1])
        starting_quantity_of_water += litters

print(f"{starting_quantity_of_water} liters left")