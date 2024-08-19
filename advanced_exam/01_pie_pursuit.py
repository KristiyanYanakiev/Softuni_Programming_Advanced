from collections import deque

pieces_per_contestant = deque([int(x) for x in input().split()])
pieces_per_pie = [int(x) for x in input().split()]

while pieces_per_contestant and pieces_per_pie:
    contestant_capacity = pieces_per_contestant.popleft()
    pie = pieces_per_pie.pop()

    if contestant_capacity >= pie:
        contestant_capacity -= pie

        if contestant_capacity > 0:
            pieces_per_contestant.append(contestant_capacity)

    else:
        pie -= contestant_capacity

        if pie > 1:
            pieces_per_pie.append(pie)
        elif pie == 1:
            if pieces_per_pie:
                pieces_per_pie[-1] += pie
            else:
                pieces_per_pie.append(pie)

if not pieces_per_pie and pieces_per_contestant:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join([str(c) for c in pieces_per_contestant])}")

elif not pieces_per_pie and not pieces_per_contestant:
    print("We have a champion!")

elif not pieces_per_contestant and pieces_per_pie:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join([str(p) for p in pieces_per_pie])}")

