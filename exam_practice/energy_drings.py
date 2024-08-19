from collections import deque

caffeine = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])

MAX_CAFFEINE = 300

current_caffeine = 0

while caffeine and energy_drinks:
    coffee = caffeine.pop()
    drink = energy_drinks.popleft()
    caffeine_in_the_drink = coffee * drink

    if caffeine_in_the_drink + current_caffeine <= MAX_CAFFEINE:
        current_caffeine += caffeine_in_the_drink

    else:
        energy_drinks.append(drink)
        current_caffeine -= 30
        if current_caffeine < 0:
            current_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(i) for i in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {current_caffeine} mg caffeine.")







