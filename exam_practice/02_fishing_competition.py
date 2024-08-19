n = int(input())

matrix = []
my_pos = []

collected_fish = 0
whirlpool = False


directions = {
    "left": [0, -1],
    "right": [0, +1],
    "up": [-1, 0],
    "down": [+1, 0]
}

for row in range(n):
    matrix.append(list(input()))
    if "S" in matrix[row]:
        my_pos.extend([row, matrix[row].index("S")])



command = input()

r, c = my_pos
matrix[r][c] = "-"

while command != "collect the nets":
    r += directions[command][0]
    c += directions[command][1]

    if r not in range(n):
        if r >= n:
            r = 0
        elif r < 0:
            r = n - 1

    if c not in range(n):
        if c >= n:
            c = 0
        elif c < 0:
            c = n - 1

    next_pos = matrix[r][c]

    if next_pos.isdigit():
        collected_fish += int(next_pos)
        matrix[r][c] = "-"

    elif next_pos == "W":
        whirlpool = True
        collected_fish = 0
        break

    command = input()




if whirlpool:
    print(
        f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{','.join(str(el) for el in [r, c])}]")
    exit()

if collected_fish >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - collected_fish} tons of fish more.")

if collected_fish:
    print(f"Amount of fish caught: {collected_fish} tons.")


matrix[r][c] = "S"
[print(*i, sep="") for i in matrix]

