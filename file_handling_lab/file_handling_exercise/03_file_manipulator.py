while True:
    command = input()

    if command == "End":
        break

    action, *info = command.split("-")

    if action == "Create":
        open(info[0], "w")

    elif action == "Add":
        file = open(info[0], "a")
        file.write(info[1])

