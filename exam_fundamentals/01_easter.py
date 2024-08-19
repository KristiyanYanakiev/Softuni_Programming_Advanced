string = input()
res = string

while True:
    command = input()

    if command == "Easter":
        break
    data = command.split()

    if "Replace" in data:
        current_char = data[1]
        new_char = data[2]

        res = res.replace(current_char, new_char)
        print(res)

    elif "Remove" in data:
        substring = data[1]

        res = res.replace(substring, "")
        print(res)

    elif "Includes" in data:
        print(data[1] in res)

    elif "Change" in data:
        if data[1] == "Lower":
            res = res.lower()
        else:
            res = res.upper()

        print(res)

    elif "Reverse" in data:
        start_index = int(data[1])
        end_index = int(data[2])

        if start_index in range(len(res)) and end_index in range(len(res)):
            substring = res[start_index:end_index + 1]
            print(substring[::-1])
        else:
            continue
