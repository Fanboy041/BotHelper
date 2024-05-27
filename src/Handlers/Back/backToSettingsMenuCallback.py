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

    if owner['chat_id'] == user_id:
        # Initial message with inline keyboard
        keyboard.add(admins_button, channels_button, groups_button)

        bot.edit_message_text("🎚 Welcome to the settings menu:\n\n<i>🥷🏼 Bot Admins</i>: To manage the admins in this bot\n\n<i>🔈 Channels</i>: To manage the channels that the bot controls\n\n<i>👥 Groups</i>: To manage the groups that the bot controls\n", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')

    elif admin is not None:
        # Initial message with inline keyboard
        keyboard.add(channels_button, groups_button)

        bot.edit_message_text("🎚 Welcome to the settings menu:\n\n<i>🔈 Channels</i>: To manage the channels that the bot controls\n\n<i>👥 Groups</i>: To manage the groups that the bot controls\n", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')

    elif user is not None:
        bot.send_message(call.message.chat.id, "You are not authorized to use this command.")
