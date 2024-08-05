num = int(input("Give a number: "))

# number = num
# if not num > 0:
# 	print("Number 0 Is Not Larger Than 0")
# else:
# 	while number > 1:
# 		print(number - 1)
# 		number -= 1
# 	print(f"{num} numbers printed successfully.")

for number in range(num, 1, -1):
	print(number - 1)
print(f"{num} numbers printed successfully.")