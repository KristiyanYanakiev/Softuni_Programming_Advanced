def check_valid_indices(r, c, some_matrix):
    return r in range(n) and c in range(len(some_matrix[r]))


n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

command = input()

while command != "END":
    action, row, col, num = command.split()
    row = int(row)
    col = int(col)
    num = int(num)

    if action == "Add":
        if check_valid_indices(row, col, matrix):
            matrix[row][col] += num
        else:
            print("Invalid coordinates")

    elif action == "Subtract":
        if check_valid_indices(row, col, matrix):
            matrix[row][col] -= num
        else:
            print("Invalid coordinates")

    command = input()

[print(*i) for i in matrix]
