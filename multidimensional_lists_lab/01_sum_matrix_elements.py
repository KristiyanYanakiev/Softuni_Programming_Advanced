row, col = [int(i) for i in input().split(", ")]

matrix = []
total = 0

for row_index in range(row):
    data = [int(el) for el in input().split(", ")]
    total += sum(data)
    matrix.append(data)


print(total)
print(matrix)


