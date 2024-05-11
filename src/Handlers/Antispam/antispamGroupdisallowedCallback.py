from telebot import types
from Database.MongoDB import owner_collection, get_admin, get_user, get_owner

def antispam_group_disallowed_callback(bot, call):
    action = call.data.split('_')[2]

    user_id = int(call.data.split('_')[3])
    group_id = call.data.split('_')[4]

    user_first_name = call.message.text.split("'")[1]
    text = call.message.text.split("[")[1]
    group_name = call.message.text.split("'")[3]

    admins = []
    administrators = bot.get_chat_administrators(group_id)
    for admin in administrators:
        if bot.get_me().id != admin.user.id:
            if get_admin(admin.user.id) is not None or get_user(admin.user.id) is not None or owner_collection.find_one({"chat_id": admin.user.id}) is not None:
                admins.append(admin)

    for admin in administrators:
        if bot.get_me().id != admin.user.id:
            if get_admin(admin.user.id) is not None or get_user(admin.user.id) is not None or owner_collection.find_one({"chat_id": admin.user.id}) is not None:
                message = bot.send_message(admin.user.id, 'Test!')
                bot.delete_message(admin.user.id, message.message_id)
                print(len(admins) - 1)
                print(admin.user.id)
                bot.delete_message(admin.user.id, message.message_id - len(admins))

    if action == "disallowed":
    
        if owner_collection.find_one({"chat_id": user_id}) is None and get_user(user_id) is None and get_admin(user_id) is None:
            
            bot.send_message(group_id, f"[{user_id}](tg://user?id={user_id}): Start the bot so that you get a message whether the admin has approved or disallowed the link and send your Link again to test it", parse_mode = "Markdown")
        else:
            bot.send_message(user_id, f"Admin has disallowed this Link: \n [{text} \n that you sent to the group {group_name}")

        keyboard = types.InlineKeyboardMarkup(row_width=2)
        KickUser_button = types.InlineKeyboardButton("Kick user from Group", callback_data=f'kick_user_{user_id}_{group_id}')
        NoPenalty_button = types.InlineKeyboardButton("NoPenalty", callback_data=' ')
        keyboard.add(NoPenalty_button, KickUser_button)

        bot.send_message(call.message.chat.id, f"you have disallowed this Link: \n [{text} \n that sent from '{user_first_name}' to the group '{group_name}'"+ 
                        f"\n What penalty do you want to impose on this user '{user_first_name}'?", parse_mode='HTML', reply_markup=keyboard)
    
    elif action == "approve":

        if owner_collection.find_one({"chat_id": user_id}) is None and get_user(user_id) is None and get_admin(user_id) is None:
            
            bot.send_message(group_id, f"[{user_id}](tg://user?id={user_id}): Start the bot so that you get a message whether the admin has approved or disallowed the link and send your Link again to test it", parse_mode = "Markdown")
        else:
            bot.send_message(call.message.chat.id, f"you have approve this Link: \n [{text} \n that sent from {user_first_name}")
            bot.send_message(user_id, f"Admin has approve this Link: \n [{text} \n that you sent to the group {group_name}")
            bot.send_message(group_id, f"Admin has approve this Link: \n [{text} \n that [{user_id}](tg://user?id={user_id}) sent", parse_mode = "Markdown")