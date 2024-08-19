from collections import deque

money_sequence_stack = [int(x) for x in input().split()]

prices_sequence_deque = deque([int(i) for i in input().split()])

eaten_food = 0

while money_sequence_stack and prices_sequence_deque:
    current_money = money_sequence_stack.pop()
    current_price = prices_sequence_deque.popleft()

    if current_price == current_money:
        eaten_food += 1

    elif current_money > current_price:
        if money_sequence_stack:
            money_sequence_stack[-1] += current_money - current_price
        eaten_food += 1


    elif current_money < current_price:
        pass


if eaten_food >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food} foods.")
elif eaten_food > 0 and eaten_food != 4:
    if eaten_food == 1:
        print(f"Henry ate: {eaten_food} food.")
    else:
        print(f"Henry ate: {eaten_food} foods.")

elif eaten_food == 0:
    print("Henry remained hungry. He will try next weekend again.")




