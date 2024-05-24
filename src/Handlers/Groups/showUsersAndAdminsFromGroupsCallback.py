from telebot import types
from Handlers.Groups.kickOrBanOrUnbanUserGroupCallback import kick_ban_unban_callback
from Database.MongoDB import get_group

def show_users_admins_callback(call, bot):
    group_id = int(call.data.split('show_users_admins_')[1])
    # Add a "Back" button
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_groups_menu')

    # Get all users info from the collection and send them as a message to the chat
    print(get_group(group_id)['users'])
    for user in get_group(group_id)['users']:
        member = bot.get_chat_member(group_id, user)
        userFound = member.user
        if userFound.last_name is not None:
            groups_button = types.InlineKeyboardButton(f"{userFound.first_name + " " + userFound.last_name}", callback_data=f'kick_ban_unban_{user}_{group_id}_{userFound.first_name}')
        else:
            groups_button = types.InlineKeyboardButton(f"{userFound.first_name}", callback_data=f'kick_ban_unban_{user}_{group_id}_{userFound.first_name}')

        keyboard.add(groups_button)

    keyboard.add(back_button)
    bot.edit_message_text("Users:\n\n", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')
    # else:
    #     # There is no admins
    #     bot.send_message(call.message.chat.id, "There are no groups.")

    # show users and admins in group button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('kick_ban_unban_'))
    def handle_kick_ban_unban_user_callback(call):
        kick_ban_unban_callback(call, bot)
