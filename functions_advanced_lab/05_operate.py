from functools import reduce

# operators = {
#     "+": lambda x, y: x + y,
#     "-": lambda x, y: x - y,
#     "*": lambda x, y: x * y,
#     "/": lambda x, y: x // y
# }


def operate(operator, *args):
    result = 0

    if operator == "+":
        result = 0
        for num in args:
            result += num

    elif operator == "-":
        result = 0
        for num in args:
            result -= num

    elif operator == "*":
        result = 1
        for num in args:
            result *= num

    elif operator == "/":
        result = 1
        for num in args:
            if num != 0:
                result /= num

    return result



print(operate("*", 3, 4))