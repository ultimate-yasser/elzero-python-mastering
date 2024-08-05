skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

for counter, skill in enumerate(reversed(skills), 50):
    if type(skill) == int: continue
    print(f'{counter} - {skill}')

print('#' * 50)

counter = 50

for skill in reversed(skills):
    if type(skill) == int:
        counter += 1
        continue
    print(f'{counter} - {skill}')
    counter += 1
