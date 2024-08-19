from collections import deque

n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

bomb_coordinates = input().split()

bomb_coordinates = deque([int(x) for el in bomb_coordinates for x in el.split(",")])


while bomb_coordinates:
    current_bomb_coordinates = [bomb_coordinates.popleft() for _ in range(2)]
    bomb_row = current_bomb_coordinates[0]
    bomb_col = current_bomb_coordinates[1]
    bomb_value = matrix[bomb_row][bomb_col]

    if bomb_value <= 0:
        continue

    else:
        matrix[bomb_row][bomb_col] -= bomb_value
        if bomb_row > 0:
            matrix[bomb_row - 1][bomb_col] -= bomb_value if matrix[bomb_row - 1][bomb_col] > 0 else 0
        if bomb_row < n - 1:
            matrix[bomb_row + 1][bomb_col] -= bomb_value if matrix[bomb_row + 1][bomb_col] > 0 else 0
        if bomb_col > 0:
            matrix[bomb_row][bomb_col - 1] -= bomb_value if matrix[bomb_row][bomb_col - 1] > 0 else 0
        if bomb_col < n - 1:
            matrix[bomb_row][bomb_col + 1] -= bomb_value if matrix[bomb_row][bomb_col + 1] > 0 else 0


        #diagonals (top_left, top_right, down_left, down_right)

        if bomb_row > 0 and bomb_col > 0:
            matrix[bomb_row - 1][bomb_col - 1] -= bomb_value if matrix[bomb_row - 1][bomb_col - 1] > 0 else 0
        if bomb_row > 0 and bomb_col < n - 1:
            matrix[bomb_row - 1][bomb_col + 1] -= bomb_value if matrix[bomb_row - 1][bomb_col + 1] > 0 else 0

        if bomb_row < n - 1 and bomb_col > 0:
            matrix[bomb_row + 1][bomb_col - 1] -= bomb_value if matrix[bomb_row + 1][bomb_col - 1] > 0 else 0

        if bomb_row < n - 1 and bomb_col < n - 1:
            matrix[bomb_row + 1][bomb_col + 1] -= bomb_value if matrix[bomb_row + 1][bomb_col + 1] > 0 else 0


alive_cells = 0
sum_cells = 0

for r in range(n):
    for c in range(n):
        current_cell = matrix[r][c]
        if current_cell > 0:
            alive_cells += 1
            sum_cells += current_cell


print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_cells}")

[print(*i) for i in matrix]








