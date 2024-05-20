from telebot import types
from Database.MongoDB import get_group
from Handlers.Antispam.antispamGroupActivationCallback import antispam_group_activation_callback

def antispam_group_confirm_callback(call, bot):
    group_id = int(call.data.split('antispam_group_confirm_')[1])
    fullname = get_group(group_id)['full_name']
    username = get_group(group_id)['username']
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    back_button = types.InlineKeyboardButton("Back 🔙", callback_data=f'antispam_group_back_{group_id}')  # Add a Back button
    if get_group(group_id)["is_antispam"] == False:
        yes_button = types.InlineKeyboardButton("Activate ✅", callback_data=f'antispam_group_activation_{group_id}')
        keyboard.add(yes_button, back_button)

        bot.edit_message_text(
        f"Do you want to activate antispam on this group?\n\nName: <b>{fullname}</b>\nUsername: @{username}\nUserID: <code>{group_id}</code>\n",
        call.message.chat.id,
        call.message.message_id, parse_mode='HTML', reply_markup=keyboard)
        
    else:
        deactivate_button = types.InlineKeyboardButton("deactivate ❌", callback_data=f'antispam_group_activation_{group_id}')
        keyboard.add(deactivate_button, back_button)
        bot.edit_message_text(
        f"Do you want to deactivate antispam on this group?\n\nName: <b>{fullname}</b>\nUsername: @{username}\nUserID: <code>{group_id}</code>\n",
        call.message.chat.id,
        call.message.message_id, parse_mode='HTML', reply_markup=keyboard)


    # antispam group yes button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('antispam_group_activation_'))
    def handle_antispam_group_yes_callback(call):
        antispam_group_activation_callback(bot, call)
