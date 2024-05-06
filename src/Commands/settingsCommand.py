# settingsCommand.py
from telebot import types
from Database.MongoDB import get_owner

def settings_command(message, bot):
    user_id = message.from_user.id

    # 🔥🔥🔥 LET IT BE COMMENTED ALL THE TIME, WHEN WE FINISH WE WILL REMOVE THE COMMENT 🔥🔥🔥

    # # Check if the user is owner
    # owner = get_owner(user_id)
    # if user_id != owner['chat_id']:
    #     bot.reply_to(message, "Only the owner is allowed to use this command.")
    #     return
        
    # Initial message with inline keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    admins_button = types.InlineKeyboardButton("🥷🏼 Bot Admins", callback_data='admins_menu')
    channels_button = types.InlineKeyboardButton("🔈 Channels", callback_data='channels_menu')
    groups_button = types.InlineKeyboardButton("👥 Groups", callback_data='groups_menu')
    users_button = types.InlineKeyboardButton("👤 Users", callback_data='users_menu')
    keyboard.add(admins_button, channels_button, groups_button, users_button)

    bot.send_message(message.chat.id, "📊 Settings:", reply_markup=keyboard)