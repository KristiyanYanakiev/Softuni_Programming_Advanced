from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque(int(x) for x in input().split(", "))

prepared_milkshakes = 0

while prepared_milkshakes < 5 and chocolates and cups_of_milk:
    current_chocolate = chocolates.pop()
    current_cup_of_milk = cups_of_milk.popleft()

    if current_chocolate <= 0 < current_cup_of_milk:
        cups_of_milk.appendleft(current_cup_of_milk)
        continue
    elif current_cup_of_milk <= 0 < current_chocolate:
        chocolates.append(current_chocolate)
        continue
    elif current_cup_of_milk <= 0 and current_chocolate <= 0:
        continue

    if current_chocolate == current_cup_of_milk:
        prepared_milkshakes += 1

    else:
        cups_of_milk.append(current_cup_of_milk)
        chocolates.append(current_chocolate - 5)


print("Great! You made all the chocolate milkshakes needed!" if prepared_milkshakes == 5 else "Not enough milkshakes.")

print(f"Chocolate: {', '.join([str(i) for i in chocolates])}" if chocolates else "Chocolate: empty")

print(f"Milk: {', '.join([str(i) for i in cups_of_milk])}" if cups_of_milk else "Milk: empty")



