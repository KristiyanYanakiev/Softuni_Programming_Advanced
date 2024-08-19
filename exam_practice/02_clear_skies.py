airspace_size = int(input())

airspace = []

jetfifghter_pos = []

enemy_count = 4

armor = 300

for row in range(airspace_size):
    airspace.append(list(input()))
    if "J" in airspace[row]:
        jetfifghter_pos.extend([row, airspace[row].index("J")])
        airspace[row][airspace[row].index("J")] = "-"



directions = {
    "left": [0, -1],
    "right": [0, +1],
    "up": [-1, 0],
    "down": [+1, 0]
}

current_jet_fighter_r = jetfifghter_pos[0]
current_jet_fighter_c = jetfifghter_pos[1]

while enemy_count > 0 and armor > 0:
    command = input()

    r, c = current_jet_fighter_r + directions[command][0], current_jet_fighter_c + directions[command][1]

    if airspace[r][c] == "-":
        airspace[current_jet_fighter_r][current_jet_fighter_c] = "-"
        current_jet_fighter_r = r
        current_jet_fighter_c = c

        continue

    elif airspace[r][c] == "E":
        enemy_count -= 1
        airspace[r][c] = "-"
        current_jet_fighter_r = r
        current_jet_fighter_c = c
        airspace[current_jet_fighter_r][current_jet_fighter_c] = "-"


        if enemy_count == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            airspace[r][c] = "J"
            [print(*row, sep="") for row in airspace]
            break
        else:
            armor -= 100
            if armor == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{r}, {c}]!")
                airspace[r][c] = "J"
                [print(*row, sep="") for row in airspace]
                break


    elif airspace[r][c] == "R":
        armor = 300
        airspace[r][c] = "-"
        airspace[current_jet_fighter_r][current_jet_fighter_c] = "-"
        current_jet_fighter_r = r
        current_jet_fighter_c = c


