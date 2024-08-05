letter = input('Enter a char from A -> Z: ')

try:
    if len(letter) > 1:
        raise IndexError
    elif not letter.isupper():
        raise NameError
except IndexError:
    print('"You Must Write One Character Only"')
except NameError:
    print("The Letter Not In A - Z")
else: 
    print('You typed', letter)