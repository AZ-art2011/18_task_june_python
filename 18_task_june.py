# Задача 18. Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.

import random
from random import randint

count_n = abs(int(input('Укажите число элементов списка: ')))
find_element = abs(int(input('Укажите искомое число: ')))
range_random = abs(int(input('Укажите верхнюю границу для генератора случайных чисел: ')))
elements_of_list = [randint(1, range_random) for x in range(1, count_n + 1)]
check_list = [abs(x - find_element) for x in elements_of_list]
min_digits = min(check_list)

neighbors = []

for i, j in enumerate(check_list):
    if j == min_digits:
        neighbors.append(elements_of_list[i])

print(f'Случайные числа: {elements_of_list}')
print(f'Минимальная дельта между элементами {min_digits} и ближайшее число (числа) {set(neighbors)}')



