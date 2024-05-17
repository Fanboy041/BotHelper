from Database.MongoDB import get_group, delete_group
from Handlers.Groups.removeGroupCallback import remove_group_callback

def remove_group_yes_callback(bot, call):
    parts = call.data.split('_')
    # Check if there are enough parts to unpack
    if len(parts) >= 3:
        action, group_id = parts[2], int(parts[3])  # Correct the unpacking

    if action == 'yes':
        # If the callback was yes, remove the group from group collection
        if get_group(group_id):
            if call.message.chat.type != "private":

                bot.delete_message(group_id, call.message.id)

            if call.message.chat.type == "private":

                bot.send_message(call.message.chat.id, f"group with ID {group_id} removed successfully.")
                remove_group_callback(call, bot)
            
            bot.leave_chat(group_id)
            delete_group(group_id)
        else:
            bot.send_message(call.message.chat.id, f"group with ID {group_id} not found.")
    elif action == 'back':
        remove_group_callback(call, bot)
    else:
        bot.send_message(call.message.chat.id, "Invalid action data.")
