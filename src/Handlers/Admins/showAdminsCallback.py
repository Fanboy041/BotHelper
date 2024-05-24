from telebot import types
from Database.MongoDB import get_admins

def show_admins_callback(call, bot):
    # Add a "Back" button
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='admins_menu')
    keyboard.add(back_button)

    # Get all admins info from the collection and send them as a message to the chat
    if len(list(get_admins())) > 0:
        admins = get_admins()
        admin_list = "\n\n".join([f"<b>{admin['full_name']}</b> (@{admin['username']})" for admin in admins])
        bot.edit_message_text("Admins:\n\n" + admin_list, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    else:
        # There is no admins
        bot.send_message(call.message.chat.id, "There are no admins.")
