from Database.MongoDB import save_group
def add_group_chat_id(message, bot):
    new_chat_member = message.new_chat_members[0]
    if new_chat_member.username == bot.get_me().username:
        # Your bot has been added to a new group
        group_id = message.chat.id
        group_name = message.chat.title
        group_username = message.chat.username
        print(f"Bot has been added to a new group: {group_name} (ID: {group_id})  (USERNAME: {group_username})")

        save_group(group_name, group_username, group_id)