file = open("numbers.txt", "w")


content = ""

for el in range(1, 6):
    content += f"{el}\n"

file_name = "numbers.txt"
file.write(content)

file = open(file_name, "r")

print(file.read())
