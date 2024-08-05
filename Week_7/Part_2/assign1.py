my_nums = [15, 81, 5, 17, 20, 21, 13]

my_nums.sort(reverse = True)
no_reminder = 1
for num in my_nums:
	if num % 5 == 0:
		print(f"{no_reminder} => {num}")
		no_reminder += 1
print("All numbers Printed")