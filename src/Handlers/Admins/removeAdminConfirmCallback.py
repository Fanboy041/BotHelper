# removeAdminConfirmCallback.py
from telebot import types
from Database.MongoDB import admin_collection

def remove_admin_confirm_callback(call, bot):
    admin_id = int(call.data.split('remove_admin_confirm_')[1])
    fullname = admin_collection.find_one({'chat_id': admin_id})['full_name']
    username = admin_collection.find_one({'chat_id': admin_id})['username']
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    yes_button = types.InlineKeyboardButton("Yes ✅", callback_data=f'remove_admin_yes_{admin_id}')
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data=f'remove_admin_back_{admin_id}')  # Add a Back button
    keyboard.add(yes_button, back_button)

    bot.edit_message_text(
        f"Are you sure you want to remove this admin:\n\nName: <b>{fullname}</b>\nUsername: @{username}\nUserID: <code>{admin_id}</code>\n\nThis action can't be undone ?",
        call.message.chat.id,
        call.message.message_id, parse_mode='HTML', reply_markup=keyboard
    )
