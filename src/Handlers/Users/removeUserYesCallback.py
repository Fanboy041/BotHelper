from Database.MongoDB import get_user, delete_user
from Handlers.Settings.backToSettingsMenuCallback import back_to_settings_menu_callback

def remove_user_yes_callback(call, bot):
    parts = call.data.split('_')
    user_id = int(parts[3])


    if get_user(user_id):
        delete_user(user_id)

        bot.send_message(call.message.chat.id, f"user with ID {user_id} removed successfully.")
    else:
        bot.send_message(call.message.chat.id, f"user with ID {user_id} not found.")

    back_to_settings_menu_callback(call, bot)