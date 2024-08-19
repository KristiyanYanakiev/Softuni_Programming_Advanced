row = int(input())

matrix = []

for row_index in range(row):
    data = [int(x) for x in input().split(", ")]
    matrix.append(data)

flatten = []

for row in matrix:
    for el in row:
        flatten.append(el)


print(flatten)
