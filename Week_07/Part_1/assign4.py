my_friends = []

while len(my_friends) < 4:
	friend = input("Friend name: ").strip()
	if friend.isupper():
		print("Invalid name")
	elif friend.islower():
		my_friends.append(friend.upper())
		print("First letter capitalized...")
	else:
		my_friends.append(friend)
	
	print(f"Friends left {4-len(my_friends)}")
else:
	print("List is full")
