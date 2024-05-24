from Database.MongoDB import delete_group, delete_user_from_Group

def delete_group_chat_id(message, bot):
    
    if message.left_chat_member.username == bot.get_me().username:
        # Your bot has been deleted from the group
        delete_group(message.chat.id)
    else:
        delete_user_from_Group(message.chat.id, message.left_chat_member.id)

    administrators = bot.get_chat_administrators(message.chat.id)

    for admin in administrators:
        if bot.get_me().id == admin.user.id:
            if message.left_chat_member.id != bot.get_me().id:
                bot.delete_message(message.chat.id, message.message_id)