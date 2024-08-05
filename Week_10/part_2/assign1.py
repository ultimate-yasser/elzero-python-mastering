def remove_chars(text):
    return text[1:-1]

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_list1 = map(remove_chars, friends_map)
for name in cleaned_list1:
    print(name)

print('#' * 50)

cleaned_list2 = map(lambda text: text[1:-1], friends_map)

for name in cleaned_list2:
    print(name)
