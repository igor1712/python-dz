
# Задание 5 Реализуйте алгоритм перемешивания списка.
from random import randint, randrange

test_list = [1, 4, 5, 6, 3]
 
print ("До: " + str(test_list))
def f():
    for i in range(len(test_list)-1, 0, -1):

        j = randint(0, i + 1)
        test_list[i], test_list[j] = test_list[j], test_list[i]

    print ("После: " +  str(test_list))


f()

