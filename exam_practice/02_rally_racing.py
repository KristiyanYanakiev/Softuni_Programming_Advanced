n = int(input())

racing_number = input()

kilometers_passed = 0
matrix = []

tunel_pos = []


for row in range(n):
    matrix.append(input().split())
    line = matrix[row]
    for el in line:
        if el == "T":
            tunel_pos.append([row, line.index("T")])

directions = {
    "left": [0, -1],
    "right": [0, +1],
    "up": [-1, 0],
    "down": [+1, 0]
}

r, c = 0, 0

finished = False
exit_race = False

while True:
    command = input()

    if command == "End":
        exit_race = True
        break

    r += directions[command][0]
    c += directions[command][1]

    next_move = matrix[r][c]

    if next_move == "F":
        kilometers_passed += 10
        finished = True
        break

    elif next_move == "T":
        tunel_pos.remove([r, c])
        kilometers_passed += 30
        matrix[r][c] = "."

        r, c = tunel_pos[0]
        matrix[r][c] = "."

    else:
        kilometers_passed += 10

matrix[r][c] = "C"

if exit_race:
    print(f"Racing car {racing_number} DNF.")
elif finished:
    print(f"Racing car {racing_number} finished the stage!")

print(f"Distance covered {kilometers_passed} km.")

for row in matrix:
    print(*row, sep="")






