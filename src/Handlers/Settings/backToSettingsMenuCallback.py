# backToSettingsMenuCallback.py
from telebot import types

def back_to_settings_menu_callback(call, bot):
    # Initial message with inline keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    admins_button = types.InlineKeyboardButton("🥷🏼 Bot Admins", callback_data='admins_menu')
    channels_button = types.InlineKeyboardButton("🔈 Channels", callback_data='channels_menu')
    groups_button = types.InlineKeyboardButton("👥 Groups", callback_data='groups_menu')
    users_button = types.InlineKeyboardButton("👤 Users", callback_data='users_menu')
    antispam_button = types.InlineKeyboardButton("📨 Antispam", callback_data='antispam')
    keyboard.add(admins_button, channels_button, groups_button, users_button, antispam_button)
    
    bot.edit_message_text("📊 Settings:", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')
