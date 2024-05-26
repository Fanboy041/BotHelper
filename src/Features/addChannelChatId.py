from telebot.types import ChatMemberUpdated
from Database.MongoDB import save_channel

def add_channel_chat_id(chat_member_update: ChatMemberUpdated, bot):
    new_chat_member = chat_member_update.new_chat_member
    if chat_member_update.chat.type == 'channel' and new_chat_member.user.id == bot.get_me().id and new_chat_member.status == 'administrator':

        channel_fullname = chat_member_update.chat.title
        channel_username = chat_member_update.chat.username
        channel_id = chat_member_update.chat.id

        save_channel(channel_fullname, channel_username, channel_id)