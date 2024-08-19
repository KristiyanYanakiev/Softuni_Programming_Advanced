def func_executor(*args):
    result = ""
    function_name = ""
    function_result = None
    for arg in args:
        function_name = arg[0].__name__
        function_result = arg[0](*arg[1])

        result += f"{function_name} - {function_result}\n"

    return result


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))