from collections import deque

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

collected_colors = []

criteria_of_secondary_colors ={
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}

substrings = deque(input().split())

while substrings:
    first_sub_string = substrings.popleft()
    second_sub_string = substrings.pop() if substrings else ""

    for result in (first_sub_string + second_sub_string, second_sub_string + first_sub_string):
        if result in main_colors or result in secondary_colors:
            collected_colors.append(result)
            break
    else:
        idx = len(substrings) // 2
        for el in (first_sub_string[:-1], second_sub_string[:-1]):
            substrings.insert(idx, el)

for color in collected_colors:
    if color in criteria_of_secondary_colors.keys():
        if set(collected_colors).issuperset(criteria_of_secondary_colors[color]):
            continue
        else:
            collected_colors.remove(color)

print(collected_colors)











