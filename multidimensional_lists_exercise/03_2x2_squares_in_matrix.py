r, c = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(r)]

square_found = 0

for r_idx in range(r - 1):
    for c_idx in range(c -1):
        el = matrix[r_idx][c_idx]
        right = matrix[r_idx][c_idx + 1]
        below = matrix[r_idx + 1][c_idx]
        right_diagonal = matrix[r_idx + 1][c_idx + 1]
        square_found += 1 if el == right == below == right_diagonal else 0

# 0, 0 > current
# 0, 1 > right
# 1, 0 > below
# 1, 1 > right_diagonal

print(square_found)
