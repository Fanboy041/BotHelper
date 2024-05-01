# removeChannelCallback.py
from telebot import types
from Database.MongoDB import (get_channel)

def remove_channel_callback(call, bot):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    channel = get_channel()
    button = types.InlineKeyboardButton(f"{channel['full_name']}", callback_data=f'remove_channel_confirm_{channel["chat_id"]}')
    back_to_channel_menu_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_channel_menu')
    keyboard.add(button, back_to_channel_menu_button)

    bot.edit_message_text("Select a channel to remove:", call.message.chat.id, call.message.message_id, reply_markup=keyboard)
