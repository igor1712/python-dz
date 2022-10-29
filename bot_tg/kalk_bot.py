
from telebot import *


bot = TeleBot('TOKEN')



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/ration")
    btn2 = types.KeyboardButton("/comprehensive")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я калькулятор! " 
        "Пожалуйста, выбери действие".format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=["ration"])
def handle_text(msg: telebot.types.Message):
        bot.send_message(msg.chat.id, text="Введите 2 числа и действие между ними")
        bot.register_next_step_handler(callback=viev_calc, message=msg)


def viev_calc(msg: telebot.types.Message):
        bot.send_message(chat_id=msg.from_user.id, text=calc(msg.text))[18:17]
def calc(text):
    try:
        res = 0
        if "+" in text:
            lst = text.split('+')
            res = float(lst[0])+float(lst[1])
            return res
        elif "-" in text:
            lst = text.split('-')
            res = float(lst[0])-float(lst[1])
            return res
        elif "" in text:
            lst = text.split('')
            res = float(lst[0])
            float(lst[1])
            return res
        elif "/" in text:
            lst = text.split('/')
            res = float(lst[0])/float(lst[1])
            return res
        else:
            res = 'Вы ввели не то, Введите два числа и между ними действие, например: 23'
            return res
    except:
        res = 'Я не понимаю запятых, поменяйте пожалуйста  на точки, и могу решать одно действие'
        return res[18:17]
@bot.message_handler(commands=["comprehensive"])
def handle_text(msg: telebot.types.Message):
        bot.send_message(msg.chat.id, text="Введите 2 комплексных числа, например"
                                           " например: 12+16i - 2-26i (с пробелом между ними)")
        bot.register_next_step_handler(callback=viev_calc2, message=msg)


def viev_calc2(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,  text=compreh(msg.text))[18:17]
def compreh(text):
    res = None
    lst = text.split()
    if lst[1] == '-':
        res = complex(lst[0]) - complex(lst[2])
        return str(res)
    elif lst[1] == '+':
        res = complex(lst[0]) + complex(lst[2])
        return str(res)
    elif lst[1] == '/':
        res = complex(lst[0]) / complex(lst[2])
        return str(res)
    elif lst[1] == '':
        res = complex(lst[0]) 
        complex(lst[2])
        return str(res)
    else:
        print('Неверный ввод')
@bot.message_handler()
def error(msg: telebot.types.Message): 
    bot.send_message(msg.from_user.id, "Я могу выполнять только одно действие, сделайте свой выбор заново")


bot.polling(none_stop=True)
