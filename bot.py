import logging
import os
from keyboards import menu_keyword,menu_detail,gm_motors,kia_motors
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from Inline_keywords.post import keyword
from main import Database

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    chat_id = str(message.chat.id)

    check_query = f"""SELECT * FROM aiogram_bot WHERE chat_id = '{chat_id}'"""
    if len(Database.connect(check_query, "select")) >= 1:
        await message.answer(f"Hello @{username}", reply_markup=menu_keyword)

    else:
        print(f"{first_name} start bot")
        query = f"""INSERT INTO aiogram_bot(first_name, last_name, username, chat_id) VALUES('{first_name}', '{last_name}', '{username}', '{chat_id}')"""
        print(f"{username} {Database.connect(query, 'insert')} database")
        await message.answer(f"Hello @{username}",reply_markup=menu_keyword)


@dp.message_handler(commands=['data'])
async def select(message: types.Message):
    chat_id = message.chat.id
    query_select = f"SELECT * FROM aiogram_bot WHERE chat_id = '{chat_id}'"
    data = Database.connect(query_select, "select")
    print(data)
    await message.reply(f"""
        Salom @{data[0][3]}

        First Name: {data[0][1]}
        Last Name: {data[0][2]}""")

@dp.message_handler(lambda message: message.text == "Menyu")
async def show_menu(message: types.Message):
    await message.answer(f"Menyulardan birini tanlang" , reply_markup=menu_detail)

@dp.message_handler(lambda message: message.text == "Category")
async def show_category(message: types.Message):
    await message.answer(f"Categorylardan birini tanlang" , reply_markup=keyword)

@dp.message_handler(lambda message: message.text == "Back 1")
async def back(message: types.Message):
    await message.answer(f"Choose Menyu or Category" , reply_markup=menu_keyword)

@dp.message_handler(lambda message: message.text == "Back 2")
async def back(message: types.Message):
    await message.answer(f"Choose Menyu or Category" , reply_markup=menu_detail)

@dp.message_handler(lambda message: message.text == "GM")
async def show_category(message: types.Message):
    await message.answer(f"GM motors",reply_markup=gm_motors)

@dp.message_handler(lambda message: message.text == "KIA")
async def show_category(message: types.Message):
    await message.answer(f"KIA motors",reply_markup=kia_motors)




@dp.callback_query_handler(lambda call: call.data == "option1")
async def option1(query: types.CallbackQuery):
    if query.data == 'option1':
        await query.answer("Hello 👋\nIt's Option 2", cache_time = 0)
@dp.callback_query_handler(lambda call: call.data == "option2")
async def option1(query: types.CallbackQuery):
    if query.data == 'option2':
        await query.answer("Hello 👋\nIt's Option 2", cache_time = 0)
@dp.callback_query_handler(lambda call: call.data == "option3")
async def option1(query: types.CallbackQuery):
    if query.data == 'option3':
        await query.answer("Hello 👋\nIt's Option 3", cache_time = 0)
@dp.callback_query_handler(lambda call: call.data == "option4")
async def option1(query: types.CallbackQuery):
    if query.data == 'option4':
        await query.answer("Hello 👋\nIt's Option 4", cache_time = 0)



@dp.message_handler(lambda message: message.text == "Cobalt")
async def show_images(message: types.Message):
    image_car_cobalt = "https://lionmotors.uz/wp-content/uploads/2020/11/cobalt3.jpg"
    caption = "Cobalt 2013\n\n102 000 000 сум\n\nCobalt 2013 probegi 197ming holati yaxshi. Oʻng tomonida krilolar almashgan kapotida petno bor. Udari yuq. Murojaat uchun 88-113-16-12 tel qiling\n\nОпубликовано 17 марта 2024 г."
    await bot.send_photo(message.chat.id, photo=image_car_cobalt ,caption=caption)

