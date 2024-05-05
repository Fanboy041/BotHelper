from Database.MongoDB import save_group

def add_group_chat_id(message, bot):
    new_chat_member = message.new_chat_members[0]
    group_id = message.chat.id
    group_name = message.chat.title
    group_username = message.chat.username

    if new_chat_member.username == bot.get_me().username:
        # Your bot has been added to a new group
        bot.send_message(message.chat.id, "can you make me admin please")
        save_group(group_name, group_username, group_id)

    administrators = bot.get_chat_administrators(group_id)

    if bot.get_me().id in administrators:
        if new_chat_member.id != bot.get_me().id:
            bot.delete_message(message.chat.id, message.message_id)