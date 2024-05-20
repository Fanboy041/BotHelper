from Database.MongoDB import admin_collection
from Handlers.Settings.backToSettingsMenuCallback import back_to_settings_menu_callback


def remove_admin_yes_callback(call, bot):
    parts = call.data.split('_')
    # Check if there are enough parts to unpack
    if len(parts) >= 3:
        action, admin_id = parts[2], int(parts[3])  # Correct the unpacking

        if action == 'yes':
            # If the callback was yes, remove the admin from admin collection
            if admin_collection.find_one({'chat_id': admin_id}):
                admin_collection.delete_one({'chat_id': admin_id})
                bot.send_message(call.message.chat.id, f"Admin with ID {admin_id} removed successfully.")
            else:
                bot.send_message(call.message.chat.id, f"Admin with ID {admin_id} not found.")

            back_to_settings_menu_callback(call, bot)  # Go back to the "Select an admin ID to remove:" message
    else:
        bot.send_message(call.message.chat.id, "Invalid action data.")
