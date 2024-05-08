from telebot import types
from Database.MongoDB import get_group, get_admins

def antispam_group(message, bot):
    if message.chat.type != "private":
        group_id = message.chat.id
        administrators = bot.get_chat_administrators(group_id)
        adminIds = []
        entities = []
        for admin in administrators:
            adminIds.append(admin.user.id)

        if bot.get_me().id in adminIds:
            if get_group(group_id)["is_antispam"] == True:

                if message.text.startswith('http') or message.link_preview_options is not None:

                    bot.delete_message(message.chat.id, message.message_id)

                    keyboard = types.InlineKeyboardMarkup(row_width=2)
                    approve_button = types.InlineKeyboardButton("approve ✔", callback_data='a')
                    disallowed_button =  types.InlineKeyboardButton("disallowed ❌", callback_data=f'antispam_group_disallowed_{message.from_user.id}_{message.chat.id}')
                    keyboard.add(approve_button, disallowed_button)

                    for admin in get_admins():
                        if message.link_preview_options is not None:
                            for entitie in message.entities:
                                entities.append(entitie.url)
                            print("en", entities)
                            bot.send_message(admin['chat_id'], f"Approv the Link from '{message.from_user.first_name }' in Group '{message.chat.title}' :\n {entities}", reply_markup=keyboard, parse_mode='HTML')
                        else:
                            bot.send_message(admin['chat_id'], f"Approv the Link from '{message.from_user.first_name }' in Group '{message.chat.title}' :\n '{message.text}'", reply_markup=keyboard, parse_mode='HTML')
        else:
            bot.send_message(message.chat.id, "can you make me admin please to read all messages and antispam them")
