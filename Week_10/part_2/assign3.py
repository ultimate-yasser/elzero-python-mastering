from functools import reduce

def mul(num1, num2):
    return num1 * num2

nums = [2, 4, 6, 2]

total_1 = reduce(mul, nums)
print(total_1)
print('#' * 50)

total_2 = reduce(lambda num1, num2:num1* num2, nums)
print(total_2)