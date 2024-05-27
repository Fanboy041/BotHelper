from telebot import types
from Database.MongoDB import get_owner, get_user

def back_to_options_menu_callback(call, bot):

    user_id = call.message.chat.id
    owner = get_owner()
    user = get_user(user_id)

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    send_message_button = types.InlineKeyboardButton("💬 Send Message", callback_data='send_message_menu')
    antispam_button = types.InlineKeyboardButton("📨 Antispam", callback_data='antispam_group')

    if owner['chat_id'] == user_id:
        # Initial message with inline keyboard
        keyboard.add(send_message_button, antispam_button)

        bot.edit_message_text("⛓ Welcome to options menu:\n\n<i>💬 Send Message</i>: Send messages to channels, groups and users.\n\n<i>📨 Antispam</i>: To activate/deactivate urls in your groups.\n", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')

    else:
        bot.send_message(call.message.chat.id, "You are not authorized to use this command.")
