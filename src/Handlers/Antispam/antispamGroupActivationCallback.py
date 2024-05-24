
from Database.MongoDB import get_group, group_collection
from Handlers.Settings.backToSettingsMenuCallback import back_to_settings_menu_callback

def antispam_group_activation_callback(bot, call):
    parts = call.data.split('_')
    group_id = int(parts[3])

    if get_group(group_id)["is_antispam"] == False:

        # Check if the bot is not admin in the group
        print(bot.get_chat_member(group_id, bot.get_me().id))
        if bot.get_chat_member(group_id, bot.get_me().id).status == "administrator":
            group_collection.update_one({"chat_id": group_id}, {"$set": {"is_antispam": True}})
            bot.send_message(call.message.chat.id, "Antispam is Activated")
            bot.send_message(group_id, "Antispam is Activated")
        else:
            bot.send_message(call.message.chat.id, "Sorry, can't activate the antispam feature\nPlease promote me to admin in the group at first")

    else: 
        group_collection.update_one({"chat_id": group_id}, {"$set": {"is_antispam": False}})
        bot.send_message(call.message.chat.id, "Antispam is Deactivated")
        bot.send_message(group_id, "Antispam is Deactivated")
    

    back_to_settings_menu_callback(call, bot)