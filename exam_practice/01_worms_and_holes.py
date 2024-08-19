from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

matches_count = 0
worm_length = len(worms)


while worms and holes:

    worm = worms.pop()
    if worm <= 0 and worms:
        worm = worms.pop()
    hole = holes.popleft()

    if worm == hole:
        matches_count += 1

    elif worm != hole:
        worm -= 3
        if worm > 0:
            worms.append(worm)

if matches_count:
    print(f"Matches: {matches_count}")
else:
    print("There are no matches.")

if not worms and matches_count and matches_count == worm_length:
    print("Every worm found a suitable hole!")
elif not worms and matches_count != worm_length:
    print("Worms left: none")
elif worms:
    print(f"Worms left: {', '.join([str(w) for w in worms])}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join([str(h) for h in holes])}")



