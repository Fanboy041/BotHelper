# removeChannelCallback.py
from telebot import types
from Database.MongoDB import (get_channel, channel_collection)

def remove_channel_callback(call, bot):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    channels = channel_collection.find()
    channel = channel_collection.find_one()
    for channel in channels:
        button = types.InlineKeyboardButton(f"{channel['full_name']}", callback_data=f'remove_channel_confirm_{channel["chat_id"]}')
        keyboard.add(button)


    # Add a "Back" button
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_channel_menu')
    keyboard.add(back_button)

    bot.edit_message_text("Select an channel to remove:", call.message.chat.id, call.message.message_id, reply_markup=keyboard)