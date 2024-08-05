def get_names(name):
    return name[-1] == 'm'

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

names1 = filter(get_names, friends_filter)

for name in names1:
    print(name)

print('#' * 50)

names2 = filter(lambda name: name[-1] == 'm', friends_filter)

for name in names2:
    print(name)