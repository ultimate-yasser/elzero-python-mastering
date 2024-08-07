country = input("What is your country: ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100

if country in countries:
	discount = .30
	print(f"You have a discount of %{discount * 100}")
	print(f"The price u have to pay is {price * (1 - discount)}")
	
else: print(f"There is no discount 4U so the price is {price}")