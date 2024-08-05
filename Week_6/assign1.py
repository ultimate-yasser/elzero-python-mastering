num1 = int(input("First number: ").strip())
num2 = int(input("Second number: ").strip())

operation = input("What do u wanna do with them? ").strip()

if operation == '+': print(f"{num1} {operation} {num2} = {num1 + num2}")
elif operation == '-': print(f"{num1} {operation} {num2} = {num1 - num2}")
elif operation == '*': print(f"{num1} {operation} {num2} = {num1 * num2}")
elif operation == '/': print(f"{num1} {operation} {num2} = {num1 / num2}")
elif operation == '%': print(f"{num1} {operation} {num2} = {num1 % num2}")
else: print("Wrong operation")