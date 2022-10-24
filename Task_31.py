# 31.	Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N. 70 = 2*5*7 => [2, 5, 7]

import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()

number = input("Введите натуральное число: ")
if number.isdigit() == False:
    print('Введенное значение не является натуральным чисом')
    exit()

number = int(number)


def Factor(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    print(ans)


Factor(number)
