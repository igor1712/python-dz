

from emoji import *
from random import randint


x = emojize(":cat:")
nole = emojize(":mouse:")


a = [['*','*','*'],

    ['*','*','*'],

    ['*','*','*'],
    ]

def print_lst(lst):
    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][j], end = ' ')
        print()



def logick_game(user_1,a,x):

    if user_1 == 1:
        a[0][0] = x
    elif user_1 == 2:
        a[0][1] = x
    elif user_1 == 3:
        a[0][2] = x
    elif user_1 == 4:
        a[1][0] = x
    elif user_1 == 5:
        a[1][1] = x
    elif user_1 == 6:
        a[1][2] = x
    elif user_1 == 7:
        a[2][0] = x
    elif user_1 == 8:
        a[2][1] = x
    elif user_1 == 9:
        a[2][2] = x 



while True:
    
    

    user_1 = int(input('User_1: '))
    # plogiat(user_1)
    logick_game(user_1,a,x)
    print_lst(a)

     # '''слева направо '''
    if a[0][0] == x and a[0][1] == x and a[0][2] == x:
        print(f'{emojize(":1st_place_medal:")*3}  {x} ')
        break
    elif a[1][0] == x and a[1][1] == x and a[1][2] == x:
        print(f'{emojize(":1st_place_medal:")*3}  {x} ')
        break
    elif a[2][0] == x and a[2][1] == x and a[2][2] == x:
        print(f'{emojize(":1st_place_medal:")*3}  {x} ')
        break

            # ''' сверху вниз '''

    elif a[0][0] == x and a[1][0] == x and a[2][0] == x:
        print(f'{emojize(":1st_place_medal:")*3}  {x} ')
        break
    elif a[0][1] == x and a[1][1] == x and a[2][1] == x:
        print(f'{emojize(":1st_place_medal:")*3}  {x} ')
        break
    elif a[0][2] == x and a[1][2] == x and a[2][2] == x:
        print(f'{emojize(":1st_place_medal:")*3}  {x} ')
        break
    
            # ''' по диагонали  '''

    
    elif a[0][0] == x and a[1][1] == x and a[2][2] == x:
        print(f'{emojize(":1st_place_medal:")*3}  {x} ')
        break
    elif a[0][2] == x and a[1][1] == x and a[2][0] == x:
        print(f'{emojize(":1st_place_medal:")*3}  {x} ')
        break


    user_2 = int(input('User_2: '))
    # plogiat(user_2)
    logick_game(user_2,a,nole)
    print_lst(a)
    
     # '''слева направо '''
    if a[0][0] == nole and a[0][1] == nole and a[0][2] == nole:
        print(f'{emojize(":1st_place_medal:")*3}  {nole} ')
        break
    elif a[1][0] == nole and a[1][1] == nole and a[1][2] == nole:
        print(f'{emojize(":1st_place_medal:")*3}  {nole} ')
        break
    elif a[2][0] == nole and a[2][1] == nole and a[2][2] == nole:
        print(f'{emojize(":1st_place_medal:")*3}  {nole} ')
        break

            # ''' сверху вниз '''

    elif a[0][0] == nole and a[1][0] == nole and a[2][0] == nole:
        print(f'{emojize(":1st_place_medal:")*3}  {nole} ')
        break
    elif a[0][1] == nole and a[1][1] == nole and a[2][1] == nole:
        print(f'{emojize(":1st_place_medal:")*3}  {nole} ')
        break
    elif a[0][2] == nole and a[1][2] == nole and a[2][2] == nole:
        print(f'{emojize(":1st_place_medal:")*3}  {nole} ')
        break
    
            # ''' по диагонали  ''nole

    
    elif a[0][0] == nole and a[1][1] == nole and a[2][2] == nole:
        print(f'{emojize(":1st_place_medal:")*3}  {nole} ')
        break
    elif a[0][2] == nole and a[1][1] == nole and a[2][0] == nole:
        print(f'{emojize(":1st_place_medal:")*3}  {nole} ')
        break
