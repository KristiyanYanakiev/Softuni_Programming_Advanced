import os

example = open("../file_handling_exercise/text.text", "r")

path = os.path.join("..", "exam_practice", "file_handling_practice")
another_file = open(path, "w")

#another_file = open("../exam_practice/file_handling_practice", "w")


another_file.write("Here is the second example")

