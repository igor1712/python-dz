'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]'''

from copy import copy


num = int(input('Введите число: '))
sum = 1
j = 0
lst = [0,1]

for i in range(num - 1):

    j, sum = -sum, - j + (-sum)
    lst.append(sum)
    num -= 1

lst.reverse()    


num_1 = copy(num)
sum_1 = 1
j_1 = 0
lst_1 = [1]

for i in range(len(lst) - 2):
    
    j_1, sum_1 = sum_1, j_1 + sum_1
    lst_1.append(sum_1)
    num_1 -= 1

lst_1 = lst + lst_1

print(lst_1 )
