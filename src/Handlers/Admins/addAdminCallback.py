# addAdminCallback.py
from telebot import types
from Database.MongoDB import save_admin, get_users, delete_user

def add_admin_callback(call, bot):
    # Add a "Back" button
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_admins_menu')
    

    #get all users from the collection and send them as buttons to the chat
    if len(list(get_users())) > 0:
        users = get_users()
        for user in users:
            users_button = types.InlineKeyboardButton(f"{user['full_name']}" , callback_data="hhh")
            
            keyboard.add(users_button)

        keyboard.add(back_button)
        bot.edit_message_text("Users:\n\n", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    else:
        # There is no users
        bot.send_message(call.message.chat.id, "There are no users.")

