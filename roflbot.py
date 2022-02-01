import telebot
from telebot import types
import random

token = '5193407607:AAF4bU8Qm05VaCO-EbAO7BXuWksn6sOw7jw'


bot=telebot.TeleBot(token)


@bot.message_handler(content_types='text')
def message_reply(message):
    if 'Кинуть с прогиба' == message.text[:16]:
        img = open('progib{}.jpeg'.format(str(random.randint(0,5))), 'rb')
        bot.send_photo(message.chat.id, img, caption="{} кинул {} с прогиба".format(str(message.from_user.first_name),str(message.text[16:])))
    if 'кинуть с прогиба' == message.text[:16]:
        img = open('progib{}.jpeg'.format(str(random.randint(0,5))), 'rb')
        bot.send_photo(message.chat.id, img, caption="{} кинул {} с прогиба".format(str(message.from_user.first_name),str(message.text[16:])))
    if 'Зделать проход в ноги' == message.text[:21]:
        img = open('prohod{}.jpeg'.format(str(random.randint(0,5))), 'rb')
        bot.send_photo(message.chat.id, img, caption="{} Зделал проход в ноги {}".format(str(message.from_user.first_name),str(message.text[21:])))
    if 'зделать проход в ноги' == message.text[:21]:
        img = open('prohod{}.jpeg'.format(str(random.randint(0,5))), 'rb')
        bot.send_photo(message.chat.id, img, caption="{} Зделал проход в ноги {}".format(str(message.from_user.first_name),str(message.text[21:])))
    if 'Изнасиловать' == message.text[:12]:
        img = open('izn{}.jpeg'.format(str(random.randint(0,3))), 'rb')
        bot.send_photo(message.chat.id, img, caption="{} изнасиловал {}".format(str(message.from_user.first_name),str(message.text[12:])))
    if 'изнасиловать' == message.text[:12]:
        img = open('izn{}.jpeg'.format(str(random.randint(0,3))), 'rb')
        bot.send_photo(message.chat.id, img, caption="{} изнасиловал {} ".format(str(message.from_user.first_name),str(message.text[12:])))
    if 'Шлепнуть' == message.text[:8]:
        img = open('shlep{}.jpeg'.format(str(random.randint(0,3))), 'rb')
        bot.send_photo(message.chat.id, img, caption="{} шлепнул {}".format(str(message.from_user.first_name),str(message.text[8:])))
    if 'шлепнуть' == message.text[:8]:
        img = open('shlep{}.jpeg'.format(str(random.randint(0,3))), 'rb')
        bot.send_photo(message.chat.id, img, caption="{} шлепнул {} ".format(str(message.from_user.first_name),str(message.text[8:])))
    if 'Пнуть' == message.text[:5]:
        img = open('pnyl{}.jpeg'.format(str(random.randint(0,3))), 'rb')
        bot.send_photo(message.chat.id, img, caption="{} пнул {}".format(str(message.from_user.first_name),str(message.text[5:])))
    if 'пнуть' == message.text[:5]:
        img = open('pnyl{}.jpeg'.format(str(random.randint(0,3))), 'rb')
        bot.send_photo(message.chat.id, img, caption="{} пнул {} ".format(str(message.from_user.first_name),str(message.text[5:])))
    if 'Ударить с вертухи' == message.text[:17]:
        img = open('vertyha{}.jpeg'.format(str(random.randint(0,3))), 'rb')
        bot.send_photo(message.chat.id, img, caption="{} ударил с вертухи {}".format(str(message.from_user.first_name),str(message.text[17:])))
    if 'ударить с вертухи' == message.text[:17]:
        img = open('vertyha{}.jpeg'.format(str(random.randint(0,3))), 'rb')
        bot.send_photo(message.chat.id, img, caption="{} ударил с вертухи {} ".format(str(message.from_user.first_name),str(message.text[17:])))
    if 'Оформить двоечку' == message.text[:16]:
        img = open('dva{}.jpeg'.format(str(random.randint(0,3))), 'rb')
        bot.send_photo(message.chat.id, img, caption="{} oформил двоечку {}".format(str(message.from_user.first_name),str(message.text[17:])))
    if 'оформить двоечку' == message.text[:16]:
        img = open('dva{}.jpeg'.format(str(random.randint(0,3))), 'rb')
        bot.send_photo(message.chat.id, img, caption="{} oформил двоечку {} ".format(str(message.from_user.first_name),str(message.text[17:])))
    if 'Трахнуть' == message.text[:8]:
        img = open('izn{}.jpeg'.format(str(random.randint(0,3))), 'rb')
        bot.send_photo(message.chat.id, img, caption="{} трахнул {}".format(str(message.from_user.first_name),str(message.text[8:])))
    if 'трахнуть' == message.text[:8]:
        img = open('izn{}.jpeg'.format(str(random.randint(0,3))), 'rb')
        bot.send_photo(message.chat.id, img, caption="{} трахнул {} ".format(str(message.from_user.first_name),str(message.text[8:])))
    if 'Help' == message.text[:4]:
    	bot.send_message(message.chat.id,'Список доступных команд: \n Кинуть с прогиба \n Зделать проход в ноги \n Изнасиловать \n Шлепнуть \n Пнуть \n Ударить с вертухи \n Оформить двоечку \n Трахнуть')
    if 'help' == message.text[:4]:
    	bot.send_message(message.chat.id,'Список доступных команд: \n Кинуть с прогиба \n Зделать проход в ноги \n Изнасиловать \n Шлепнуть \n Пнуть \n Ударить с вертухи \n Оформить двоечку \n Трахнуть')

bot.infinity_polling()