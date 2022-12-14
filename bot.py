import telebot
from telebot import types
import currencies as cur
import users_db

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
    users_db.add_new(message.from_user.id)
    text = "О, я тебя категорически приветствую, путник! Чего знать изволишь?"
    bot.send_message(message.from_user.id, text, reply_markup=add_buttons())


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "курс":
        text = "Отдав 1 тенге, ты получишь " + str(cur.get_currency_rate("KZT")) + " рубля, путник"
    elif message.text.lower() == "обратный курс":
        text = "Отдав 1 рубль, ты получишь " + str(cur.get_currency_rate("KZT", back=True)) + " тенге, путник"
    elif message.text.lower() == "/help":
        text = "Рассказываю путникам о курсах валют"
    else:
        text = "Не понимаю тебя, путник, пока я умею только сообщать о курсе рубля к тенге и наоброт"
    bot.send_message(message.from_user.id, text, reply_markup=add_buttons())


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)





