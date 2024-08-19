size = 5

matrix = []

my_pos = []


total_targets = 0
hit_targets = 0

hit_targets_pos = []

for row in range(size):
    matrix.append(input().split())

    if "A" in matrix[row]:
        my_pos.extend([row, matrix[row].index("A")])

    if "x" in matrix[row]:
        total_targets += matrix[row].count("x")


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}



num_of_commands = int(input())


for _ in range(num_of_commands):
    command = input().split()

    if command[0] == "move":
        direction = command[1]
        steps = int(command[2])


        r = my_pos[0] + directions[direction][0] * steps
        c = my_pos[1] + directions[direction][1] * steps

        if r in range(size) and c in range(size) and matrix[r][c] == ".":
            matrix[my_pos[0]][my_pos[1]] = "."
            matrix[r][c] = "A"
            my_pos[0], my_pos[1] = r, c


    elif command[0] == "shoot":
        direction = command[1]

        r_idx = my_pos[0] + directions[direction][0]
        c_idx = my_pos[1] + directions[direction][1]

        while r_idx in range(size) and c_idx in range(size):
            if matrix[r_idx][c_idx] == "x":
                matrix[r_idx][c_idx] = "."
                hit_targets += 1
                hit_targets_pos.append([r_idx, c_idx])
                break
            r_idx += directions[direction][0]
            c_idx += directions[direction][1]

    if hit_targets == total_targets:
        print(f"Training completed! All {total_targets} targets hit.")
        break

if hit_targets < total_targets:
    print(f"Training not completed! {total_targets - hit_targets} targets left.")


[print(line) for line in hit_targets_pos]
