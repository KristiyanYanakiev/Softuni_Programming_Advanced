records = {}

while True:
    command = input()

    if command == "Results":
        break

    data = command.split(":")

    if "Add" in data:
        person_name = data[1]
        health = int(data[2])
        energy = int(data[3])

        if person_name not in records.keys():
            records[person_name] = [health, energy]
        else:
            records[person_name][0] += health



    elif "Attack" in data:
        attacker_name = data[1]
        defender_name = data[2]
        damage = int(data[3])

        if attacker_name in records.keys() and defender_name in records.keys():
            records[defender_name][0] -= damage
            records[attacker_name][1] -= 1

            if records[defender_name][0] <= 0:
                print(f"{defender_name} was disqualified!")
                del records[defender_name]

            if records[attacker_name][1] <= 0:
                print(f"{attacker_name} was disqualified!")
                del records[attacker_name]

    elif "Delete" in data:
        username = data[1]


        if username == "All":
            records = records.clear()
        else:
            del records[username]

count = len(records.keys())
print(f"People count: {count}")

for k, v in records.items():
    print(f"{k} - {v[0]} - {v[1]}")









