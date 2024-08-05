def my_all(iterable):
    falses = [0, [], '', ()]
    if iterable == [] or iterable == ():
        return False
    for element in iterable:
        if element in falses:
            return False
    
    return True

def my_any(iterable):
    falses = [0, [], '', ()]
    if iterable == [] or iterable == ():
        return False
    for element in iterable:
        if element not in falses:
            return True
    
    return False

def my_min(iterable):
    minimal = iterable[0]
    for num in iterable[0:]:
        if minimal > num:
            minimal = num
    return minimal

def my_max(iterable):
    maximum = iterable[0]
    for number in iterable[0:]:
        if maximum < number:
            maximum = number

    return maximum


# my_all
print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False

# my_any
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False

# my_min
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100

# my_max
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700