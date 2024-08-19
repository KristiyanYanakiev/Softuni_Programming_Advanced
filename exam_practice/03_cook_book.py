def cookbook(*tuples_of_data):
    cuisines = set()
    data = {}

    for tuple in tuples_of_data:
        cuisines.add(tuple[1])

    for cuisine in cuisines:
        for tuple in tuples_of_data:
            if tuple[1] == cuisine:
                recipe = tuple[0]
                list_of_ingredients = tuple[2]
                if cuisine not in data.keys():
                    data[cuisine] = {recipe: list_of_ingredients}
                else:
                    data[cuisine].update({recipe: list_of_ingredients})


    for key, value in data.items():
        sorted_value = dict(sorted(value.items()))
        data[key] = sorted_value

    print(data)

    result = dict(sorted(data.items(), key=lambda x: (-len(x[1]), x[0])))

    output = ""

    for cuisine, recipes in result.items():
        output += f"{cuisine} cuisine contains {len(recipes)} recipes:\n"
        for recipe_name, ingredients in recipes.items():
            output += f"  * {recipe_name} -> Ingredients: {', '.join(str(i) for i in ingredients)}\n"

    return output

