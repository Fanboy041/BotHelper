from telebot import types
from Database.MongoDB import get_groups
from Handlers.Groups.showUsersAndAdminsFromGroupsCallback import show_users_admins_callback

def show_groups_callback(call, bot):
    # Add a "Back" button
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='groups_menu')
    keyboard.add(back_button)

    # Get all groups info from the collection and send them as a message to the chat
    if len(list(get_groups())) > 0:
        groups = get_groups()
        # group_list = "\n\n".join([f"<b>{group['full_name']}</b> (@{group['username']})" for group in groups])
        for group in groups: 
            groups_button = types.InlineKeyboardButton(f"{group['full_name']}", callback_data=f'show_users_admins_{group["chat_id"]}')

            keyboard.add(groups_button)
            
        keyboard.add(back_button)
        bot.edit_message_text("Groups:\n\n", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    else:
        # There is no admins
        bot.send_message(call.message.chat.id, "There are no groups.")

    # show users and admins in group button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('show_users_admins_'))
    def handle_show_users_admins_callback(call):
        show_users_admins_callback(call, bot)