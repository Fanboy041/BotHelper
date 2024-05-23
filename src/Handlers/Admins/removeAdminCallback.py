from telebot import types
from Database.MongoDB import get_admins
from Handlers.Admins.removeAdminConfirmCallback import remove_admin_confirm_callback

def remove_admin_callback(call, bot):

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
        # There is no admins
        bot.send_message(call.message.chat.id, "There are no admins.")
    
    # Remove admin confirm button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_admin_confirm_'))
    def handle_remove_admin_confirm_callback(call):
        remove_admin_confirm_callback(call, bot)
