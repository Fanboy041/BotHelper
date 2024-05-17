from telebot import types
from Database.MongoDB import admin_collection

def show_admins_callback(call, bot):
    # Add a "Back" button
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_admins_menu')
    keyboard.add(back_button)

    # Get all admins info from the collection and send them as a message to the chat
    if admin_collection.count_documents({}) > 0:
        admin = admin_collection.find_one()
        admins = admin_collection.find()
        admin_list = "\n\n".join([f"<b>{admin['full_name']}</b> (@{admin['username']})" for admin in admins])
        bot.edit_message_text("Admins:\n\n" + admin_list, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    else:
        # There is no admins
        bot.send_message(call.message.chat.id, "There are no admins.")
