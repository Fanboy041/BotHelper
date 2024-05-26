from telebot import types
from Database.MongoDB import get_owner, get_admin, get_user
from Handlers.Admins.adminsMenuCallback import admins_callback
from Handlers.Channel.channelsMenuCallback import channels_menu_callback
from Handlers.Groups.groupsMenuCallback import groups_menu_callback
from Handlers.Users.usersMenuCallback import users_menu_callback
from Handlers.Antispam.antispamGroupCallback import antispam_group_callback
from Handlers.Settings.backToSettingsMenuCallback import back_to_settings_menu_callback

def settings_command(message, bot):
    if message.chat.type == "private":
        user_id = message.from_user.id

        # Check if the user is owner
        owner = get_owner()
        admin = get_admin(user_id)
        user = get_user(user_id)

        # Create inline keyboard and locks the row width to 2
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        admins_button = types.InlineKeyboardButton("🥷🏼 Bot Admins", callback_data='admins_menu')
        channels_button = types.InlineKeyboardButton("🔈 Channels", callback_data='channels_menu')
        groups_button = types.InlineKeyboardButton("👥 Groups", callback_data='groups_menu')
        users_button = types.InlineKeyboardButton("👤 Users", callback_data='users_menu')
        antispam_button = types.InlineKeyboardButton("📨 Antispam", callback_data='antispam_group')

        if owner['chat_id'] == user_id:
            # Initial message with inline keyboard
            keyboard.add(admins_button, channels_button, groups_button, users_button, antispam_button)

            bot.send_message(message.chat.id, "📊 Welcome to the settings menu:\n\n<i>🥷🏼 Bot Admins</i>: To manage the admins in this bot\n\n<i>🔈 Channels</i>: To manage the channels that the bot controls\n\n<i>👥 Groups</i>: To manage the groups that the bot controls\n\n<i>👤 Users</i>: To manage the users that they started the bot\n\n<i>📨 Antispam</i>: To activate/deactivate urls in your groups\n", reply_markup=keyboard, parse_mode='HTML')

        elif admin is not None:
            # Initial message with inline keyboard
            keyboard.add(channels_button, groups_button, users_button, antispam_button)

            bot.send_message(message.chat.id, "📊 Welcome to the settings menu:\n\n<i>🔈 Channels</i>: To manage the channels that the bot controls\n\n<i>👥 Groups</i>: To manage the groups that the bot controls\n\n<i>👤 Users</i>: To manage the users that they started the bot\n\n<i>📨 Antispam</i>: To activate/deactivate urls in your groups\n", reply_markup=keyboard, parse_mode='HTML')

        elif user is not None:
            bot.send_message(message.chat.id, "You are not authorized to use this command.")
    else:
        bot_username = bot.get_me().username
        if f"@{bot_username}" in message.text:
            bot.reply_to(message, "Please run the command in private")

    # Admins menu and back to Admins menu button
    @bot.callback_query_handler(func=lambda call: call.data == 'admins_menu')
    def handle_admins_callback(call):
        admins_callback(call, bot)

    # Channels menu and back to Channels menu button
    @bot.callback_query_handler(func=lambda call: call.data == 'channels_menu')
    def handle_channel_callback(call):
        channels_menu_callback(call, bot)

    # Groups menu and back to Groups menu button
    @bot.callback_query_handler(func=lambda call: call.data == 'groups_menu')
    def handle_group_callback(call):
        groups_menu_callback(call, bot)

    # Users menu and back to users menu button
    @bot.callback_query_handler(func=lambda call: call.data == 'users_menu')
    def handle_user_menu_callback(call):
        users_menu_callback(call, bot)

    # Antispam group and back to Antispam group button
    @bot.callback_query_handler(func=lambda call: call.data == 'antispam_group')
    def handle_antispam_group_callback(call):
        antispam_group_callback(call, bot)

    @bot.callback_query_handler(func=lambda call: call.data == 'back_to_settings_menu')
    def handle_back_to_settings_menu_callback(call):
        back_to_settings_menu_callback(call, bot)