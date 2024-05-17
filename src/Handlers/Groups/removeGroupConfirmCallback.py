from telebot import types
from Database.MongoDB import get_group

def remove_group_confirm_callback(call, bot):
    group_id = int(call.data.split('remove_group_confirm_')[1])
    fullname = get_group(group_id)['full_name']
    username = get_group(group_id)['username']
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    yes_button = types.InlineKeyboardButton("Yes ✅", callback_data=f'remove_group_yes_{group_id}')
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data=f'remove_group_back_{group_id}')  # Add a Back button
    keyboard.add(yes_button, back_button)

    bot.edit_message_text(
        f"Are you sure you want to remove this group:\n\nName: <b>{fullname}</b>\nUsername: @{username}\nUserID: <code>{group_id}</code>\n\nThis action can't be undone ?",
        call.message.chat.id,
        call.message.message_id, parse_mode='HTML', reply_markup=keyboard)
