def get_people_scores(name = '', **scores):
	if name:
		if scores:
			print(f"Hello {name.capitalize()}, this is your score table: ")
			for subject, score in scores.items():
				print(f"{subject.capitalize()} => {score}")
		else:
			print(f"Hello {name.capitalize()}, You have no scores to show...")
	else:
		for subject, score in scores.items():
				print(f"{subject.capitalize()} => {score}")
