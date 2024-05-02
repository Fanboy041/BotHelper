# muteJoinedGroupMembers.py
def delete_join_message(message, bot):
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except:
        if message.new_chat_member.id != bot.get_me().id:
            bot.send_message(message.chat.id, "Please make me an admin to remove the join and leave messages in this group!")
        else:
            bot.send_message(message.chat.id, "Hi! I am your trusty GroupSilencer Bot! Thanks for adding me! To use me, make me an admin, and I will be able to delete all the pesky notifications when a member joins or leaves the group!")