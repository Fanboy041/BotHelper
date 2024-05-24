from telebot import types
from Database.MongoDB import get_groups

def show_groups_callback(call, bot):
    
    if len(list(get_groups())) > 0:
        groups = get_groups()
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for group in groups:
            button = types.InlineKeyboardButton(f"{group['full_name']}", callback_data=f'view_group_{group["chat_id"]}')
            keyboard.add(button)

        back_button = types.InlineKeyboardButton("Back 🔙", callback_data='groups_menu')
        keyboard.add(back_button)
        
        bot.edit_message_text(
            "Select a group:", call.message.chat.id, call.message.message_id, reply_markup=keyboard
        )
        
    else:
        bot.send_message(call.message.chat.id, "No groups found.")

