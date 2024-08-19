from collections import deque

time_for_task = deque([int(x) for x in input().split()])
tasks = [int(x) for x in input().split()]


task_values = {
    range(0, 61): "Darth Vader Ducky",
    range(61, 121): "Thor Ducky",
    range(121, 181): "Big Blue Rubber Ducky",
    range(181, 241): "Small Yellow Rubber Ducky"
}

ducks = {}


while tasks:
    time = time_for_task.popleft()
    task = tasks.pop()

    res = time * task

    for range, duck_name in task_values.items():
        if duck_name not in ducks.keys():
            ducks[duck_name] = 0
        if res in range:
            ducks[duck_name] += 1
    if res > 240:
        task -= 2
        tasks.append(task)
        time_for_task.append(time)

desired_order = ['Darth Vader Ducky', 'Thor Ducky', 'Big Blue Rubber Ducky', 'Small Yellow Rubber Ducky']

sorted_ducks = dict(sorted(ducks.items(), key=lambda x: desired_order.index(x[0])))


print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for k, v in sorted_ducks.items():
    print(f"{k}: {v}")
