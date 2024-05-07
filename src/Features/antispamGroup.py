import json
from telebot import types
from Database.MongoDB import get_group, get_admins

def antispam_group(message, bot):
    if message.chat.type != "private":
        group_id = message.chat.id
        administrators = bot.get_chat_administrators(group_id)
        adminIds = []
        for admin in administrators:
            adminIds.append(admin.user.id)

        if bot.get_me().id in adminIds:
            if get_group(group_id)["is_antispam"] == True:
                if message.text.startswith('http'):
                    bot.delete_message(message.chat.id, message.message_id)

                    keyboard = types.InlineKeyboardMarkup(row_width=2)
                    approve_button = types.InlineKeyboardButton("approve ✔", callback_data='a')
                    disallowed_button =  types.InlineKeyboardButton("disallowed ❌", callback_data='a')
                    keyboard.add(approve_button, disallowed_button)

                    for admin in get_admins():
                        bot.send_message(admin['chat_id'], f"Approv the Link from {message.from_user.first_name }:\n {message.text}", reply_markup=keyboard, parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "can you make me admin please to read all messages and antispam them")