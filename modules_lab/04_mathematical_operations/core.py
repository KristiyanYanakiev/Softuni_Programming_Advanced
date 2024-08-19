def division(num1, num2):
    while True:
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("Division by zero not possible")
            try:
                num2 = int(input("please try enter the second number again: "))
            except ValueError:
                num2 = int(input("please enter the second number again: "))

def math_operations(num1, num2, sign):
    operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "^": lambda x, y: x ** y,
    "/": division
}

    res = operations[sign](num1, num2)
    return f"{res:.2f}"