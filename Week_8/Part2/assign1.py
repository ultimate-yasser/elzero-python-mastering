def get_score(**mydictionary):
	for subject, score in mydictionary.items():
		print(f"{subject.title()} => {score}")

get_score(Math=90, Science=80, Language=70)