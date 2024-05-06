# addAdminCallback.py
from telebot import types
from Database.MongoDB import save_admin, get_user, delete_user

def add_admin_callback(call, bot):
    # Add a "Back" button
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_admins_menu')
    keyboard.add(back_button)

    bot.edit_message_text(
        "⏩ Forward a message from the user you want to add as an admin.",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=keyboard,
        parse_mode='Markdown'
        )
    # Set the next state to handle the forwarded message
    # bot.register_next_step_handler(call.message, process_admin_forwarded_message, bot)

def process_pressing_back_callback(call, bot):
    if call.data == 'back_to_admins_menu':
        print("hi1")
        bot.clear_step_handler()
    else:
        print("hi2")
        bot.register_next_step_handler(call.message, process_pressing_back_callback, bot)
        print("hi3")

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


