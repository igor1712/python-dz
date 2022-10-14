
'''Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый
 ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
 Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
 чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""'''


from random import randint

cand = 100
rand = randint(1,2)

print(f'Первый ход User: {rand}')
print()


while True:

     
    if rand == 1:
        bot = randint(1,28)

        user = int(input('User: ' ))   
        while user < 1 or user > 28:
            print('Возьми не меньше 1 и не больше 28 конфет')
            user = int(input('User: '))
        while user > cand:
            print('Не хватает конфет')
            user = int(input('user: '))
        if cand - user == 0:
            print('Win user')
            break
        cand -= user                             
        print(cand)
        user = 0
        
        if bot > cand:
            bot = randint(1,cand)
            print(f'bot: {bot} ') 
            if cand - bot == 0:
                print('Win bot')
                break
        cand -= bot
        print(f'bot: {bot}')
        print(cand)
        bot = 0
   

        '''Второй блок , если rand = 2'''

    elif rand == 2:
        bot = randint(1,28)
        
        if bot > cand:
            bot = randint(1,cand)
            print(f'bot: {bot} ') 
            if cand - bot == 0:
                print('Win bot')
                break
        cand -= bot
        print(f'bot: {bot}')
        print(cand)
        bot = 0


        user = int(input('User: ' ))   
        while user < 1 or user > 28:
            print('Возьми не меньше 1 и не больше 28 конфет')
            user = int(input('User: '))
        while user > cand:
            print('Не хватает конфет')
            user = int(input('user: '))
        if cand - user == 0:
            print('Win user')
            break
        cand -= user                             
        print(cand)
        user = 0
    

    

    


    



    

    
    

        
    
        
    

            
    
    
        


        

    
          




