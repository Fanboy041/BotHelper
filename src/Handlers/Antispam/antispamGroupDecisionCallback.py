from telebot import types
from Database.MongoDB import owner_collection, get_admin, get_user
from Handlers.Antispam.kickUserFromGroupCallback import kick_user_from_group_callback
from Handlers.Antispam.banUserFromGroupCallback import ban_user_from_group_callback

def antispam_group_decision_callback(bot, call):
    action = call.data.split('_')[2]

    user_id = int(call.data.split('_')[3])
    group_id = call.data.split('_')[4]

    lines = call.message.text.split('\n')

    group_name = lines[2].split("'")[1]
    user_first_name = lines[3].split("'")[1]
    text = lines[4].split("'")[1]

    adminsIds = []
    administrators = bot.get_chat_administrators(group_id)
    for admin in administrators:
        if bot.get_me().id != admin.user.id:
            if get_admin(admin.user.id) is not None or get_user(admin.user.id) is not None or owner_collection.find_one({"chat_id": admin.user.id}) is not None:
                adminsIds.append(admin.user.id)

    for admin in adminsIds:
        message = bot.send_message(admin, 'Test!')
        bot.delete_message(admin, message.message_id)
        bot.delete_message(admin, message.message_id - len(adminsIds))

    if action == "disallow":
    
        if owner_collection.find_one({"chat_id": user_id}) is None and get_user(user_id) is None and get_admin(user_id) is None:
            if user_id == 1087968824:
                bot.send_message(group_id, f"[{user_id}](tg://user?id={user_id}): this Admin is Annonymous that's the reason why i can't send him a message", parse_mode = "Markdown")
            else:
                bot.send_message(group_id, f"[{user_id}](tg://user?id={user_id}): Start the bot so that you get a message whether the admin has approved or disallowed the link.", parse_mode = "Markdown")
        else:
            bot.send_message(user_id, f"Admin has disallowed your link:\n\n----------\n\n{text}\n\n----------\n\nthat you sent to the group #{group_name}")

        keyboard = types.InlineKeyboardMarkup(row_width=2)
        kickUser_button = types.InlineKeyboardButton("Kick user from Group", callback_data=f'kick_user_{user_id}_{group_id}')
        banUser_button = types.InlineKeyboardButton("Ban user from Group", callback_data=f'ban_user_{user_id}_{group_id}')
        noPenalty_button = types.InlineKeyboardButton("NoPenalty", callback_data=' ')
        keyboard.add(noPenalty_button, kickUser_button, banUser_button)

        bot.send_message(call.message.chat.id, f"You have disallowed this link:\n\n----------\n\n{text}\n\n----------\n\nSender: '{user_first_name}'\n\nGroup: '{group_name}'"+ 
                        f"\n What penalty do you want to impose on this user '{user_first_name}'?", parse_mode='HTML', reply_markup=keyboard)
    
    elif action == "approve":

        if owner_collection.find_one({"chat_id": user_id}) is None and get_user(user_id) is None and get_admin(user_id) is None:
            if user_id == 1087968824:
                bot.send_message(group_id, f"[{user_id}](tg://user?id={user_id}): this Admin is Annonymous, that's the reason why i can't send him a message", parse_mode = "Markdown")
            else:
                bot.send_message(group_id, f"[{user_id}](tg://user?id={user_id}): Start the bot so that you get a message whether the admin has approved or disallowed the link.", parse_mode = "Markdown")
        else:
            bot.send_message(user_id, f"Admin has approved your link:\n\n----------\n\n{text}\n\n----------\n\nthat you sent to the group #{group_name}")

        bot.send_message(call.message.chat.id, f"Great, you have approved this link: {text}\n\nthat sent from: [{user_first_name}](tg://user?id={user_id})")
        bot.send_message(group_id, f"Admin has approved [{user_first_name}](tg://user?id={user_id})'s message:\n\n----------\n\n{text}\n\n----------", parse_mode = "Markdown")
        
    # kick user from group button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('kick_user_'))
    def handle_kick_user_from_group_callback(call):
        kick_user_from_group_callback(bot, call)

    # ban user from group button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('ban_user_'))
    def handle_ban_user_from_group_callback(call):
        ban_user_from_group_callback(bot, call)