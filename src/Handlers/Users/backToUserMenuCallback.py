# userCallback.py
from telebot import types

def back_to_user_menu_callback(call, bot):

    # Initial message with inline keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    remove_user = types.InlineKeyboardButton("Remove user ✖️", callback_data='remove_user')
    show_users = types.InlineKeyboardButton("Show users 📝", callback_data='show_users')
    back_to_settings_menu = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_settings_menu')
    keyboard.add(remove_user, show_users, back_to_settings_menu)

    bot.edit_message_text("📊 Users Control Panel:", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')
