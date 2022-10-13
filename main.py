word_file = open("WordFile.txt", 'r')
word_lines = word_file.readlines()
for word_line in word_lines:
    list_of_words = word_line.split(" ")
    print(list_of_words)