n = int(input())

guest_list = set()
for _ in range(n):
    name = input()
    guest_list.add(name)


command = input()

while command != "END":
    if command in guest_list:
        guest_list.remove(command)

    command = input()

print(len(guest_list))
print(*sorted(guest_list), sep="\n")