excepion_list = [6, 8, 12]
for number in range(1, 21):
	if number in excepion_list: pass
	else: print(str(number).zfill(2))