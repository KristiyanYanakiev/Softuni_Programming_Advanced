rows, cols = [int(x) for x in input().split()]

matrix = []

boy_starting_pos = []

delivered = False
out_of_range = False

for r_idx in range(rows):
    matrix.append(list(input()))
    line = matrix[r_idx]

    if "B" in line:
        boy_starting_pos.extend([r_idx, line.index("B")])

directions = {
    "left": [0, -1],
    "right": [0, +1],
    "up": [-1, 0],
    "down": [+1, 0]
}

r, c = boy_starting_pos

while not delivered:
    command = input()
    r += directions[command][0]
    c += directions[command][1]

    if r not in range(rows) or c not in range(cols):
        print("The delivery is late. Order is canceled.")
        out_of_range = True
        break

    cell = matrix[r][c]

    if cell == "P":
        matrix[r][c] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    elif cell == "*":
        r -= directions[command][0]
        c -= directions[command][1]
        continue

    elif cell == "A":
        matrix[r][c] = "P"
        print("Pizza is delivered on time! Next order...")
        delivered = True

    elif cell == "-":
        matrix[r][c] = "."


if out_of_range:
    start_r, start_c = boy_starting_pos
    matrix[start_r][start_c] = " "

for i in matrix:
    print("".join(i))

