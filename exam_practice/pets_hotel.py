def accommodate_new_pets(capacity, weight_limit, *tuples):
    pets = {}
    out_of_space = False

    for tuple in tuples:
        pet_type = tuple[0]
        pet_weight = tuple[1]

        if capacity == 0:
            out_of_space = True
            break

        if pet_weight <= weight_limit:
            capacity -= 1
            if pet_type not in pets.keys():
                pets[pet_type] = 0
            pets[pet_type] += 1
        else:
            continue



    output = ""
    total_accomodated_pets = 0

    for v in pets.values():
        total_accomodated_pets += v

    if not out_of_space:
        output = f"All pets are accommodated! Available capacity: {capacity}.\n"
    else:
        output = "You did not manage to accommodate all pets!\n"

    sorted_pets = dict(sorted(pets.items(), key=lambda x: x[0]))

    output += "Accommodated pets:\n"

    for p, n in sorted_pets.items():
        output += f"{p}: {n}\n"

    return output[:-1]



print(accommodate_new_pets(
    0,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))