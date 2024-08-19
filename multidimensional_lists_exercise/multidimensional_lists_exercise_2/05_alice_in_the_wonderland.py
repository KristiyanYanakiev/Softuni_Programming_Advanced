n = int(input())

matrix = []

alice_pos = []

collected_tea = 0
game_over = False

for row in range(n):
    matrix.append(input().split())
    if "A" in matrix[row]:
        alice_pos.extend([row, matrix[row].index("A")])
        matrix[row][matrix[row].index("A")] = "*"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

r = alice_pos[0]
c = alice_pos[1]

while not game_over and collected_tea < 10:
    command = input()

    r += directions[command][0]
    c += directions[command][1]

    if r not in range(n) or c not in range(n):
        game_over = True
        continue

    if matrix[r][c] == "R":
        game_over = True

    elif matrix[r][c].isdigit():
        collected_tea += int(matrix[r][c])

    matrix[r][c] = "*"



if collected_tea < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*i) for i in matrix]





