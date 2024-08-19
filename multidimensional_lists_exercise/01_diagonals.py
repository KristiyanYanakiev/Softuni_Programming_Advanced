rows = int(input())

matrix = [ [int(x) for x in input().split(", ")] for _ in range(rows)]

# with comprehensions:
primary_diagonal = [matrix[row_idx][row_idx] for row_idx in range(rows)]

secondary_diagonal = [matrix[row_idx][rows - row_idx - 1] for row_idx in range(rows)]


# for row_idx in range(rows):
#     el = matrix[row_idx][row_idx]
#     primary_diagonal.append(el)
#
#
# for r_idx in range(rows):
#     el = matrix[r_idx][rows - r_idx - 1]
#     secondary_diagonal.append(el)

print(f"Primary diagonal: {', '.join(str(i) for i in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(i) for i in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")









