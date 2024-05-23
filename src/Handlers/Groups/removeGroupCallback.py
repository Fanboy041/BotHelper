from telebot import types
from Database.MongoDB import get_groups
from Handlers.Groups.removeGroupConfirmCallback import remove_group_confirm_callback

def remove_group_callback(call, bot):
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    if len(list(get_groups())) > 0:
        groups = get_groups()
        for group in groups:
            button = types.InlineKeyboardButton(f"{group['full_name']}", callback_data=f'remove_group_confirm_{group["chat_id"]}')
            keyboard.add(button)


        # Add a "Back" button
        back_button = types.InlineKeyboardButton("Back 🔙", callback_data='groups_menu')
        keyboard.add(back_button)

        bot.edit_message_text("Select a group to remove:", call.message.chat.id, call.message.message_id, reply_markup=keyboard)

    else:
        bot.send_message(call.message.chat.id, "There are no groups.")

    # Remove group confirm button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_group_confirm_'))
    def handle_remove_group_confirm_callback(call):
        remove_group_confirm_callback(call, bot)