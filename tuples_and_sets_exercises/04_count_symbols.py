text = input()

set_of_chars = set()

for i in text:
    set_of_chars.add(i)

for el in sorted(set_of_chars):
    print(f"{el}: {text.count(el)} time/s")
