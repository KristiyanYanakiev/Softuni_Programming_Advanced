from collections import deque

def fill_the_box(*args):
    cubes = deque(args)

    h = cubes.popleft()
    l = cubes.popleft()
    w = cubes.popleft()

    box_size = h * l * w

    while cubes[0] != "Finish":
        box_size -= cubes.popleft()

        if box_size < 0:
            cubes_left = sum(c for c in cubes if c != "Finish")
            return f"No more free space! You have {cubes_left + abs(box_size)} more cubes."

    return f"There is free space in the box. You could put {box_size} more cubes."




print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

