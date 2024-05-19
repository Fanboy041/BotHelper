# settingsCommand.py
from telebot import types
from Database.MongoDB import get_owner, get_admin, get_user

def settings_command(message, bot, handlers):
    if message.chat.type == "private":
        user_id = message.from_user.id

        # 🔥🔥🔥 LET IT BE COMMENTED ALL THE TIME, WHEN WE FINISH WE WILL REMOVE THE COMMENT 🔥🔥🔥

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

            bot.send_message(message.chat.id, "📊 Settings:", reply_markup=keyboard)

        elif admin is not None:
            # Initial message with inline keyboard
            keyboard.add(channels_button, groups_button, users_button, antispam_button)

            bot.send_message(message.chat.id, "📊 Settings:", reply_markup=keyboard)

        elif user is not None:
            bot.send_message(message.chat.id, "You are not authorized to use this command.")
    else:
        bot_username = bot.get_me().username
        if f"@{bot_username}" in message.text:
            bot.reply_to(message, "أهلا بكم في بوت الدعم الرجاء طرح مشكلتكم بشكل واضح ,لن نتأخر في الرد🌹.")
    

    # antispam group and antispam group back button
    @bot.callback_query_handler(func=lambda call: call.data == 'antispam_group_callback')
    @bot.callback_query_handler(func=lambda call: call.data.startswith('antispam_group_back_'))
    def handle_antispam_group_callback(call):
        if 'antispamGroupCallback' in handlers:
            handlers['antispamGroupCallback'].antispam_group_callback(call, bot, handlers)
