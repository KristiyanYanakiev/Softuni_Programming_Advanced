symbols = ("-", ",", ".", "!", "?")

with open("text.txt", "r") as text_file:

    lines = text_file.readlines()

    for row in range(0, len(lines), 2):

        for symbol in symbols:
            lines[row] = lines[row].replace(symbol, "@")

        print(*lines[row].split()[::-1])



