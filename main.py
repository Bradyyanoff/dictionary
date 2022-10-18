word_file = open("WordFile.txt", 'r')
word_lines = word_file.readlines()
word_counts = {'the': 0}
for word_line in word_lines:
    list_of_words = word_line.split(" ")
    for current_word in list_of_words:
        current_word = current_word.lower()
        current_word = current_word.strip()
        if word_counts.get(current_word):
            word_counts[current_word] += 1
            # same as word_counts[current_word] = word_counts[current_word]+1
        else:
            word_counts[current_word] = 1
print(word_counts)
