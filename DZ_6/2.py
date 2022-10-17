
# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# def sum_(num):
#     number = 0
#     for i in num:
#         if i != ',' and i != '-':
#             number += int(i)
#     print(number)

# num = input("Введите число: ")
# sum_(num)


num = input('Введите вещественное число: ')
lst = [int(x) for x in num if x.isdigit()]
print('сумма элементов числа равна: ', sum(lst))