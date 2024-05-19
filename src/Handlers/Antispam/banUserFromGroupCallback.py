import datetime
from Database.MongoDB import get_admin, get_user, owner_collection
from telebot import types

def ban_user_from_group_callback(bot, call):
    user_id = int(call.data.split('_')[2])
    group_id = call.data.split('_')[3]

    user_first_name = call.message.text.split("'")[1]
    text = call.message.text.split("[")[1]
    group_name = call.message.text.split("'")[3]
    text = text.split("]")[0]

    owner = None
    userIds = []
    administrators = bot.get_chat_administrators(group_id)
    for admin in administrators:
        userIds.append(admin.user.id)
        if admin.status == "creator":
            owner = admin.user.id

    bot.delete_message(call.message.chat.id, call.message.message_id)                   

    if user_id not in userIds:
        bot.send_message(call.message.chat.id, "Done!")

        if get_admin(admin.user.id) is not None or get_user(admin.user.id) is not None or owner_collection.find_one({"chat_id": admin.user.id}) is not None:
            bot.send_message(user_id, f"you ban from this group {group_name} by sending this Link: \n [{text}")

        ChatPermissions = types.ChatPermissions(
        can_send_messages = False,
        can_send_audios = False,
        can_send_documents = False,
        can_send_photos = False,
        can_send_videos = False,
        can_send_video_notes = False,
        can_send_voice_notes = False,
        can_send_polls = False,
        can_send_other_messages = False,
        can_add_web_page_previews = False,
        can_change_info = False,
        can_invite_users = False,
        can_pin_messages = False,
        can_manage_topics = False)

        bot.restrict_chat_member(group_id, user_id, ChatPermissions, {
            datetime.now() + datetime.timedelta(hours=1),
})

    else:
        bot.send_message(owner, f"i want to ban this user {user_first_name} '{user_id}', because of sending this Link {text} in this Group {group_name}")
