from time import sleep

import telebot
from telebot import types

#Подключил своего бота
Bot = telebot.TeleBot('8088657846:AAGeM6oDdDh_F5qLcVakkZbSULWLWp0OOtY')

bal = 0
user_bals = {}

#викторина
#file = open('./photo.JPG', 'rb')
#Bot.send_photo(message.chat.id, file, reply_markup=markup)


#отввет на команду текст можно форматировать
@Bot.message_handler(commands=['start', 'Start'])
def obrabotka_comand(message):
    Bot.send_message(message.chat.id, f'{message.from_user.first_name} давай сыграем в игру??? ')
    Bot.send_message(message.chat.id, 'Это моя не большая викторина на 5 вопросов если готов начать пиши да')

    #Кнопки добавить
    #markup.add(types.InlineKeybardButton('да'))

@Bot.message_handler()
def game(message):
    if message.text.lower() in ['да', 'да']:
        Bot.send_message(message.chat.id, 'Ура ура! Правила следующие: за каждый правильный ответ ты будешь получать баллы в зависимости от сложности вопроса. Удачи!')
        game_1(message)
    elif message.text.lower() in ['нет', 'нет']:
        Bot.send_message(message.chat.id, 'Прости, но это лишь иллюзия выбора.')
        game_1(message)
    else:
        Bot.reply_to(message, 'Прости, я тебя не понимаю. Я ботик ^_^')
        Bot.send_message(message.chat.id, 'Попробуй написать "да" или "нет".')


def game_1(message):
    global bal
    Bot.send_message(message.chat.id, 'Вопрос 1: Какой из этих городов находится на двух континентах? 100 баллов')

    # Создаём клавиатуру
    markup = types.ReplyKeyboardMarkup()
    b1 = types.KeyboardButton('москва')  # Кнопка 1
    b2 = types.KeyboardButton('стамбул')  # Кнопка 2
    b3 = types.KeyboardButton('лондон')  # Кнопка 1
    b4 = types.KeyboardButton('токио')  # Кнопка 2
    markup.add(b1, b2, b3, b4)  # Добавляем кнопки в разметку

    # Отправляем вопрос с клавиатурой
    Bot.send_message(message.chat.id, 'Выбери один из вариантов:', reply_markup=markup)

    # Переход к следующему шагу
    Bot.register_next_step_handler(message, otvet_1)

def otvet_1(message):
    global bal
    if message.text.lower() == 'стамбул':
        Bot.send_message(message.chat.id, 'Отлично, держи +100 баллов!')
        bal+=100
        game_2(message)
    elif message.text.lower() in ['москва','лондон','токио']:
        Bot.send_message(message.chat.id, 'Жаль, не верно +0 баллов.')
        Bot.send_message(message.chat.id, 'Правильный ответ Стамбул')
        game_2(message)
    else:
        Bot.send_message(message.chat.id, 'Прости, я не понимаю этот ответ. Попробуй выбрать один из вариантов на клавиатуре.')
        game_1(message)  # Повторяем вопрос

def game_2(message):
    global bal
    Bot.send_message(message.chat.id, 'Вопрос 2: Ты меня слышишь, но не видишь. Я не говорю, пока ты не скажешь. Что я? 50 баллов')

    # Создаём клавиатуру
    markup = types.ReplyKeyboardMarkup()
    b1 = types.KeyboardButton('радио')  # Кнопка 1
    b2 = types.KeyboardButton('тишина')  # Кнопка 2
    b3 = types.KeyboardButton('ветер')  # Кнопка 1
    b4 = types.KeyboardButton('эхо')  # Кнопка 2
    markup.add(b1, b2, b3, b4)  # Добавляем кнопки в разметку

    Bot.send_message(message.chat.id, 'Выбери один из вариантов:', reply_markup=markup)

    # Переход к следующему шагу
    Bot.register_next_step_handler(message, otvet_2)

def otvet_2(message):
    global bal
    if message.text.lower() == 'эхо':
        Bot.send_message(message.chat.id, 'Отлично, держи +50 баллов!')
        bal+=50
        game_3(message)
    elif message.text.lower() in ['ветер','радио','тишина']:
        Bot.send_message(message.chat.id, 'Жаль, не верно +0 баллов.')
        Bot.send_message(message.chat.id, 'Правильный ответ Эхо')
        game_3(message)
    else:
        Bot.send_message(message.chat.id, 'Прости, я не понимаю этот ответ. Попробуй выбрать один из вариантов на клавиатуре.')
        game_2(message)  # Повторяем вопрос

def game_3(message):
    global bal

    Bot.send_message(message.chat.id, 'Вопрос 3: Какая из этих стран не была колонией Великобритании? 100 баллов')

    # Создаём клавиатуру
    markup = types.ReplyKeyboardMarkup()
    b1 = types.KeyboardButton('австралия')  # Кнопка 1
    b2 = types.KeyboardButton('канада')  # Кнопка 2
    b3 = types.KeyboardButton('сша')  # Кнопка 1
    b4 = types.KeyboardButton('франция')  # Кнопка 2
    markup.add(b1, b2, b3, b4)  # Добавляем кнопки в разметку

    # Отправляем вопрос с клавиатурой
    Bot.send_message(message.chat.id, 'Выбери один из вариантов:', reply_markup=markup)

    # Переход к следующему шагу
    Bot.register_next_step_handler(message, otvet_3)

