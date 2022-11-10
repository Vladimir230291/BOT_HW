import telebot

from calculator import reformatNegativeValues, calculate, open_brackets
from base import writeLog, readLog, clearLog
from tic_tac_toe import *

global wait_input
wait_input = False

token = '5722701400:AAEKsYtTOzQMW4d1F-w4jBxS-UnMGkfT5qg'
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
                                      "/game - запустить крестики-нолики\n")


@bot.message_handler(content_types='text')
def all_message(message):
    global wait_input

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
        lst = readLog()
        bot.send_message(message.chat.id, lst)

    if message.text == "/clear":
        lst = clearLog()
        bot.send_message(message.chat.id, lst)

    if message.text == "/game":
        bot.send_message(message.chat.id, "игра запущена, введите число ячейки\n "
                                          "куда надо сделать ход \n"
                                          "/exit - для остановки игры")
        start_game()
        x = print_board()
        bot.send_message(message.chat.id, x)
        bot.send_message(message.chat.id, next_stape())
        wait_input = True


def calc_result(mesg):
    input_text = mesg.text.split()
    task = ' '.join(input_text)
    input_text = reformatNegativeValues(input_text)
    result = calculate(open_brackets(input_text))
    result = f'{task} = {result}'
    writeLog(result)
    bot.send_message(mesg.chat.id, f"Ваш ответ: {result}")


try:
    print("Бот запущен")
    bot.polling()
except:
    print("Ошибка")
