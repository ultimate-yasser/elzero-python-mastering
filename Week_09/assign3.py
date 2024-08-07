file = open('txt1.txt', 'r')
file_lines = file.readlines()
words_count = 0
chars_count = 0
char_l = 0
for line in file_lines:
    words = line.split()
    words_count += len(words)
    for word in words:
        chars_count += len(word)
        for char in word:
            if char == 'l':
                char_l += 1

print(len(file_lines))
print(words_count)
print(chars_count)
print(char_l)
