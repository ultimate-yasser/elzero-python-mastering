def reverse_string(name):
    for char in name[::-1]:
        yield char

for c in reverse_string('Yasser'):
    print(c)
