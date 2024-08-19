import re

file = open("words.txt", "r")

searched_words = (file.read()).split()
text_file = open("../file_handling_exercise/text.text", "r")

content = text_file.read().lower()

word_count = {}

for word in searched_words:
    pattern = re.compile(rf"\b{word}\b")
    results = re.findall(pattern, content)

    word_count[word] = results.count(word)

sorted_word_count = sorted(word_count.items(), key=lambda x: -x[1])

for k, v in sorted_word_count:
    print(f"{k} - {v}")
