n = int(input())

health = 100
MAX_HEALTH = 100
matrix = []
starting_pos = []

for row in range(n):
    matrix.append(list(input()))

    line = matrix[row]
    if "P" in line:
        starting_pos.extend([row, line.index("P")])

directions = {
    "left": [0, -1],
    "right": [0, +1],
    "up": [-1, 0],
    "down": [+1, 0]
}

exit_reached = False
traveller_died = False

r, c = starting_pos
matrix[r][c] = "-"
while not exit_reached and not traveller_died:
    direction = input()

    r += directions[direction][0]
    c += directions[direction][1]

    if r not in range(n) or c not in range(n):
        r -= directions[direction][0]
        c -= directions[direction][1]
        continue

    next_cell = matrix[r][c]

    if next_cell == "M":
        health -= 40

        if health <= 0:
            health = 0
            matrix[r][c] = "P"
            traveller_died = True
        else:
            matrix[r][c] = "-"

    elif next_cell == "H":
        health += 15
        if health > MAX_HEALTH:
            health = MAX_HEALTH

        matrix[r][c] = "-"

    elif next_cell == "X":
        matrix[r][c] = "P"
        exit_reached = True


if not health:
    print("Player is dead. Maze over!")

else:
    print("Player escaped the maze. Danger passed!")

print(f"Player's health: {health} units")

[print(*i, sep="") for i in matrix]




