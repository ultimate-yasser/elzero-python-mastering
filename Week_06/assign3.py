age = int(input("Your age: ").strip())


if age > 10 and age < 100:
	months = age * 12
	weeks = age * 51
	days = age * 365
	hours = days * 24
	minutes = hours * 60
	seconds = minutes * 60

	print(f"Ur age in Months is {months:,}")
	print(f"Ur age in Weeks is {weeks:,}")
	print(f"Ur age in Days is {days:,}")
	print(f"Ur age in Hours is {hours:,}")
	print(f"Ur age in Minutes is {minutes:,}")
	print(f"Ur age in Seconds is {seconds:,}")

else: print("Age out of range")
