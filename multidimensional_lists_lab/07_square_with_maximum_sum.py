row, col = [int(x) for x in input().split(", ")]

matrix = []
max_sum = float("-inf")

for _ in range(row):
    matrix.append([int(el) for el in input().split(", ")])

# 0, 0     0, 1
# 1, 0     1, 1
square_line_one = None
square_line_two = None

for row_idx in range(row - 1):
    for col_idx in range(col - 1):
        current_element = matrix[row_idx][col_idx]
        next_element = matrix[row_idx][col_idx + 1]
        beneath_element = matrix[row_idx + 1][col_idx]
        diagonal_element = matrix[row_idx + 1][col_idx + 1]

        sum_of_current_square = sum([current_element, next_element, beneath_element, diagonal_element])

        if sum_of_current_square > max_sum:
            max_sum = sum_of_current_square
            square_line_one = [current_element, next_element]
            square_line_two = [beneath_element, diagonal_element]


print(*square_line_one)
print(*square_line_two)
print(max_sum)