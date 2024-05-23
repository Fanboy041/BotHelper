from telebot import types
from Database.MongoDB import get_user
from Handlers.Users.removeUserYesCallback import remove_user_yes_callback

def remove_user_confirm_callback(call, bot):
    user_id = int(call.data.split('remove_user_confirm_')[1])
    fullname = get_user(user_id)['full_name']
    username = get_user( user_id)['username']
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    yes_button = types.InlineKeyboardButton("Yes ✅", callback_data=f'remove_user_yes_{user_id}')
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='remove_user')
    keyboard.add(yes_button, back_button)

    bot.edit_message_text(
        f"Are you sure you want to remove this user:\n\nName: <b>{fullname}</b>\nUsername: @{username}\nUserID: <code>{user_id}</code>\n\nThis action can't be undone ?",
        call.message.chat.id,
        call.message.message_id, parse_mode='HTML', reply_markup=keyboard)

    # Remove user yes button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_user_yes_'))
    def handle_remove_user_yes_callback(call):
        remove_user_yes_callback(call, bot)
