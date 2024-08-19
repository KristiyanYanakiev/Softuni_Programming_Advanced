from collections import deque

quantity_of_food = int(input())

orders_queue = deque([int(element) for element in input().split()])

print(max(orders_queue))

for _ in range(len(orders_queue)):
    if orders_queue[0] <= quantity_of_food:
        quantity_of_food -= orders_queue[0]
        orders_queue.popleft()
    else:
        left_orders = " ".join([str(i) for i in orders_queue])
        print(f"Orders left: {left_orders}")
        break

else:
    print("Orders complete")