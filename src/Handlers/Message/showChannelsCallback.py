from telebot import types
from Database.MongoDB import get_channels
from .viewChannelCallback import view_channel_callback

def show_channels_callback(call, bot):

    if len(list(get_channels())) > 0:
        channels = get_channels()
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for channel in channels:
            button = types.InlineKeyboardButton(f"{channel['full_name']}",
                                                 callback_data=f'view_channel_{channel["chat_id"]}')
            keyboard.add(button)

        back_button = types.InlineKeyboardButton("Back 🔙", callback_data='send_message_menu')
        keyboard.add(back_button)

        bot.edit_message_text(
            "Select a channel:", call.message.chat.id, call.message.message_id, reply_markup=keyboard
        )

    else:
        bot.send_message(call.message.chat.id, "No channels found.")

    @bot.callback_query_handler(func=lambda call: call.data.startswith('view_channel_'))
    def handle_view_channel_callback(call):
        view_channel_callback(call, bot)

