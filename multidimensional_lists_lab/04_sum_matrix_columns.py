row, col = [int(el) for el in input().split(", ")]

matrix = []


for row_index in range(row):
    data = [int(x) for x in input().split()]
    matrix.append(data)


for col_idx in range(col):
    sum_of_cols = 0
    for row_idx in range(row):
        sum_of_cols += matrix[row_idx][col_idx]
    print(sum_of_cols)



