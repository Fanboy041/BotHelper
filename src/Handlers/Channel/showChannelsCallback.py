from telebot import types
from Database.MongoDB import get_channels

def show_channels_callback(call, bot):

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='channels_menu')
    keyboard.add(back_button)

    if len(list(get_channels())) > 0:
        channels = get_channels()
        channel_list = "\n\n".join([f"<b>{channel['full_name']}</b> (@{channel['username']})" for channel in channels])
        bot.edit_message_text("Channels:\n\n" + channel_list, call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='HTML')

    else:
        bot.send_message(call.message.chat.id, "There are no channels.")