# showAdminsCallback.py
from telebot import types
from Database.MongoDB import get_groups

def show_groups_callback(call, bot):
    # Add a "Back" button
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_groups_menu')
    keyboard.add(back_button)

    # Get all groups info from the collection and send them as a button to the chat
    if len(list(get_groups())) > 0:
        groups = get_groups()
        for group in groups:
            groups_button = types.InlineKeyboardButton(f"{group['full_name']}" , callback_data="hhh")
            keyboard.add(groups_button)
        bot.edit_message_text("Groups:\n\n", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    else:
        # There is no admins
        bot.send_message(call.message.chat.id, "There are no groups.")
