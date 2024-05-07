# backToSettingsMenuCallback.py
from telebot import types
from Database.MongoDB import get_owner, get_admin, get_user

def back_to_settings_menu_callback(call, bot):
    user_id = call.message.chat.id
    # Initial message with inline keyboard

    # Check if the user is owner
    owner = get_owner()
    admin = get_admin(user_id) 
    user = get_user(user_id)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    admins_button = types.InlineKeyboardButton("🥷🏼 Bot Admins", callback_data='admins_menu')
    channels_button = types.InlineKeyboardButton("🔈 Channels", callback_data='channels_menu')
    groups_button = types.InlineKeyboardButton("👥 Groups", callback_data='groups_menu')
    users_button = types.InlineKeyboardButton("👤 Users", callback_data='users_menu')
    antispam_button = types.InlineKeyboardButton("📨 Antispam", callback_data='antispam_group_callback')

    if owner['chat_id'] == user_id:
        # Initial message with inline keyboard
        keyboard.add(admins_button, channels_button, groups_button, users_button, antispam_button)

        bot.edit_message_text("📊 Settings:", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')

    elif admin is not None:
        # Initial message with inline keyboard
        keyboard.add(channels_button, groups_button, users_button, antispam_button)

        bot.edit_message_text("📊 Settings:", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')

    elif user is not None:
        bot.send_message(call.message.chat.id, "You are not authorized to use this command.")
