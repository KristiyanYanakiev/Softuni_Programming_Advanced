stops = input()

action = ""
data = []

while True:
    command = input()
    if command == "Travel":
        break

    if "::" in command:
        action, *data = command.split("::")
    else:
        action, *data = command.split(":")

    if action == "Add Stop":
        index = int(data[0])
        word = data[1]
        if index in range(len(stops)):
            stops = stops[:index] + word + stops[index::]

        print(stops)

    elif action == "Remove Stop":
        start_index = int(data[0])
        end_index = int(data[1])

        if start_index in range(len(stops)) and end_index in range(len(stops)):
            stops = stops[:start_index] + stops[end_index + 1::]

        print(stops)

    elif action == "Switch":
        old, new = data

        if old in stops:
            stops = stops.replace(old, new)

        print(stops)

print(f"Ready for world tour! Planned stops: {stops}")