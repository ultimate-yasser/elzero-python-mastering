num = input('Enter a number: ')

if len(num) > 1:
    raise IndexError('Only One Character Allowed')
elif num == '0':
    raise ValueError('Number Must Be Larger Than 0')
elif num.isalpha():
    raise Exception('Only numbers allowed')
else:
    num = int(num)
    print('#' * 50, f'The number is {num}', '#' * 50, sep='\n')
    
