import os

dir_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir_path)

for i in range(1, 51):
    if i == 25:
        file = open('special-text.txt', 'w')
    else:
        file = open(f'txt{i}.txt', 'w')
        file.write(f'Elzero web school => {i}\n')
    file.close()
    print(os.getcwd())
    print(dir_path)
    print(os.path.abspath(__file__))
    print(len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))]))
    
