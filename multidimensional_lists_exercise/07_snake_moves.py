from collections import deque

n, m = [int(x) for x in input().split()]

snake = deque(input())

snake_copy = snake.copy()

matrix = []

for row in range(n):
    while len(snake_copy) < m:
        snake_copy.extend(snake)

    current_content = [snake_copy.popleft() for _ in range(m)]
    if row % 2 != 0:
        current_content = current_content[::-1]

    matrix.append(current_content)



[print(*i, sep="") for i in matrix]
