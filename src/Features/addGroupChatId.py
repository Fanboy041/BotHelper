from Database.MongoDB import save_group

def add_group_chat_id(message, bot):
    new_chat_member = message.new_chat_members[0]
    group_id = message.chat.id
    group_name = message.chat.title
    group_username = message.chat.username

    if new_chat_member.username == bot.get_me().username:
        save_group(group_name, group_username, group_id)
        bot.send_message(message.chat.id, f"I'm glad to join <b>{group_name}</b>!\n\nThank you for interacting with our Telegram bot. We're excited to have you on board 🌹\n\nPlease make sure I'm admin in your group so I can assist you.", parse_mode='HTML')

    administrators = bot.get_chat_administrators(group_id)

    for admin in administrators:
        if bot.get_me().id == admin.user.id:
            if new_chat_member.id != bot.get_me().id:
                bot.delete_message(message.chat.id, message.message_id)