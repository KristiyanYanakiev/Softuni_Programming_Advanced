from math import log

number = int(input())
try:
    base = int(input())
    res = log(number, base)
except ValueError:
    res = log(number)

print(f"{res:.2f}")

