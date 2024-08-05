'''This module is the 5th assign in Week 12 part 1'''

my_friends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_people) -> list:
    '''This func is to say hello to somepeople'''
    for someone in some_people:
        print(f"Hello {someone}")

say_hello(my_friends)
