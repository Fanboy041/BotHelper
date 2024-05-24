from telebot import types
from Handlers.Antispam.kickUserFromGroupCallback import kick_user_from_group_callback
from Handlers.Antispam.banUserFromGroupCallback import ban_user_from_group_callback

def kick_ban_unban_callback(call, bot):
    user_id = int(call.data.split('_')[3])
    group_id = call.data.split('_')[4]
    username = call.data.split('_')[5]

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_groups_menu')
    kickUser_button = types.InlineKeyboardButton("Kick user from Group", callback_data=f'kick_user_{user_id}_{group_id}')
    banUser_button = types.InlineKeyboardButton("Ban user from Group", callback_data=f'ban_user_{user_id}_{group_id}')
    noPenalty_button = types.InlineKeyboardButton("Unban user from Group", callback_data=f'unban_user_{user_id}_{group_id}')
    keyboard.add(noPenalty_button, kickUser_button, banUser_button, back_button)

    bot.edit_message_text(f"What penalty do you want to impose on this user '{username}'?", call.message.chat.id, call.message.message_id,
                            reply_markup=keyboard, parse_mode='HTML')

    # kick user from group button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('kick_user_'))
    def handle_kick_user_from_group_callback(call):
        kick_user_from_group_callback(bot, call)

    # ban user from group button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('ban_user_'))
    def handle_ban_user_from_group_callback(call):
        ban_user_from_group_callback(bot, call)