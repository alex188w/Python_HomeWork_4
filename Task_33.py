# 33.	Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k и приравняйте его к нулю. Пример:
# 1.	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x²  = 0
# 2*x**2 + 4*x + 5 = 0 или 2*x^2 + 4*x + 5 = 0

from random import randint
import itertools

k = randint(2, 5)
print(f'k = {k}')

def get_ratios(k):
    ratios = [randint(0, 101) for i in range (k + 1)]
    return ratios

def get_polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
                                                    # zip_longest() работает до последней итерации, пропущенные элементы заполняются fillvalue
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial)) # itertools.chain - объединяет списки
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x') # "".join - объединение списка строк (конвертация в строку)

ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(polynom1)

with open('Polynomial_1.txt', 'w') as data:
    data.write(polynom1)


# Второй многочлен для следующей задачи:

k = randint(2, 5)

ratios = get_ratios(k) 
polynom2 = get_polynomial(k, ratios)
print(polynom2)

with open('Polynomial_2.txt', 'w') as data:
    data.write(polynom2)