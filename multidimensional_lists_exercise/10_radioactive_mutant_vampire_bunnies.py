from collections import deque

n, m = [int(x) for x in input().split()]

matrix = []

player_pos = []
player_last_alive_pos = []

player_won = False

player_dead = False

directions = {
    "L": (0, -1),
    "R": (0, +1),
    "U": (-1, 0),
    "D": (+1, 0)
}

bunnies_coordinates = []

for row in range(n):
    matrix.append(list(input()))

    if "P" in matrix[row]:
        player_pos = [row, matrix[row].index("P")]



commands = list(input())

current_tour = deque(commands)

while True:
    current_command = current_tour.popleft()

    r = player_pos[0] + directions[current_command][0]
    c = player_pos[1] + directions[current_command][1]

    matrix[player_pos[0]][player_pos[1]] = "."

    if r not in range(n) or c not in range(m):
        player_won = True

    else:
        next_step = matrix[r][c]
        if next_step == "B":
            player_dead = True
            if player_last_alive_pos:
                player_last_alive_pos[0], player_last_alive_pos[1] = r, c
            else:
                player_last_alive_pos.extend([r, c])
        else:
            matrix[r][c] = "P"
            player_pos[0], player_pos[1] = r, c


    # bunnies_movement



    for b_r in range(n):
        for b_c in range(m):
            current = matrix[b_r][b_c]
            if current == "B":
                bunnies_coordinates.append([b_r, b_c])


    for current_bunny_coordinates in bunnies_coordinates:
        row_idx = current_bunny_coordinates[0]
        col_idx = current_bunny_coordinates[1]


        if 0 <= row_idx - 1 < n:
            upper = matrix[row_idx - 1][col_idx]
            if upper == "P":
                player_dead = True
                player_last_alive_pos = [row_idx - 1, col_idx]
            matrix[row_idx - 1][col_idx] = "B"

        if 0 <= row_idx + 1 < n:
            lower = matrix[row_idx + 1][col_idx]
            if lower == "P":
                player_dead = True
                player_last_alive_pos = [row_idx + 1, col_idx]
            matrix[row_idx + 1][col_idx] = "B"

        if 0 <= col_idx -1 < m:
            left = matrix[row_idx][col_idx - 1]
            if left == "P":
                player_dead = True
                player_last_alive_pos = [row_idx, col_idx - 1]
            matrix[row_idx][col_idx - 1] = "B"

        if 0 <= col_idx + 1 < m:
            right = matrix[row_idx][col_idx + 1]
            if right == "P":
                player_dead = True
                player_last_alive_pos = [row_idx, col_idx + 1]
            matrix[row_idx][col_idx + 1] = "B"
    if player_dead or player_won:
        break

[print(*i, sep="") for i in matrix]

if player_won:
    print(f"won: {player_pos[0]} {player_pos[1]}")

elif player_dead:
    print(f"dead: {player_last_alive_pos[0]} {player_last_alive_pos[1]}")







