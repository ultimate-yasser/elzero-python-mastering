def addition(*numbers):
	summation = 0
	for number in numbers:
		if number == 10:
			pass
		elif number == 5:
			summation -= 5
		else:
			summation += number
	return summation

print(addition(5, 10, 5, 15, 10))