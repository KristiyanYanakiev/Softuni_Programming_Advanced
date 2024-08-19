from collections import deque

line = deque([name for name in input().split()])

n_toss = int(input()) - 1

while len(line) > 1:
    line.rotate( - n_toss)
    name = line.popleft()
    print(f"Removed {name}")


print(f"Last is {line.popleft()}")




