row = int(input())

matrix = []
for row_index in range(row):
    data = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(data)

print(matrix)
