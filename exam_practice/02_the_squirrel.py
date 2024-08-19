from collections import deque

collected_hazelnuts = 0

n = int(input())

squirrel_pos = []
matrix = []

trap = False
out_of_range = False


directions = {
    "left": [0, -1],
    "right": [0, +1],
    "up": [-1, 0],
    "down": [+1, 0]
}

commands = deque(input().split(", "))

for row in range(n):
    matrix.append(list(input()))
    line = matrix[row]

    if "s" in line:
        s_r = row
        s_c = line.index("s")
        squirrel_pos.extend([s_r, s_c])
        matrix[s_r][s_c] = "*"

r, c = squirrel_pos

while collected_hazelnuts < 3 and not trap and not out_of_range and commands:

        command = commands.popleft()
        r += directions[command][0]
        c += directions[command][1]

        if r in range(n) and c in range(n):

            next_step = matrix[r][c]

            if next_step == "h":
                collected_hazelnuts += 1
                matrix[r][c] = "*"

            elif next_step == "t":
                trap = True

        else:
            out_of_range = True

if out_of_range:
    print("The squirrel is out of the field.")
elif trap:
    print("Unfortunately, the squirrel stepped on a trap...")
elif collected_hazelnuts < 3:
    print("There are more hazelnuts to collect.")
elif collected_hazelnuts >= 3:
    print("Good job! You have collected all hazelnuts!")

print(f"Hazelnuts collected: {collected_hazelnuts}")





