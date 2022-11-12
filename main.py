import telebot

from calculator import reformatNegativeValues, calculate, open_brackets
from base import writeLog, readLog, clearLog
from tic_tac_toe import *
from InformSistem.base import *

global wait_input, i_s
wait_input = False
i_s = False

token = 'token'
bot = telebot.TeleBot(token)


def bot_start():
    print("бот запущен")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Это бот калькулятор который ведет запись всех операци\n"
                                      "Дополнительно можно поиграть в крестики нолики\n"
                                      "/calc - запускает калькулятор\n"
                                      "/log - показать список операции\n"
                                      "/clear - очистить список операции\n"
                                      "/game - запустить крестики-нолики\n"
                                      "/inform_sistem - информационная система")


@bot.message_handler(content_types='text')
def all_message(message):
    global wait_input
    global i_s

    if wait_input:
        if message.text != "/exit":
            try:
                result = take_input(int(message.text))

                if result in "1":
                    bot.send_message(message.chat.id, print_board())
                    bot.send_message(message.chat.id, next_stape())
                else:
                    bot.send_message(message.chat.id, result)
                if result == "Ты выиграл!":
                    wait_input = False
            except:
                bot.send_message(message.chat.id, "Введите число от 1 до 9. Чтобы выйти из игры /exit")

    if message.text == "/exit":
        wait_input = False
        bot.send_message(message.chat.id, "Game Over")

    if message.text == "/calc":
        msg = bot.send_message(message.chat.id, "Введите выражение")
        bot.register_next_step_handler(msg, calc_result)

    if message.text == "/log":
        try:
            lst = readLog()
            print(lst)
            bot.send_message(message.chat.id, lst)
        except:
            bot.send_message(message.chat.id, "Список пуст")

    if message.text == "/clear":
        clearLog()
        bot.send_message(message.chat.id, "список очищен!")

    if message.text == "/game":
        bot.send_message(message.chat.id, "игра запущена, введите число ячейки\n "
                                          "куда надо сделать ход \n"
                                          "/exit - для остановки игры")
        start_game()
        x = print_board()
        bot.send_message(message.chat.id, x)
        bot.send_message(message.chat.id, next_stape())
        wait_input = True

    if message.text == "/inform_sistem":
        i_s = True
        if i_s:
            bot.send_message(message.chat.id, start_bd())
            msg = bot.send_message(message.chat.id, "Введите нужную операцию:\n"
                                                    "/add - добавить нового сотрудника\n"
                                                    "/del - удалить сотрудника\n"
                                                    "/all_db - показать полный список сотрудников\n"
                                                    "/search - показать информацию по фамилии\n"
                                                    "/out - выйти из системы")
            bot.register_next_step_handler(msg, inform_sistem)




def calc_result(mesg):
    input_text = mesg.text.split()
    task = ' '.join(input_text)
    input_text = reformatNegativeValues(input_text)
    result = calculate(open_brackets(input_text))
    result = f'{task} = {result}'
    writeLog(result)
    bot.send_message(mesg.chat.id, f"Ваш ответ: {result}")



def inform_sistem(message):
    global i_s
    if message.text == "/add":
        pass # добавление сотрудника
    if message.text == "/del":
        pass # удаление сотрудника
    if message.text == "/all_db":
        pass # viev all worker
    if message.text == "/search":
        pass # search worker in data bese last_name
    if message.text == "/out":
        bot.send_message(message.chat.id, "Закрыто, введите команду  /start")
        i_s = False
        return i_s
try:
    print("Бот запущен")
    bot.polling()
except:
    print("Ошибка")
