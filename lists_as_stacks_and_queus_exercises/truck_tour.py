# from collections import deque
#
# number_of_pumps = int(input())
# list_pumps = []
#
# for _ in range(number_of_pumps):
#     command = input().split()
#     kilometers = int(command[0])
#     distance = int(command[1])
#
#     data = [kilometers, distance]
#     list_pumps.append(data)
#
# pumps = deque(list_pumps)
#
# pumps_copy = pumps.copy()
# fuel = 0
# starting_point = 0
# # write algorithm
#
# while pumps_copy:
#     petrol, distance_to_next = pumps_copy.popleft()
#
#     fuel += petrol
#
#     if fuel >= distance_to_next:
#         fuel -= distance_to_next
#     else:
#         pumps.rotate(-1)
#         pumps_copy = pumps.copy()
#         starting_point += 1
#         fuel = 0
#
# print(starting_point)


#Solution with indexing of the deque:

from collections import deque

number_of_pumps = int(input())
list_pumps = []

for _ in range(number_of_pumps):
    command = input().split()
    kilometers = int(command[0])
    distance = int(command[1])

    data = [kilometers, distance]
    list_pumps.append(data)

pumps = deque(list_pumps)

fuel = 0
starting_point = 0






