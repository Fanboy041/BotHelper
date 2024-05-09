from Database.MongoDB import owner_collection, get_admin, get_user, get_admins

def antispam_group_disallowed_callback(bot, call):
    action = call.data.split('_')[2]

    user_id = int(call.data.split('_')[3])
    group_id = call.data.split('_')[4]

    user_first_name = call.message.text.split("'")[1]
    text = call.message.text.split("[")[1]
    group_name = call.message.text.split("'")[3]

    bot.delete_message(call.message.chat.id, call.message.message_id)

    if action == "disallowed":
    
        if owner_collection.find_one({"chat_id": user_id}) is None and get_user(user_id) is None and get_admin(user_id) is None:
            
            bot.send_message(group_id, f"[{user_id}](tg://user?id={user_id}): Start the bot so that you get a message whether the admin has approved or disallowed the link and send your Link again to test it", parse_mode = "Markdown")
        else:
            bot.send_message(call.message.chat.id, f"you have disallowed this Link: \n [{text} \n that sent from {user_first_name}")
            bot.send_message(user_id, f"Admin has disallowed this Link: \n [{text} \n that you sent to the group {group_name}")
    
    elif action == "approve":

        if owner_collection.find_one({"chat_id": user_id}) is None and get_user(user_id) is None and get_admin(user_id) is None:
            
            bot.send_message(group_id, f"[{user_id}](tg://user?id={user_id}): Start the bot so that you get a message whether the admin has approved or disallowed the link and send your Link again to test it", parse_mode = "Markdown")
        else:
            bot.send_message(call.message.chat.id, f"you have approve this Link: \n [{text} \n that sent from {user_first_name}")
            bot.send_message(user_id, f"Admin has approve this Link: \n [{text} \n that you sent to the group {group_name}")
            bot.send_message(group_id, f"Admin has approve this Link: \n [{text} \n that [{user_id}](tg://user?id={user_id}) sent", parse_mode = "Markdown")