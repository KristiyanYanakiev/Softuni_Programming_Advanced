size_of_matrix = int(input())

matrix = []

bunny_pos = []
field_pos_of_collected_eggs = []
max_collected_eggs = float("-inf")
best_direction = ""

for row in range(size_of_matrix):
    matrix.append(input().split())
    if "B" in matrix[row]:
        bunny_pos = [row, matrix[row].index("B")]


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


for direction, coordinations in directions.items():
    current_collected_eggs = 0
    current_field_pos_collected_eggs = []
    r, c = [
        bunny_pos[0] + coordinations[0],
        bunny_pos[1] + coordinations[1]
    ]


    while 0 <= r < size_of_matrix and 0 <= c < size_of_matrix:
        if matrix[r][c] == "X":
            break

        current_collected_eggs += int(matrix[r][c])
        current_field_pos_collected_eggs.append([r, c])

        r += coordinations[0]
        c += coordinations[1]

    if current_collected_eggs >= max_collected_eggs:
        max_collected_eggs = current_collected_eggs
        field_pos_of_collected_eggs = current_field_pos_collected_eggs
        best_direction = direction





print(best_direction)

print(*field_pos_of_collected_eggs, sep="\n")

print(max_collected_eggs)











