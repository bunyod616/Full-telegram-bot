from aiogram import types

keyword = types.InlineKeyboardMarkup()
button_1 = types.InlineKeyboardButton(text="Option 1", callback_data="option1")
button_2 = types.InlineKeyboardButton(text="Option 2", callback_data="option2")
button_3 = types.InlineKeyboardButton(text="Option 3", callback_data="option3")
button_4 = types.InlineKeyboardButton(text="Option 4", callback_data="option4")

keyword.add(button_1,button_2)
keyword.add(button_3,button_4)


keyword_click = types.InlineKeyboardMarkup(row_width=2)
keyword_click.add(button_1,button_2)