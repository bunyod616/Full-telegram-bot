from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from main import Database
menu_keyword = ReplyKeyboardMarkup([
    [KeyboardButton('Menyu'),KeyboardButton('Category')],
],resize_keyboard=True)

menu_detail = ReplyKeyboardMarkup(resize_keyboard=True)
query = "select * from menu"
for i in Database.connect(query, "select"):
    menu_detail.add(KeyboardButton(i[1]))
menu_detail.add(KeyboardButton("Back 1"))

gm_motors = ReplyKeyboardMarkup([
    [KeyboardButton('Cobalt'),KeyboardButton('Spark')],
    [KeyboardButton('Malibu'),KeyboardButton('Nexia (3)')],
    [KeyboardButton('Back 2')],
],resize_keyboard=True)

kia_motors = ReplyKeyboardMarkup([
    [KeyboardButton('KIA K9'),KeyboardButton('KIA EV6')],
    [KeyboardButton('KIA K5'),KeyboardButton('KIA K8')],
    [KeyboardButton('Back 2')],
],resize_keyboard=True)
