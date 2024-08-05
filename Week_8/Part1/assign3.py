def show_skills(name, *skills):
	if skills:
		print(f"Hello {name.capitalize()} your skills are: ")
		for skill in skills:
			print(f"- {skill.capitalize()}")
	else:
		print(f"Hello {name.capitalize()}, you have no skills")

show_skills('Ahmed', 'python', 'css', 'html')