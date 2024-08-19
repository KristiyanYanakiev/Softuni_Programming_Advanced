line = input().split("|")

sub_lists = []

# for el in line[::-1]:
#     sub_lists.extend(el.split())
#
# print(*sub_lists)

for el in line[::-1]:
    sub_lists.append(el.split())

[print(*row, end=" ") for row in sub_lists]







