def age_assignment(*args, **kwargs):
    new_dict = {}
    for key,value in kwargs.items():
        for name in args:
            if name.startswith(key):
                new_dict[name] = kwargs[key]

    result = "\n".join(f"{k} is {v} years old." for k, v in sorted(new_dict.items()))

    return result



print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))