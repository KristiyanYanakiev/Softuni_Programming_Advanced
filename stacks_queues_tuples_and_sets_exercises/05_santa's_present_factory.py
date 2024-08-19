from collections import deque

boxes_with_materials = [int(x) for x in input().split()]
magic_values = deque(int(x) for x in input().split())

crafted_presents = []

present_magic_ratio = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while boxes_with_materials and magic_values:
    current_box_with_material = boxes_with_materials.pop()
    current_magic_level = magic_values.popleft()

    total_magic = current_box_with_material * current_magic_level

    if total_magic in present_magic_ratio.keys():
        toy = present_magic_ratio[total_magic]
        crafted_presents.append(toy)

    else:

        if current_box_with_material == 0 and current_magic_level != 0:
            magic_values.appendleft(current_magic_level)
            continue

        elif current_magic_level == 0 and current_box_with_material != 0:
            boxes_with_materials.append(current_box_with_material)
            continue

        elif current_magic_level == 0 and current_box_with_material == 0:
            continue

        if total_magic < 0:
            sum_of_two = current_box_with_material + current_magic_level
            boxes_with_materials.append(sum_of_two)

        elif total_magic > 0:
            boxes_with_materials.append(current_box_with_material + 15)

if {"Doll", "Wooden train"}.issubset(crafted_presents) or {"Teddy bear", "Bicycle"}.issubset(crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes_with_materials:
    print(f"Materials left: {', '.join([str(i) for i in boxes_with_materials[::-1]])}")

if magic_values:
    print(f"Magic left: {', '.join([str(i) for i in magic_values])}")

if crafted_presents:
    for present in sorted(set(crafted_presents)):
        print(f"{present}: {crafted_presents.count(present)}")

# Continue by studying the 