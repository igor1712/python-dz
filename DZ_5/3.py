


from random import randint
x = 'x'
nole = '0'

a = [['*','*','*'],

    ['*','*','*'],

    ['*','*','*'],
    ]

def print_lst(lst):
    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][j], end = ' ')
        print()

# def plogiat(user_1):
    
#     count_lst = [0 * i for i in range(1,10)]
#     while True:
#         count_lst.append(user_1)
#         if  user_1  == count_lst[]:
#             for i in range(1,10):
#                 while True:
#                     print('такое значение есть в списке')
#                     user_1 = int(input('User_1: '))
#             print(count_lst)           
            

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
        print(f'Победил игрок  {x} ')
        break
    elif a[1][0] == x and a[1][1] == x and a[1][2] == x:
        print(f'Победил игрок  {x} ')
        break
    elif a[2][0] == x and a[2][1] == x and a[2][2] == x:
        print(f'Победил игрок  {x} ')
        break

            # ''' сверху вниз '''

    elif a[0][0] == x and a[1][0] == x and a[2][0] == x:
        print(f'Победил игрок  {x} ')
        break
    elif a[0][1] == x and a[1][1] == x and a[2][1] == x:
        print(f'Победил игрок  {x} ')
        break
    elif a[0][2] == x and a[1][2] == x and a[2][2] == x:
        print(f'Победил игрок  {x} ')
        break
    
            # ''' по диагонали  '''

    
    elif a[0][0] == x and a[1][1] == x and a[2][2] == x:
        print(f'Победил игрок  {x} ')
        break
    elif a[0][2] == x and a[1][1] == x and a[2][0] == x:
        print(f'Победил игрок  {x} ')
        break


    user_2 = int(input('User_2: '))
    # plogiat(user_2)
    logick_game(user_2,a,nole)
    print_lst(a)
    
     # '''слева направо '''
    if a[0][0] == nole and a[0][1] == nole and a[0][2] == nole:
        print(f'Победил игрок  {nole} ')
        break
    elif a[1][0] == nole and a[1][1] == nole and a[1][2] == nole:
        print(f'Победил игрок  {nole} ')
        break
    elif a[2][0] == nole and a[2][1] == nole and a[2][2] == nole:
        print(f'Победил игрок  {nole} ')
        break

            # ''' сверху вниз '''

    elif a[0][0] == nole and a[1][0] == nole and a[2][0] == nole:
        print(f'Победил игрок  {nole} ')
        break
    elif a[0][1] == nole and a[1][1] == nole and a[2][1] == nole:
        print(f'Победил игрок  {nole} ')
        break
    elif a[0][2] == nole and a[1][2] == nole and a[2][2] == nole:
        print(f'Победил игрок  {nole} ')
        break
    
            # ''' по диагонали  ''nole

    
    elif a[0][0] == nole and a[1][1] == nole and a[2][2] == nole:
        print(f'Победил игрок  {nole} ')
        break
    elif a[0][2] == nole and a[1][1] == nole and a[2][0] == nole:
        print(f'Победил игрок  {nole} ')
        break
