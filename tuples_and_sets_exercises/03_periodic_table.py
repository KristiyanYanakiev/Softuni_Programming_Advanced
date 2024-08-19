n = int(input())

periodic_table = set()

for _ in range(n):
    els = input().split()
    for el in els:
        periodic_table.add(el)

print(*periodic_table, sep="\n")

