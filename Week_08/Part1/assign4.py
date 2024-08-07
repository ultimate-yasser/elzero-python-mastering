def say_hello(name = 'unknown', age = 'unknown', country = 'unknown'):
	return f"Hello {name.capitalize()} Your Age Is {age} And You Live In {country.capitalize()}"

print(say_hello('aHmed', 19, 'egypt'))