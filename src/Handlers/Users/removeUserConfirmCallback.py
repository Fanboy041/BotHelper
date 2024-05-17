from telebot import types
from Database.MongoDB import get_user

def remove_user_confirm_callback(call, bot):
    user_id = int(call.data.split('remove_user_confirm_')[1])
    fullname = get_user(user_id)['full_name']
    username = get_user( user_id)['username']
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    yes_button = types.InlineKeyboardButton("Yes ✅", callback_data=f'remove_user_yes_{user_id}')
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data=f'remove_user_back_{user_id}')  # Add a Back button
    keyboard.add(yes_button, back_button)

    bot.edit_message_text(
        f"Are you sure you want to remove this user:\n\nName: <b>{fullname}</b>\nUsername: @{username}\nUserID: <code>{user_id}</code>\n\nThis action can't be undone ?",
        call.message.chat.id,
        call.message.message_id, parse_mode='HTML', reply_markup=keyboard)
