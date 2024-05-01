# settingsCommand.py
from telebot import types

def settings_command(message, bot):
    # Initial message with inline keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    admins_button = types.InlineKeyboardButton("Admins", callback_data='admins')
    channel_button = types.InlineKeyboardButton("Channel", callback_data='channel')
    keyboard.add(admins_button, channel_button)

    bot.send_message(message.chat.id, "📊 Settings:", reply_markup=keyboard)