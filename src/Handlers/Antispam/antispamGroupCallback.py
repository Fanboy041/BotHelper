from telebot import types
from Database.MongoDB import get_groups
from Handlers.Antispam.antispamGroupConfirmCallback import antispam_group_confirm_callback

def antispam_group_callback(call, bot):
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    if len(list(get_groups())) > 0:
        groups = get_groups()
        for group in groups:
            if group['is_antispam'] == True:
                status = "✅"
            else:
                status = "❌"
            button = types.InlineKeyboardButton(f"{group['full_name']} - status: {status}", callback_data=f'antispam_group_confirm_{group["chat_id"]}')
            keyboard.add(button)

        back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_options_menu')
        keyboard.add(back_button)

        bot.edit_message_text("Select a group to activate/deactivate antispam:", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')

    else:
        bot.send_message(call.message.chat.id, "There are no groups to edit the antispam function in it.")

    # antispam group confirm button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('antispam_group_confirm_'))
    def handle_antispam_group_confirm_callback(call):
        antispam_group_confirm_callback(call, bot)