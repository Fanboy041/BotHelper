from telebot import types
from Database.MongoDB import get_admins

def remove_admin_callback(call, bot):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    admins = get_admins()
    for admin in admins:
        button = types.InlineKeyboardButton(f"{admin['full_name']}", callback_data=f'remove_admin_confirm_{admin["chat_id"]}')
        keyboard.add(button)


    # Add a "Back" button
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_admins_menu')
    keyboard.add(back_button)

    bot.edit_message_text("Select an admin to remove:", call.message.chat.id, call.message.message_id, reply_markup=keyboard)
