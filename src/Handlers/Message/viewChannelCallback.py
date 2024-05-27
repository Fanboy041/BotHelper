from telebot import types
from Database.MongoDB import get_channel
from Handlers.Message.sendChannelCallback import send_channel_callback

def view_channel_callback(call, bot):
    channel_id = int(call.data.split('view_channel_')[1])
    fullname = get_channel(channel_id)['full_name']
    username = get_channel(channel_id)['username']

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    send_button = types.InlineKeyboardButton("Send Message", callback_data=f'send_channel_{channel_id}')
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='show_channels')
    keyboard.add(send_button, back_button)

    bot.edit_message_text(
        f"Channel:\n\nName: <b>{fullname}</b>\nUsername: @{username}\nUserID: <code>{channel_id}</code>\n\nChoose your action.",
        call.message.chat.id,
        call.message.message_id, parse_mode='HTML', reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data.startswith('send_channel_'))
    def handle_send_channel_callback(call):
        send_channel_callback(call, bot)
