from telebot import types
from Handlers.Admins.addAdminCallback import add_admin_callback
from Handlers.Admins.removeAdminCallback import remove_admin_callback
from Handlers.Admins.showAdminsCallback import show_admins_callback
from Handlers.Settings.backToSettingsMenuCallback import back_to_settings_menu_callback

def admins_callback(call, bot):
    # Initial message with inline keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    add_admin_button = types.InlineKeyboardButton("Add Admin 🥷🏼", callback_data='add_admin')
    remove_admin_button = types.InlineKeyboardButton("Remove Admin ✖️", callback_data='remove_admin')
    show_admins_button = types.InlineKeyboardButton("Show Admins 📝", callback_data='show_admins')
    back_to_settings_menu = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_settings_menu')
    keyboard.add(add_admin_button, remove_admin_button, show_admins_button, back_to_settings_menu)

    bot.edit_message_text("📊 Admins Control Panel:",
                          call.message.chat.id,
                          call.message.message_id,
                          reply_markup=keyboard,
                          parse_mode='Markdown')

    # Add admin button
    @bot.callback_query_handler(func=lambda call: call.data == 'add_admin')
    def handle_add_admin_callback(call):
        add_admin_callback(call, bot)

    # Remove admin button
    @bot.callback_query_handler(func=lambda call: call.data == 'remove_admin')
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_admin_back_'))
    def handle_remove_admin_callback(call):
        remove_admin_callback(call, bot)
    
    # Show admins button
    @bot.callback_query_handler(func=lambda call: call.data == 'show_admins')
    def handle_show_admins_callback(call):
        show_admins_callback(call, bot)

    # Back to settings menu button
    @bot.callback_query_handler(func=lambda call: call.data == 'back_to_settings_menu')
    def handle_back_to_settings_menu_callback(call):
        back_to_settings_menu_callback(call, bot)