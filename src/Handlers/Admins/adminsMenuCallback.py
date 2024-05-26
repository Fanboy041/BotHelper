
#todo: This file need to be checked for the clean code

from telebot import types
from Database.MongoDB import get_user, get_users, get_admin, get_admins, save_admin, delete_admin
from Handlers.Settings.backToSettingsMenuCallback import back_to_settings_menu_callback

def admins_callback(call, bot):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    add_admin_button = types.InlineKeyboardButton("Add Admin 🥷🏼", callback_data='add_admin')
    remove_admin_button = types.InlineKeyboardButton("Remove Admin ✖️", callback_data='remove_admin')
    back_to_settings_menu = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_settings_menu')
    keyboard.add(add_admin_button, remove_admin_button, back_to_settings_menu)

    bot.edit_message_text("📊 Admins Control Panel:",
                          call.message.chat.id,
                          call.message.message_id,
                          reply_markup=keyboard,
                          parse_mode='Markdown')

    # Add admin button
    @bot.callback_query_handler(func=lambda call: call.data == 'add_admin')
    def add_admin_callback(call):
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        back_button = types.InlineKeyboardButton("Back 🔙", callback_data='admins_menu')
        

        # Get all users from the collection and send them as buttons to the chat
        if len(list(get_users())) > 0:
            users = get_users()
            for user in users:
                users_button = types.InlineKeyboardButton(f"{user['full_name']}", callback_data=f'add_admin_confirm_{user["chat_id"]}')
                
                keyboard.add(users_button)

            keyboard.add(back_button)
            bot.edit_message_text("Users:\n\n", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
        else:
            bot.send_message(call.message.chat.id, "There are no users.")

    # Remove admin button
    @bot.callback_query_handler(func=lambda call: call.data == 'remove_admin')
    def remove_admin_callback(call):

        keyboard = types.InlineKeyboardMarkup(row_width=1)

        if len(list(get_admins())) > 0:
            admins = get_admins()
            for admin in admins:
                button = types.InlineKeyboardButton(f"{admin['full_name']}", callback_data=f'remove_admin_confirm_{admin["chat_id"]}')
                keyboard.add(button)
            
            back_button = types.InlineKeyboardButton("Back 🔙", callback_data='admins_menu')
            keyboard.add(back_button)

            bot.edit_message_text("Select an admin to remove:",
                                call.message.chat.id,
                                call.message.message_id,
                                reply_markup=keyboard)

        else:
            bot.send_message(call.message.chat.id, "There are no admins.")

    # Make user admin in Bot button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('add_admin_confirm_'))
    def add_admin_confirm_callback(call):
        admin_id = int(call.data.split('add_admin_confirm_')[1])
        fullname = get_user(admin_id)['full_name']
        username = get_user(admin_id)['username']
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        yes_button = types.InlineKeyboardButton("Yes ✅", callback_data=f'add_admin_yes_{admin_id}')
        back_button = types.InlineKeyboardButton("Back 🔙", callback_data=f'add_admin')
        keyboard.add(yes_button, back_button)

        bot.edit_message_text(
            f"Are you sure you want to add this admin:\n\nName: <b>{fullname}</b>\nUsername: @{username}\nUserID: <code>{admin_id}</code>\n\nThis action can't be undone ?",
            call.message.chat.id,
            call.message.message_id, parse_mode='HTML', reply_markup=keyboard
        )

    # Add admin yes button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('add_admin_yes_'))
    def handle_add_admin_yes_callback(call):
        parts = call.data.split('_')
        user_id = int(parts[3])
        user = get_user(user_id)
        username = user['username']
        full_name = user['full_name']
        save_admin(full_name, username, user_id)
        
        back_to_settings_menu_callback(call, bot)

        # Remove admin confirm button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_admin_confirm_'))
    def remove_admin_confirm_callback(call):
        admin_id = int(call.data.split('remove_admin_confirm_')[1])
        fullname = get_admin(admin_id)['full_name']
        username = get_admin(admin_id)['username']
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        yes_button = types.InlineKeyboardButton("Yes ✅", callback_data=f'remove_admin_yes_{admin_id}')
        back_button = types.InlineKeyboardButton("Back 🔙", callback_data=f'remove_admin')
        keyboard.add(yes_button, back_button)

        bot.edit_message_text(
            f"Are you sure you want to remove this admin:\n\nName: <b>{fullname}</b>\nUsername: @{username}\nUserID: <code>{admin_id}</code>\n\nThis action can't be undone ?",
            call.message.chat.id,
            call.message.message_id, parse_mode='HTML', reply_markup=keyboard
        )

    # Remove admin yes button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_admin_yes_'))
    def handle_remove_admin_yes_callback(call):
        parts = call.data.split('_')
        admin_id = int(parts[3])

        delete_admin(admin_id)

        back_to_settings_menu_callback(call, bot)