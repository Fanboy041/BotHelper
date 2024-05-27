from telebot import types
from Database.MongoDB import get_groups

def show_groups_callback(call, bot):
    # Add a "Back" button
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='send_message_menu')

    # Get all groups info from the collection and send them as a message to the chat
    if len(list(get_groups())) > 0:
        groups = get_groups()
        for group in groups:
            button = types.InlineKeyboardButton(f"{group['full_name']}", callback_data=f'send_group_{group["chat_id"]}')
            keyboard.add(button)

        keyboard.add(back_button)
        bot.edit_message_text("Groups:\n\n", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    else:
        bot.send_message(call.message.chat.id, "No groups found.")

