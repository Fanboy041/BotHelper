from telebot import types
from Handlers.Users.showUsersCallback import show_users_callback
from Handlers.Users.removeUserCallback import remove_user_callback

def users_menu_callback(call, bot):

    # Initial message with inline keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    remove_user = types.InlineKeyboardButton("Remove user ✖️", callback_data='remove_user')
    show_users = types.InlineKeyboardButton("Show users 📝", callback_data='show_users')
    back_to_settings_menu = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_settings_menu')
    keyboard.add(remove_user, show_users, back_to_settings_menu)

    bot.edit_message_text("📊 Users Control Panel:", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')

    # Show users button
    @bot.callback_query_handler(func=lambda call: call.data == 'show_users')
    def handle_show_users_callback(call):
        show_users_callback(call, bot)

    # Remove user and remove user back button
    @bot.callback_query_handler(func=lambda call: call.data == 'remove_user')
    def handle_remove_user_callback(call):
        remove_user_callback(call, bot)