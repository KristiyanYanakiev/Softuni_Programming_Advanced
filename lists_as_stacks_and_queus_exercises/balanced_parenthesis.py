def pairing_parenthesis(opening_parenthesis, closing_parenthesis):
    if opening_parenthesis == "(" and closing_parenthesis == ")":
        return True
    elif opening_parenthesis == "{" and closing_parenthesis == "}":
        return True
    elif opening_parenthesis == "[" and closing_parenthesis == "]":
        return True
    else:
        return False



sequence_of_parenthesis = input()
stack_of_opened = []

opening = ["(", "{", "["]
closing = [")", "}", "]"]

balance = False

for i in sequence_of_parenthesis:
    if i in opening:
        stack_of_opened.append(i)
    else:
        if stack_of_opened:
            last_opening = stack_of_opened.pop()
            if pairing_parenthesis(last_opening, i):
                balance = True



if not stack_of_opened and balance:
    print("YES")
else:
    print("NO")





