def otvet_3(message):
    global bal
    if message.text.lower() == 'франция':
        Bot.send_message(message.chat.id, 'Отлично, держи +100 баллов!')
        bal+=100
        game_4(message)
    elif message.text.lower() in ['австралия','канада','сша']:
        Bot.send_message(message.chat.id, 'Жаль, не верно +0 баллов.')
        Bot.send_message(message.chat.id, 'Правильный ответ франция')
        game_4(message)
    else:
        Bot.send_message(message.chat.id, 'Прости, я не понимаю этот ответ. Попробуй выбрать один из вариантов на клавиатуре.')
        game_3(message)  # Повторяем вопрос

def game_4(message):
    global bal
    Bot.send_message(message.chat.id, 'Вопрос 4: Какой металл является самым прочным? 150 баллов')

    # Создаём клавиатуру
    markup = types.ReplyKeyboardMarkup()
    b1 = types.KeyboardButton('железо')  # Кнопка 1
    b2 = types.KeyboardButton('титан')  # Кнопка 2
    b3 = types.KeyboardButton('вольфрам')  # Кнопка 1
    b4 = types.KeyboardButton('хром')  # Кнопка 2
    markup.add(b1, b2, b3, b4)  # Добавляем кнопки в разметку

    # Отправляем вопрос с клавиатурой
    Bot.send_message(message.chat.id, 'Выбери один из вариантов:', reply_markup=markup)

    # Переход к следующему шагу
    Bot.register_next_step_handler(message, otvet_4)

def otvet_4(message):
    global bal
    if message.text.lower() == 'вольфрам':
        Bot.send_message(message.chat.id, 'Отлично, держи +150 баллов!')
        bal+=150
        game_5(message)
    elif message.text.lower() in ['железо','титан','хром']:
        Bot.send_message(message.chat.id, 'Жаль, не верно +0 баллов.')
        Bot.send_message(message.chat.id, 'Правильный ответ вольфрам')
        game_5(message)
    else:
        Bot.send_message(message.chat.id, 'Прости, я не понимаю этот ответ. Попробуй выбрать один из вариантов на клавиатуре.')
        game_4(message)  # Повторяем вопрос

def game_5(message):
    global bal
    Bot.send_message(message.chat.id, 'Вопрос 5: Какая планета Солнечной системы вращается вокруг своей оси в направлении, противоположном другим планетам? 100 баллов')

    # Создаём клавиатуру
    markup = types.ReplyKeyboardMarkup()
    b1 = types.KeyboardButton('венера')  # Кнопка 1
    b2 = types.KeyboardButton('марс')  # Кнопка 2
    b3 = types.KeyboardButton('нептун')  # Кнопка 1
    b4 = types.KeyboardButton('уран')  # Кнопка 2
    markup.add(b1, b2, b3, b4)  # Добавляем кнопки в разметку

    # Отправляем вопрос с клавиатурой
    Bot.send_message(message.chat.id, 'Выбери один из вариантов:', reply_markup=markup)

    # Переход к следующему шагу
    Bot.register_next_step_handler(message, otvet_5)

def otvet_5(message):
    global bal
    if message.text.lower() == 'венера':
        Bot.send_message(message.chat.id, 'Отлично, держи +100 баллов!')
        bal+=100
        end(message)
    elif message.text.lower() in ['марс','нептун','уран']:
        Bot.send_message(message.chat.id, 'Жаль, не верно +0 баллов.')
        Bot.send_message(message.chat.id, 'Правильный ответ венер')
        end(message)
    else:
        Bot.send_message(message.chat.id, 'Прости, я не понимаю этот ответ. Попробуй выбрать один из вариантов на клавиатуре.')
        game_5(message)  # Повторяем вопрос

def end(message):
    global bal
    markup = types.ReplyKeyboardMarkup()
    b1 = types.KeyboardButton('/start')
    markup.add(b1)# Кнопка 1
    Bot.send_message(message.chat.id,'------------------------' , reply_markup=markup)
    Bot.send_message(message.chat.id, f'Спасибо что прошёл мою викторину у тебя {bal}')
    Bot.send_message(message.chat.id, 'если нашёл ошибки обязательно сообщи мне а так же чтобы начать заного напиши /start')






# информация о чате
@Bot.message_handler(commands=['info'])
def info(message):
    Bot.send_message(message.chat.id, message)

#Обработка произвольного текста(можно использовать условия)
@Bot.message_handler(func=lambda message: True)
def ne_comanda(message):
    Bot.reply_to(message, 'Прости, я тебя не понимаю я ботик ^_^')



#чтобы бот работал вечно
Bot.polling(none_stop=True)
