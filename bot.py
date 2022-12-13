import telebot
from telebot import types
import currencies as cur

TOKEN = "5960856662:AAFGdwozhammIXhjaMdaaXYCnto-VEOrTrI"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Курс":
        bot.send_message(message.from_user.id, "Отдав 1 тенге, ты получишь " + str(cur.get_currency_rate("KZT")) + " рубля, путник")
    elif message.text == "Обратный курс":
        bot.send_message(message.from_user.id, "Отдав 1 рубль, ты получишь " + str(cur.get_currency_rate("KZT", back=True)) + " тенге, путник")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Рассказываю путникам о курсах валют")
    else:
        bot.send_message(message.from_user.id, "Не понимаю тебя, путник, пока я умею только сообщать о курсе рубля к тенге и наоброт")

bot.polling(none_stop=True, interval=0)





