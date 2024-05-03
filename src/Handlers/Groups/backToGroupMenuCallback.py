# groupCallback.py
from telebot import types

def back_to_group_menu_callback(call, bot):

    # Initial message with inline keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    add_group = types.InlineKeyboardButton("Add group 🔈", callback_data='add_group')
    remove_group = types.InlineKeyboardButton("Remove group ✖️", callback_data='remove_group')
    show_group = types.InlineKeyboardButton("Show groups 📝", callback_data='show_groups')
    back_to_settings_menu = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_settings_menu')
    keyboard.add(add_group, remove_group, show_group, back_to_settings_menu)

    bot.edit_message_text("📊 Groups Control Panel:", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')