@dp.message_handler(lambda message: message.text == "Spark")
async def show_images(message: types.Message):
    image_car_spark = "https://frankfurt.apollo.olxcdn.com/v1/files/w1md5muwybxd-UZ/image;s=1000x700,https://frankfurt.apollo.olxcdn.com/v1/files/z7e4npf0wzc81-UZ/image;s=1000x700"
    caption = ("Spark 2017\n\n102 000 000 сум\n\nChevrolet Spark 2017 год 4-позиция\n\
Пробег 129000 км\n\
Есть крашенные детали\n\
В хорошем состоянии\n\
С кондиционером\n\
Шумка в 4 дверях, пульт Megicar, фары, тонировка\n\n\
Обмен на новый Monza, Gentra или Tracker 2 с моей доплатой\n\n\
Опубликовано 16 марта 2024 г.")
    await bot.send_photo(message.chat.id, photo=image_car_spark ,caption=caption)

@dp.message_handler(lambda message: message.text == "Malibu")
async def show_images(message: types.Message):
    image_car_malibu = "https://frankfurt.apollo.olxcdn.com/v1/files/z5ds36qw5p1n3-UZ/image;s=1000x700"
    caption = ("Chevrolet Malibu\n\n264 440 400 сум\n\nПродаю свою Малибу 2, 2017 год.\n\
двигатель атмосферный,без люка ,\n\
цвет мокрый асфальт, \n\
пробег 119.000 км \n\
С кондиционером\n\
новый аккумулятор,не битая не крашеная ,в машине не курили,полностью покрыта дорогой керамикой. Задняя полусфера затонирована самой дорогой пленкой Llumar.\
Готовая машина, сел и поехал наслаждаться.\n\nОпубликовано 16 марта 2024 г.")
    await bot.send_photo(message.chat.id, photo=image_car_malibu ,caption=caption)

@dp.message_handler(lambda message: message.text == "Nexia (3)")
async def show_images(message: types.Message):
    image_car_nexia = "https://repost.uz/storage/uploads/0-1638800837-mursyaev-post-material.jpeg"
    caption = ("Chevrolet Malibu\n\n116 000 000 сум\n\nПродаю свою Малибу 2, 2017 год.\n\n2019 йли 68400 пробек 116милон Кроска роднуй метан бор 907265760 механика\n\nОпубликовано 11 марта 2024 г.")
    await bot.send_photo(message.chat.id, photo=image_car_nexia,caption=caption)





@dp.message_handler(lambda message: message.text == "KIA K9")
async def show_images(message: types.Message):
    image_car_kia = "https://www.autostrada.uz/wp-content/uploads/2023/07/kia-gotovitsya-nachat-prodazhi-bolshogo-sedana-k9-v-uzbekistane.jpg"
    caption = "K9\n\n869 900 000 сум"
    await bot.send_photo(message.chat.id, photo=image_car_kia,caption=caption)

@dp.message_handler(lambda message: message.text == "KIA EV6")
async def show_images(message: types.Message):
    image_car_kia = "https://stimg.cardekho.com/images/carexteriorimages/930x620/Kia/EV6/8947/1654159762071/front-left-side-47.jpg"
    caption = ("EV6\n\n699 900 000 сум")
    await bot.send_photo(message.chat.id, photo=image_car_kia,caption=caption)

@dp.message_handler(lambda message: message.text == "KIA K5")
async def show_images(message: types.Message):
    image_car_kia = "https://data.favorit-motors.ru/upload/iblock/438/438ebcd1e59de06e4bc5527668c48321.jpg"
    caption = ("K5\n\n359 900 000 сум")
    await bot.send_photo(message.chat.id, photo=image_car_kia,caption=caption)

@dp.message_handler(lambda message: message.text == "KIA K8")
async def show_images(message: types.Message):
    image_car_kia = "https://avatars.mds.yandex.net/get-autoru-vos/1773638/5af19c84a40e0e0e3f11e9387712f759/320x240"
    caption = ("K8\n\n 729 900 000 сум")
    await bot.send_photo(message.chat.id, photo=image_car_kia,caption=caption)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)