

'''Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''

# lst = [2, 3, 5, 9, 3]
# sum_ = 0
# for i in range(1,len(lst),2):
#     sum_ += lst[i]
# print(f'Сумма элементов на не четных позициях = {sum_}.')


lst = [2, 3, 5, 9, 3]
lst_1 = [lst[i] for i in range(len(lst)) if  i % 2 != 0  ]
print(f'Сумма на не чет позциях = {sum(lst_1)}')