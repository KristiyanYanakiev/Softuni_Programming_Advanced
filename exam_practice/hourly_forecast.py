def forecast(*args):
    data = {}

    for tuple in args:
        location = tuple[0]
        weather = tuple[1]

        if weather not in data.keys():
            data[location] = weather



    desired_order = ["Sunny", "Cloudy", "Rainy"]

    sorted_data = dict(sorted(data.items(), key=lambda x: (desired_order.index(x[1]), x[0])))



    output = ""
    for loc, w in sorted_data.items():

        output += f"{loc} - {w}\n"

    return output[:-1]


