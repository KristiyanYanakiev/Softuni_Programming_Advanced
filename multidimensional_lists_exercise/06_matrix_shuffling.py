def check_valid_indecies(some_coordinates):
    return {some_coordinates[0], some_coordinates[2]}.issubset(valid_rows) and {some_coordinates[1], some_coordinates[3]}.issubset(valid_cols)

def swap(some_action, some_coordinates):
    if some_action == "swap" and len(some_coordinates) == 4 and check_valid_indecies(some_coordinates):
        r_1 = some_coordinates[0]
        r_2 = some_coordinates[2]
        c_1 = some_coordinates[1]
        c_2 = some_coordinates[3]

        matrix[r_1][c_1], matrix[r_2][c_2] = matrix[r_2][c_2], matrix[r_1][c_1]
        [print(*i) for i in matrix]

    else:
        print("Invalid input!")


row, col = [int(x) for x in input().split()]

matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(row)]

valid_rows = range(row)
valid_cols = range(col)

while True:
    command = input()

    if command == "END":
        break

    action, *coordinates = [int(x) if x.isdigit() else x for x in command.split()]

    swap(action, coordinates)

