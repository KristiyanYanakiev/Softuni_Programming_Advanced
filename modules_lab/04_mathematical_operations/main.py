from core import math_operations

text = input()

n1 = float(text.split()[0])
n2 = int(text.split()[2])
sign = text.split()[1]

print(math_operations(n1, n2, sign))
