from collections import deque

initial_fuel = [int(x) for x in input().split()]
consumption_index = deque([int(x) for x in input().split()])

needed_fuel_for_altitude = deque([int(x) for x in input().split()])

needed_fuel_for_altitude_copy = needed_fuel_for_altitude.copy()

reached_altitudes = []
failed_altitudes = []

for current_altitude in range(1, len(needed_fuel_for_altitude_copy) + 1):
    result = initial_fuel.pop() - consumption_index.popleft()
    altitude = needed_fuel_for_altitude.popleft()

    if result >= altitude:
        reached_altitudes.append(altitude)
        print(f"John has reached: Altitude {current_altitude}")
    else:
        failed_altitudes.append(altitude)
        print(f"John did not reach: Altitude {current_altitude}")
        break


if reached_altitudes and failed_altitudes:
    print("John failed to reach the top.")
    res = "Reached altitudes: "
    for al in range(1, len(reached_altitudes) + 1):
        res += f"Altitude {al}, "
    print(res[:-2])


elif not reached_altitudes:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")

elif len(reached_altitudes) == len(needed_fuel_for_altitude):
    print("John has reached all the altitudes and managed to reach the top!")


if reached_altitudes and not failed_altitudes:
    print("John has reached all the altitudes and managed to reach the top!")