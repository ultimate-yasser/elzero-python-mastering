def calculate(num1, num2, operation = 'a'):
	operation = operation.lower()
	if operation == 'add' or operation == "a":
		print(f"{num1} + {num2} = {num1 + num2}")
	elif operation == 'sub' or operation == 's':
		print(f"{num1} - {num2} = {num1 - num2}")
	elif operation == 'mul' or operation == 'm':
		print(f"{num1} X {num2} = {num1 * num2}")
	else:
		print("Invalid operation")

calculate(2, 3, 'MuL')