write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "H")
print(nb_characters)