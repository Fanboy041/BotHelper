# addAdminCallback.py
from telebot import types
from Database.MongoDB import save_admin, get_users, delete_user

def add_admin_callback(call, bot):
    # Add a "Back" button
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_admins_menu')
    keyboard.add(back_button)

    #get all users from the collection and send them as buttons to the chat
    if len(list(get_users())) > 0:
        users = get_users()
        for user in users:
            users_button = types.InlineKeyboardButton(f"{user['full_name']}" , callback_data="hhh")
            keyboard.add(users_button)
        bot.edit_message_text("Users:\n\n", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    else:
        # There is no users
        bot.send_message(call.message.chat.id, "There are no users.")

    # Set the next state to handle the forwarded message
    bot.register_next_step_handler(call.message, process_admin_forwarded_message, bot)

def process_admin_forwarded_message(message, bot):
    try:
        # Check if message.forward_from exists and has necessary attributes
        if message.forward_from and hasattr(message.forward_from, 'id') and hasattr(message.forward_from, 'first_name'):
            # Extract user information from the forwarded message
            user_id = message.forward_from.id
            username = message.forward_from.username
            full_name = (
                f"{message.forward_from.first_name} {message.forward_from.last_name}"
                if message.forward_from.last_name
                else message.forward_from.first_name
            )
            save_admin(full_name, username, user_id)
        else:
            bot.send_message(
                message.chat.id, "Error: The forwarded message doesn't contain valid user information. Make sure the account is not hidden."
            )
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {str(e)}")


