friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
exceeded_friends = 0
i = 0

while i < len(friends):
	if friends[i].istitle(): print(friends[i]) 
	else: exceeded_friends += 1
	i += 1
print(f"The number of exceeded friends => {exceeded_friends}")