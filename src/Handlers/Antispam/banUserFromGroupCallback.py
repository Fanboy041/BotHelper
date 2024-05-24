from datetime import datetime, timedelta
from Database.MongoDB import get_admin, get_user, owner_collection
from telebot import types

def ban_user_from_group_callback(bot, call):
    user_id = int(call.data.split('_')[2])
    group_id = call.data.split('_')[3]

    user_first_name = call.message.text.split("'")[1]
    if "[" in call.message.text:
        text = call.message.text.split("[")[1]
        group_name = call.message.text.split("'")[3]
        text = text.split("]")[0]
    else:
        text = None
    

    owner = None
    userIds = []
    administrators = bot.get_chat_administrators(group_id)
    for admin in administrators:
        userIds.append(admin.user.id)
        if admin.status == "creator":
            owner = admin.user.id

    bot.delete_message(call.message.chat.id, call.message.message_id)                   

    if user_id not in userIds:

        keyboard = types.InlineKeyboardMarkup(row_width=2)
        halfHour_button = types.InlineKeyboardButton("Half an Hour", callback_data='half_hour')
        oneHour_button = types.InlineKeyboardButton("One Hour", callback_data='one_hour')
        oneDay_button = types.InlineKeyboardButton("One Day", callback_data='one_day')
        oneWeek_button = types.InlineKeyboardButton("One Week", callback_data='one_week')
        keyboard.add(halfHour_button, oneHour_button, oneDay_button, oneWeek_button)

        bot.send_message(call.message.chat.id, f"How long would you like to ban this user '{user_first_name}'?", parse_mode='HTML', reply_markup=keyboard)

    else:
        if text is not None:
            bot.send_message(owner, f"i want to ban this admin {user_first_name} [{user_id}](tg://user?id={user_id}), because of sending this Link {text} in this Group {group_name}", parse_mode = "Markdown")
        else:
            bot.send_message(owner, f"i want to ban this admin {user_first_name} [{user_id}](tg://user?id={user_id})", parse_mode = "Markdown")

    
    # ban user from group for half an hour button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('half_hour'))
    def handle_half_an_hour_callback(call):
        ban_and_delete_message_if_success(call, bot, group_id, user_id, admin, text, timedelta(minutes=30))

    # ban user from group for one hour button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('one_hour'))
    def handle_one_hour_callback(call):
        ban_and_delete_message_if_success(call, bot, group_id, user_id, admin, text, timedelta(hours=1))

    # ban user from group for one day button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('one_day'))
    def handle_one_hday_callback(call):
        ban_and_delete_message_if_success(call, bot, group_id, user_id, admin, text, timedelta(days=1))

    # ban user from group for one week button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('one_week'))
    def handle_one_week_callback(call):
        ban_and_delete_message_if_success(call, bot, group_id, user_id, admin, text, timedelta(weeks=1))

def ban_and_delete_message_if_success(call, bot, group_id, user_id, admin, text, time):

    chatPermissions = types.ChatPermissions(can_send_messages= False,
                                                can_send_audios= False,
                                                can_send_documents= False,
                                                can_send_photos= False,
                                                can_send_videos= False,
                                                can_send_video_notes= False,
                                                can_send_voice_notes= False,
                                                can_send_polls= False,
                                                can_send_other_messages= False,
                                                can_add_web_page_previews= False,
                                                can_change_info= False,
                                                can_invite_users= False,
                                                can_pin_messages= False,
                                                can_manage_topics= False
                                                )
    
    bot.restrict_chat_member(group_id, user_id, until_date= int((datetime.now() + time).timestamp()), permissions=chatPermissions)
    bot.delete_message(call.message.chat.id, call.message.message_id) 
    bot.send_message(call.message.chat.id, "Done!")
    
    if get_admin(admin.user.id) is not None or get_user(admin.user.id) is not None or owner_collection.find_one({"chat_id": admin.user.id}) is not None:
        if text is not None:
            bot.send_message(user_id, f"you banned from this group [{group_id}](tg://user?id={group_id}) by sending this Link: \n [{text}]", parse_mode = "Markdown")
        else:
            bot.send_message(user_id, f"you banned from this group [{group_id}](tg://user?id={group_id})", parse_mode = "Markdown")