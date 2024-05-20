from telebot import types
from Database.MongoDB import get_owner

def admins_callback(call, bot):
    # Initial message with inline keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    add_admin_button = types.InlineKeyboardButton("Add Admin 🥷🏼", callback_data='add_admin')
    remove_admin_button = types.InlineKeyboardButton("Remove Admin ✖️", callback_data='remove_admin')
    show_admins_button = types.InlineKeyboardButton("Show Admins 📝", callback_data='show_admins')
    back_to_settings_menu = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_settings_menu')
    keyboard.add(add_admin_button, remove_admin_button, show_admins_button, back_to_settings_menu)

    bot.edit_message_text("📊 Admins Control Panel:", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')
