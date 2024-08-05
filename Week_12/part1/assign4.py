def say_hello(name) -> str:
    '''This function says hello to the name'''
    return f"Hello {name.title()}"

print(say_hello('yasser'))
print(say_hello.__doc__)