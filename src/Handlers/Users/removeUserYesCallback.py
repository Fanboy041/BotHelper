# removeuserYesCallback.py
from Database.MongoDB import get_user, delete_user
from Handlers.Users.removeUserCallback import remove_user_callback

def remove_user_yes_callback(call, bot):
    parts = call.data.split('_')
    # Check if there are enough parts to unpack
    if len(parts) >= 3:
        action, user_id = parts[2], int(parts[3])  # Correct the unpacking

        if action == 'yes':
            # If the callback was yes, remove the user from user collection
            if get_user(                                                                          user_id):
                delete_user(user_id)
                remove_user_callback(call, bot)
                bot.send_message(call.message.chat.id, f"user with ID {user_id} removed successfully.")
            else:
                bot.send_message(call.message.chat.id, f"user with ID {user_id} not found.")
        elif action == 'back':
            remove_user_callback(call, bot)  # Go back to the "Select an user ID to remove:" message
    else:
        bot.send_message(call.message.chat.id, "Invalid action data.")
