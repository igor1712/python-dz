# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.

from random import randint, random


n = int(input('Введите диапозон листа: '))
a = int(input('Введите позицию а: '))
b = int(input('Введите позицию b: '))

def f(n,a,b):
    lst = []
    for i in range(n):
            lst.append(randint(-10,15))
    print(lst)
    sum = lst[a] * lst[b]
    print(f'сумма позиций a and b =  {sum};')


f(n,a,b)