from Database.MongoDB import delete_group

def mute_comment(message, bot):
    chatId = message.chat.id
    if message.content_type == 'new_chat_members':
        new_chat_member = message.new_chat_members[0]
        userId = new_chat_member.id
        username = new_chat_member.username
        if userId != bot.get_me().id:
            bot.delete_message(chatId, message.message_id)
            bot.send_message(message.chat.id, f"Welcome [{userId}](tg://user?id={userId}) @[{username}] in our Group", parse_mode = "Markdown")
            
    elif message.content_type == 'left_chat_member':
        left_chat_memeber = message.left_chat_member
        userId = left_chat_memeber.id
        username = left_chat_memeber.username
        if userId != bot.get_me().id:
            bot.delete_message(chatId, message.message_id)
            bot.send_message(message.chat.id, f"Goodbye Bitch [{userId}](tg://user?id={userId}) @[{username}]", parse_mode = "Markdown")
            