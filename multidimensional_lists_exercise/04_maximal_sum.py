def take_data(text):
    return [int(x) for x in text.split()]

r, c = take_data(input())
matrix = []

biggest_sum = float("-inf")
sub_matrix = []
for _ in range(r):
    matrix.append(take_data(input()))

for r_idx in range(r - 2):
    for c_index in range(c - 2):
        first_row = matrix[r_idx][c_index:c_index + 3]
        second_row = matrix[r_idx + 1][c_index:c_index + 3]
        third_row = matrix[r_idx + 2][c_index:c_index + 3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            sub_matrix = [first_row, second_row, third_row]

print( *("Sum =", biggest_sum))
[print(*row) for row in sub_matrix]






