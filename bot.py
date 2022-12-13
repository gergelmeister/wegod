import telebot
from telebot import types
import currencies as cur

TOKEN = "5960856662:AAFGdwozhammIXhjaMdaaXYCnto-VEOrTrI"

bot = telebot.TeleBot(TOKEN)


def add_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Курс")
    btn2 = types.KeyboardButton("Обратный курс")
    markup.add(btn1, btn2)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "О, я тебя категорически приветствую, путник! Чего знать изволишь?", reply_markup=add_buttons())


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Курс":
        bot.send_message(message.from_user.id, "Отдав 1 тенге, ты получишь " + str(cur.get_currency_rate("KZT")) + " рубля, путник", reply_markup=add_buttons())
    elif message.text == "Обратный курс":
        bot.send_message(message.from_user.id, "Отдав 1 рубль, ты получишь " + str(cur.get_currency_rate("KZT", back=True)) + " тенге, путник", reply_markup=add_buttons())
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Рассказываю путникам о курсах валют", reply_markup=add_buttons())
    else:
        bot.send_message(message.from_user.id, "Не понимаю тебя, путник, пока я умею только сообщать о курсе рубля к тенге и наоброт", reply_markup=add_buttons())

bot.polling(none_stop=True, interval=0)





