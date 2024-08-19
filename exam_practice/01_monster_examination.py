from collections import deque

monsters_armors = deque([int(x) for x in input().split(",")])
soldier_strikes = [int(x) for x in input().split(",")]

killed_monsters = 0

while monsters_armors and soldier_strikes:
    strike = soldier_strikes.pop()
    armor = monsters_armors.popleft()

    if strike >= armor:
        remaining_striking_impact = strike - armor
        if soldier_strikes:
            soldier_strikes[-1] += remaining_striking_impact
        else:
            if remaining_striking_impact:
                soldier_strikes.append(remaining_striking_impact)

        killed_monsters += 1
    else:
        armor -= strike
        monsters_armors.append(armor)

if not monsters_armors:
    print("All monsters have been killed!")

if not soldier_strikes:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")





