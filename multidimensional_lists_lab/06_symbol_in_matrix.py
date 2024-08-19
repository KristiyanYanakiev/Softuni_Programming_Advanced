row = int(input())

matrix = []

for _ in range(row):
    matrix.append(list(input()))

symbol = input()

for row_idx in range(row):
    for col_idx in range(row):
        el = matrix[row_idx][col_idx]
        if el == symbol:
            print(f"({row_idx}, {col_idx})")
            exit()

print(f"{symbol} does not occur in the matrix")
