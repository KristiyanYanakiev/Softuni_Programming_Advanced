def concatenate(*args, **kwargs):
    text = ""
    for word in args:
        text += word

    for key in kwargs:
        text = text.replace(key, kwargs[key])

    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))