from collections import deque

n = int(input())

movements = deque(input().split())


matrix = []
miner_place = []
total_coal = 0
collected_coal = 0



directions = {
    "left": [0, -1],
    "right": [0, +1],
    "up": [-1, 0],
    "down": [+1, 0]
}

for row in range(n):
    matrix.append(input().split())
    if "s" in matrix[row]:
        miner_place = [row, matrix[row].index("s")]
    if "c" in matrix[row]:
        total_coal += matrix[row].count("c")


r, c = miner_place
r_idx, c_idx = r, c

while movements:
    current_move = movements.popleft()

    move_r, move_c = directions[current_move]
    if r_idx + move_r not in range(n) or c_idx + move_c not in range(n):
        continue

    r_idx, c_idx = r_idx + move_r, c_idx + move_c
    current_stop = matrix[r_idx][c_idx]

    if current_stop == "c":
        collected_coal += 1
        matrix[r_idx][c_idx] = "*"
        if collected_coal == total_coal:
            print(f"You collected all coal! ({r_idx}, {c_idx})")
            break

    elif current_stop == "e":
        print(f"Game over! ({r_idx}, {c_idx})")
        break

else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({r_idx}, {c_idx})")







