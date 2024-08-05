import random

num1 = random.randint(10, 50)
num2 = random.choice([i for i in range(2, 11, 2)])
num3 = random.choice([i for i in range(1, 10, 2)])

print(f'Random Number Between 10 And 50 => {num1}')
print(f'Random Even Number Between 2 And 10 => {num2}')
print(f'Random Odd Number Between 1 And 9 => {num3}')
print(dir(random))