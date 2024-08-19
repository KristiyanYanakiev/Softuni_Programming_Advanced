import os

try:
    os.remove("my_first_file_txt")
except:
    print("File already deleted!")