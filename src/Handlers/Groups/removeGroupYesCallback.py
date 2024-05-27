from Database.MongoDB import get_group, delete_group
from Handlers.Back.backToSettingsMenuCallback import back_to_settings_menu_callback

def remove_group_yes_callback(bot, call):
    parts = call.data.split('_')
    group_id = int(parts[3])

    if get_group(group_id):
        if call.message.chat.type != "private":

            bot.delete_message(group_id, call.message.id)

        if call.message.chat.type == "private":

            bot.send_message(call.message.chat.id, f"group with ID {group_id} removed successfully.")


        bot.leave_chat(group_id)
        delete_group(group_id)
    else:
        bot.send_message(call.message.chat.id, f"group with ID {group_id} not found.")

    back_to_settings_menu_callback(call, bot)
