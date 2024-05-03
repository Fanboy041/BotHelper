# showAdminsCallback.py
from telebot import types
from Database.MongoDB import get_users

def show_users_callback(call, bot):
    # Add a "Back" button
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_users_menu')
    keyboard.add(back_button)

    # Get all users info from the collection and send them as a message to the chat
    if len(list(get_users())) > 0:
        users = get_users()
        group_list = "\n\n".join([f"<b>{group['full_name']}</b> (@{group['username']})" for group in users])
        bot.edit_message_text("users:\n\n" + group_list, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    else:
        # There is no admins
        bot.send_message(call.message.chat.id, "There are no users.")
