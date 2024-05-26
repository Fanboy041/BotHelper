from Database.MongoDB import delete_group

def mute_comment(message, bot):
    if message.content_type == 'new_chat_members':
        new_chat_member = message.new_chat_members[0]
        if new_chat_member.id != bot.get_me().id:
            bot.delete_message(message.chat.id, message.message_id)
    elif message.content_type == 'left_chat_member':
        if message.left_chat_member.id != bot.get_me().id:
            bot.delete_message(message.chat.id, message.message_id)