age = int(input("What's ur age: ").strip())

if age < 16:
	print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else:
	print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")