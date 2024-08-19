n = int(input())

parking = set()

for _ in range(n):
    direction, car = input().split(", ")

    if direction == "IN":
        parking.add(car)
    else:
        if car in parking:
            parking.remove(car)

if parking:
    for car in parking:
        print(car)
else:
    print("Parking Lot is Empty")
