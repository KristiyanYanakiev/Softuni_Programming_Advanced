row = int(input())

matrix = []

for _ in range(row):
    sub_list = [int(el) for el in input().split()]
    matrix.append(sub_list)

diagonal_sum = 0

for row_index in range(row):
    for col_index in range(row):
        if row_index == col_index:
            num = matrix[row_index][row_index]
            diagonal_sum += num

print(diagonal_sum)
