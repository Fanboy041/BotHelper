# removeGroupYesCallback.py
from Database.MongoDB import group_collection, delete_group
from Handlers.Groups.removeGroupCallback import remove_group_callback

def remove_group_yes_callback(call, bot):
    parts = call.data.split('_')
    # Check if there are enough parts to unpack
    if len(parts) >= 3:
        action, group_id = parts[2], int(parts[3])  # Correct the unpacking

        if action == 'yes':
            # If the callback was yes, remove the group from group collection
            if group_collection.find_one({'chat_id': group_id}):
                delete_group(group_id)
                remove_group_callback(call, bot)
                bot.send_message(call.message.chat.id, f"group with ID {group_id} removed successfully.")
            else:
                bot.send_message(call.message.chat.id, f"group with ID {group_id} not found.")
        elif action == 'back':
            remove_group_callback(call, bot)  # Go back to the "Select an group ID to remove:" message
    else:
        bot.send_message(call.message.chat.id, "Invalid action data.")
