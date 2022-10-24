# 32.	Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности

import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()


def random_list(n):
    import random
    list = []
    for i in range(n):
        num = random.randint(0, 10)
        list.append(num)
    return list


def unique_nums(nums):
    unique = []

    for num in nums:
        if num in unique:
            continue
        else:
            unique.append(num)
    return unique


my_list = random_list(7)
print(f'Исходный сисок: {my_list}')
print(f'Спиоок неповторяющихся элементов {unique_nums(my_list)}')
