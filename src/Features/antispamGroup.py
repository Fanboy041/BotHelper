from telebot import types
from Database.MongoDB import get_group, get_admin, get_user, owner_collection
from Handlers.Antispam.antispamGroupdisallowedCallback import antispam_group_disallowed_callback

def antispam_group(message, bot):
    if message.chat.type != "private":
        group_id = message.chat.id
        administrators = bot.get_chat_administrators(group_id)
        # adminIds = []
        # if bot.get_me().id in adminIds:
        if get_group(group_id)["is_antispam"] == True:
            if bot.get_me().id in (admin.user.id for admin in administrators):
            
                if message.from_user.id not in (admin.user.id for admin in administrators):
                    if message.text.lower().startswith('http') or message.entities is not None:

                        bot.delete_message(message.chat.id, message.message_id)

                        keyboard = types.InlineKeyboardMarkup(row_width=2)
                        approve_button = types.InlineKeyboardButton("approve ✔", callback_data=f'antispam_group_approve_{message.from_user.id}_{message.chat.id}')
                        disallowed_button =  types.InlineKeyboardButton("disallow ❌", callback_data=f'antispam_group_disallowed_{message.from_user.id}_{message.chat.id}')
                        keyboard.add(approve_button, disallowed_button)

                        entities_urls = []
                        for admin in administrators:
                            # adminIds.append(admin.user.id)
                            # for adminId in adminIds:
                            adminId = admin.user.id
                            adminUsername = admin.user.username

                            if message.entities is not None:
                                for entitie in message.entities:
                                    if entitie.type == "text_link":
                                        entities_urls.append(entitie.url)

                            if bot.get_me().id != adminId:
                                if get_admin(adminId) is not None or get_user(adminId) is not None or owner_collection.find_one({"chat_id": adminId}) is not None:
                                    if len(entities_urls) > 0:
                                        bot.send_message(adminId, f"Approv the Link from '{message.from_user.first_name }' in Group '{message.chat.title}' :\n {entities_urls}", reply_markup=keyboard, parse_mode='HTML')
                                    else:
                                        bot.send_message(adminId, f"Approv the Link from '{message.from_user.first_name }' in Group '{message.chat.title}' :\n [{message.text}]", reply_markup=keyboard, parse_mode='HTML')
                                else:
                                    bot.send_message(message.chat.id, f"[{adminId}](tg://user?id={adminId}) @[{adminUsername}]: you are a Admin in this Group, can you start this Bot [{bot.get_me().id}](tg://user?id={bot.get_me().id}) @[{bot.get_me().username}] to approve or disallow the links that the users send" , parse_mode = "Markdown")
            else:
                bot.send_message(message.chat.id, "Please make me admin to activate antispam on uls")


    # antispam group disallowd button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('antispam_group_approve_'))
    @bot.callback_query_handler(func=lambda call: call.data.startswith('antispam_group_disallowed_'))
    def handle_antispam_group_disallowed_callback(call):
        antispam_group_disallowed_callback(bot, call)
