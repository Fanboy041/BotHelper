# settingsCommand.py
from telebot import types
from Database.MongoDB import get_owner

def settings_command(message, bot):
    user_id = message.from_user.id

    # Check if the user is owner
    owner = get_owner()
    if user_id != owner['chat_id']:
        bot.reply_to(message, "Only the owner is allowed to use this command.")
        return
        
    # Initial message with inline keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    admins_button = types.InlineKeyboardButton("Bot Admins", callback_data='admins')
    channel_button = types.InlineKeyboardButton("Channel", callback_data='channel')
    keyboard.add(admins_button, channel_button)

    bot.send_message(message.chat.id, "📊 Settings:", reply_markup=keyboard)