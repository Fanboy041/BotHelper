from telebot import types
from Database.MongoDB import get_users
from Handlers.Users.removeUserConfirmCallback import remove_user_confirm_callback

def remove_user_callback(call, bot):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    users = get_users()
    for user in users:
        button = types.InlineKeyboardButton(f"{user['full_name']}", callback_data=f'remove_user_confirm_{user["chat_id"]}')
        keyboard.add(button)


    # Add a "Back" button
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='users_menu')
    keyboard.add(back_button)

    bot.edit_message_text("Select an user to remove:", call.message.chat.id, call.message.message_id, reply_markup=keyboard)

    # Remove user confirm button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_user_confirm_'))
    def handle_remove_user_confirm_callback(call):
        remove_user_confirm_callback(call, bot)