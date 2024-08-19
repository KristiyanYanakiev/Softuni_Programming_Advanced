n = int(input())

biggest_intersection = set()

for _ in range(n):
    ranges = input().split("-")
    first_range = ranges[0].split(",")
    second_range = ranges[1].split(",")

    first_set = {num for num in range(int(first_range[0]), int(first_range[1]) + 1)}
    second_set = {num for num in range(int(second_range[0]), int(second_range[1]) + 1)}
    current_intersection = first_set.intersection(second_set)
    if len(current_intersection) > len(biggest_intersection):
        biggest_intersection = current_intersection


print(f'Longest intersection is [{", ".join(str(i) for i in biggest_intersection)}] with length {len(biggest_intersection)}')

