from collections import deque

list_of_waiting_clients = deque([])

command = input()

while command != "End":
    if command == "Paid":
        while list_of_waiting_clients:
            print(list_of_waiting_clients.popleft())
    else:
        client_name = command
        list_of_waiting_clients.append(client_name)

    command = input()

print(f"{len(list_of_waiting_clients)} people remaining.")



