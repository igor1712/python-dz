# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.
# Пример:
# Для n = 6 -> 14.072


# def f(n):
#     lst = []
#     result = None
#     for i in range(1,n+1):
#         result = (1+1/i)**i
#         lst.append(result)

#     print(round(sum(lst),3))       


# n = int(input('Введите число: '))
# f(n)


n = int(input('Введите число: '))
lst = [round(((1 + 1 / i)**i), 3) for i in range(1, n + 1)]
print()
print(f"Сумма чисел последовательности равна: {sum(lst)}")
