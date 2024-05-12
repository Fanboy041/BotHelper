from telebot import types
from Database.MongoDB import get_group, get_admin, get_user, owner_collection

def antispam_group(message, bot):
    if message.chat.type != "private":
        group_id = message.chat.id
        administrators = bot.get_chat_administrators(group_id)
        adminIds = []
        entities_urls = []
        for admin in administrators:
            adminIds.append(admin.user.id)

        if bot.get_me().id in adminIds:
            if get_group(group_id)["is_antispam"] == True:

                if message.text.lower().startswith('http') or message.entities is not None:

                    bot.delete_message(message.chat.id, message.message_id)

                    keyboard = types.InlineKeyboardMarkup(row_width=2)
                    approve_button = types.InlineKeyboardButton("approve ✔", callback_data=f'antispam_group_approve_{message.from_user.id}_{message.chat.id}')
                    disallowed_button =  types.InlineKeyboardButton("disallow ❌", callback_data=f'antispam_group_disallowed_{message.from_user.id}_{message.chat.id}')
                    keyboard.add(approve_button, disallowed_button)

                    for adminId in adminIds:
                        if message.entities is not None:
                            for entitie in message.entities:
                                if entitie.type == "text_link":
                                    entities_urls.append(entitie.url)

                        if bot.get_me().id != adminId:
                            if get_admin(adminId) is not None or get_user(adminId) is not None or owner_collection.find_one({"chat_id": adminId}) is not None:
                                if len(entities_urls) > 0:
                                    message1 = bot.send_message(adminId, f"Approv the Link from '{message.from_user.first_name }' in Group '{message.chat.title}' :\n {entities_urls}", reply_markup=keyboard, parse_mode='HTML')
                                    print(adminId)
                                    print(message1.message_id)
                                else:
                                    message1 = bot.send_message(adminId, f"Approv the Link from '{message.from_user.first_name }' in Group '{message.chat.title}' :\n [{message.text}]", reply_markup=keyboard, parse_mode='HTML')
                                    print(adminId)
                                    print(message1.message_id)
                            else:
                                bot.send_message(message.chat.id, f"[{adminId}](tg://user?id={adminId}): you are a Admin in this Group, can you start this Bot [{bot.get_me().id}](tg://user?id={bot.get_me().id}) to approve or disallow the links that the users send" , parse_mode = "Markdown")
        else:
            bot.send_message(message.chat.id, "can you make me admin please to read all messages and antispam them")
