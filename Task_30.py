# 	Задача 30. Вычислить число π c заданной точностью d. Пример: при d = 0.001, π = 3.141 10^(-1)≤d≤10^(-10)

# !!! Задание преподавателя на семинаре: вывести заданное количесвто знаков после запятой числа Пи,
# остальное отбросить! Пример: при d = 0.001, π = 3.141 (при округлении будет 3,142). Результат должен быть числом.
import os
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()
precis = input("Введите необходимую точночть числа Пи: ")
if precis.isdigit() == False:
    print('Введенное значение не может быть переведено')
    exit()

precis = int(precis)

import math

num_pi = str(math.pi)
b = str(num_pi)[:precis+2]
print(f'Число пи, строка: {b}')
c = float(b)
print(f'Число пи, число float: {c}')

