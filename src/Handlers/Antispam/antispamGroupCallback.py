from telebot import types
from Database.MongoDB import get_groups

def antispam_group_callback(call, bot):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    groups = get_groups()
    for group in groups:
        button = types.InlineKeyboardButton(f"{group['full_name']}", callback_data=f'antispam_group_confirm_{group["chat_id"]}')
        keyboard.add(button)

    # Add a "Back" button
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_settings_menu')
    keyboard.add(back_button)

    bot.edit_message_text("Select a group to Antispam:", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')