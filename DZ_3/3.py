'''Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

lst = [1.1, 1.2, 3.1, 5, 10.01]
print(lst, '\n')
max_ = 0
min_ = lst[0]

for i in range(len(lst)): 

    lst[i] -= int(lst[i])
    lst[i] = round(lst[i], 2)

    if lst[i] == 0:
        continue

    if max_ < lst[i]:
        max_ = lst[i]

    if min_ > lst[i]:
        min_ = lst[i]

r = max_ - min_    

print(lst, '\n')
print(f'{max_} - {min_} = {r}')   

