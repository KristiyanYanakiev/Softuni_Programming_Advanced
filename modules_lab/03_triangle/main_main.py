def col_data_in_triangle(r):
    for col in range(1, r + 1):
        print(col, end=" ")
    print()

def top_half(size):
    for row in range(1, size + 1):
        col_data_in_triangle(row)



def lower_halp(size):
    for row in range(size - 1, 0, -1):
        col_data_in_triangle(row)


def draw_triangle(size):
    top_half(size)
    lower_halp(size)

