from telebot.types import ChatMemberUpdated
from Database.MongoDB import save_channel, save_group, delete_group, delete_channel

def add_remove_group_channel(chat_member_update: ChatMemberUpdated, bot):
    fullname = chat_member_update.chat.title
    username = chat_member_update.chat.username
    id = chat_member_update.chat.id
    status = chat_member_update.new_chat_member.status
    chatType = chat_member_update.chat.type
    if chatType == 'channel':
        if status == 'member':
            save_channel(fullname, username, id)
            bot.send_message(id, f"I'm glad to join <b>{fullname}</b>!\n\nThank you for interacting with our Telegram bot. We're excited to have you on board 🌹\n\nPlease make sure I'm admin in your Channel so I can assist you.", parse_mode='HTML')

        elif status == 'left':
            delete_channel(id)

    elif chatType == 'supergroup':
        if status == 'member':
            save_group(fullname, username, id)

            bot.send_message(id, f"I'm glad to join <b>{fullname}</b>!\n\nThank you for interacting with our Telegram bot. We're excited to have you on board 🌹\n\nPlease make sure I'm admin in your group so I can assist you.", parse_mode='HTML')
        
        elif status == 'left':
            delete_group(id)
