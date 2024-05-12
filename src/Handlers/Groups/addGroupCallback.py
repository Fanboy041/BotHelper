# addgroupCallback.py
from telebot import types

def add_group_callback(call, bot):
    # Add a "Back" button
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    add_button = types.InlineKeyboardButton("Add Me To Group", url="http://t.me/Doptica_Bot?startgroup=botstart")
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_groups_menu')
    keyboard.add(add_button, back_button)

    bot.edit_message_text("Press (Add Me To Group) button", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')