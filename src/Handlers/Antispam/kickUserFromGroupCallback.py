from datetime import datetime, timedelta
from Database.MongoDB import get_admin, get_user, owner_collection
from telebot import types

def kick_user_from_group_callback(bot, call):
    user_id = int(call.data.split('_')[2])
    group_id = call.data.split('_')[3]

    user_first_name = call.message.text.split("'")[1]
    text = call.message.text.split("[")[1]
    group_name = call.message.text.split("'")[3]
    text = text.split("]")[0]

    owner = None
    userIds = []
    administrators = bot.get_chat_administrators(group_id)
    for admin in administrators:
        userIds.append(admin.user.id)
        if admin.status == "creator":
            owner = admin.user.id

    bot.delete_message(call.message.chat.id, call.message.message_id)                   

    if user_id not in userIds:
        bot.send_message(call.message.chat.id, "Done!")

        if get_admin(admin.user.id) is not None or get_user(admin.user.id) is not None or owner_collection.find_one({"chat_id": admin.user.id}) is not None:
            bot.send_message(user_id, f"You've been kicked from this group {group_name} by sending this link:\n\n----------\n\n{text}\n\n----------\n\nGoodbye.")
        bot.ban_chat_member(group_id, user_id)

    else:
        bot.send_message(owner, f"i want to kick this user {user_first_name} '{user_id}', because of sending this Link {text} in this Group {group_name}")
