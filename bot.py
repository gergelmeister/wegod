import telebot
from telebot import types
import currencies as cur
import users_db
import datetime
import threading

TOKEN = "5960856662:AAFGdwozhammIXhjaMdaaXYCnto-VEOrTrI"

bot = telebot.TeleBot(TOKEN)


def add_buttons(agreement):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Курс")
    btn2 = types.KeyboardButton("Обратный курс")
    if agreement == 1:
        btn3 = types.KeyboardButton("Отписаться от курса")
    else:
        btn3 = types.KeyboardButton("Подписаться на курс")
    markup.add(btn1, btn2, btn3)
    return markup


def rate_reminder():
    event = threading.Event()
    while True:
        print("Я здеся")
        base = users_db.get_base()
        for user in base:
            if user[2] == 1:
                if int(datetime.datetime.utcnow().timestamp() - 3600) > int(user[3]):
                    text = f"""Сейчас ты получишь {str(cur.get_currency_rate('KZT'))} рублей за 1 тенге и {str(cur.get_currency_rate('KZT', back=True))} тенге за 1 рубль"""
                    bot.send_message(user[0], text, reply_markup=add_buttons(users_db.get_agreement(user[0])))
                    users_db.set_last_interaction(user[0])
        event.wait(timeout=60)


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    users_db.add_new(user_id)
    text = "О, я тебя категорически приветствую, путник! Чего знать изволишь?"
    bot.send_message(user_id, text, reply_markup=add_buttons(users_db.get_agreement(user_id)))
    users_db.set_last_interaction(user_id)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    user_id = message.from_user.id
    if message.text.lower() == "курс":
        text = "Отдав 1 тенге, ты получишь " + str(cur.get_currency_rate("KZT")) + " рубля, путник"
    elif message.text.lower() == "обратный курс":
        text = "Отдав 1 рубль, ты получишь " + str(cur.get_currency_rate("KZT", back=True)) + " тенге, путник"
    elif message.text.lower() == "/help":
        text = "Рассказываю путникам о курсах валют"
    elif message.text.lower() == "подписаться на курс":
        text = "Спасибо, путник, теперь я буду присылать тебе уведомление о курсе каждый час"
        users_db.change_agreement(user_id, 1)
    elif message.text.lower() == "отписаться от курса":
        text = "Понял, больше не побеспокою"
        users_db.change_agreement(user_id, 0)
    else:
        text = "Не понимаю тебя, путник, пока я умею только сообщать о курсе рубля к тенге и наоброт"
    bot.send_message(message.from_user.id, text, reply_markup=add_buttons(users_db.get_agreement(message.from_user.id)))
    users_db.set_last_interaction(user_id)


if __name__ == '__main__':
    monitoring = threading.Thread(target=rate_reminder)
    monitoring.start()
    bot.polling(none_stop=True, interval=0)





