from telebot import types
from Database.MongoDB import get_owner, get_admin, get_user
from Handlers.Message.sendMessageMenuCallback import send_message_menu_callback
from Handlers.Antispam.antispamGroupCallback import antispam_group_callback
from Handlers.Back.backToOptionsMenuCallback import back_to_options_menu_callback

def options_command(message, bot):
    if message.chat.type == "private":
        user_id = message.from_user.id

        owner = get_owner()
        admin = get_admin(user_id)
        user = get_user(user_id)

        keyboard = types.InlineKeyboardMarkup(row_width=2)
        send_message_button = types.InlineKeyboardButton("💬 Send Message", callback_data='send_message_menu')
        antispam_button = types.InlineKeyboardButton("📨 Antispam", callback_data='antispam_group')

        if owner['chat_id'] == user_id:

            keyboard.add(send_message_button, antispam_button)
            bot.send_message(message.chat.id, "⛓ Welcome to options menu:\n\n<i>💬 Send Message</i>: Send messages to channels, groups and users.\n\n<i>📨 Antispam</i>: To activate/deactivate urls in your groups.\n", reply_markup=keyboard, parse_mode='HTML')

        else:

            bot.send_message(message.chat.id, "You are not authorized to use this command.")

    else:
        bot_username = bot.get_me().username
        if f"@{bot_username}" in message.text:
            bot.reply_to(message, "Please run the command in private")

    # Send message button
    @bot.callback_query_handler(func=lambda call: call.data == 'send_message_menu')
    def handle_send_message_menu_callback(call):
        send_message_menu_callback(call, bot)

    # Antispam group and back to Antispam group button
    @bot.callback_query_handler(func=lambda call: call.data == 'antispam_group')
    def handle_antispam_group_callback(call):
        antispam_group_callback(call, bot)

    # Back to options menu button
    @bot.callback_query_handler(func=lambda call: call.data == 'back_to_options_menu')
    def handle_back_to_options_menu_callback(call):
        back_to_options_menu_callback(call, bot)