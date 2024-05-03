# removeuserCallback.py
from telebot import types
from Database.MongoDB import get_users

def remove_user_callback(call, bot):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    users = get_users()
    for user in users:
        button = types.InlineKeyboardButton(f"{user['full_name']}", callback_data=f'remove_user_confirm_{user["chat_id"]}')
        keyboard.add(button)


    # Add a "Back" button
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_users_menu')
    keyboard.add(back_button)

    bot.edit_message_text("Select an user to remove:", call.message.chat.id, call.message.message_id, reply_markup=keyboard)
