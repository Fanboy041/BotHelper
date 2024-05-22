from Database.MongoDB import delete_group

def delete_group_chat_id(message, bot):
    
    if message.left_chat_member.username == bot.get_me().username:

        delete_group(message.chat.id)

    else:
        administrators = bot.get_chat_administrators(message.chat.id)

        for admin in administrators:
            if bot.get_me().id == admin.user.id:
                if message.left_chat_member.id != bot.get_me().id:
                    bot.delete_message(message.chat.id, message.message_id)