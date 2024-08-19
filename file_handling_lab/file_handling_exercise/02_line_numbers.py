from string import punctuation

with open("text.txt", "r") as text_file:

    output_file = open("output_file_number_two", "w")
    lines = text_file.readlines()

    for row in range(len(lines)):
        letters, punctuation_marks = 0, 0

        for element in lines[row]:
            if element.isalpha():
                letters += 1
            elif element in punctuation:
                punctuation_marks += 1

        output_file.write(f"Line {row + 1}: {''.join(lines[row])[:-1]} ({letters}), ({punctuation_marks})\n")
