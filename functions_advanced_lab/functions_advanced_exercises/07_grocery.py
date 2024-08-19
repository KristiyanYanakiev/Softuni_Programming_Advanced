def grocery_store(**kwargs):
    result = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    # final = ""
    # for element in result:
    #     final += f"{element[0]}: {element[1]}\n"

    final = "\n".join(f"{product}: {quantity}" for product, quantity in result)

    return final


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))