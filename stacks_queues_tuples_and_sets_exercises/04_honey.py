from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0

functions = {"+": lambda a, b: abs(a + b),
             "-": lambda a, b: abs(a - b),
             "*": lambda a, b: abs(a * b),
             "/": lambda a, b: abs(a / b) if b != 0 else 0,
}



while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= current_bee:
        symbol = symbols.popleft()
        total_honey += functions[symbol](current_bee, current_nectar)
    else:
        working_bees.appendleft(current_bee)

print(f"Total honey made: {total_honey}")


# print(f"Bees left: {', '.join([str(i) for i in working_bees])}" if working_bees else '')
# print(f"Nectar left: {', '.join([str(i) for i in nectar])}" if nectar else '')


if working_bees:
    print(f"Bees left: {', '.join([str(i) for i in working_bees])}")

if nectar:
    print(f"Nectar left: {', '.join([str(i) for i in nectar])}")





