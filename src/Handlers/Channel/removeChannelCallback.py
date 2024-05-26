from telebot import types
from Database.MongoDB import get_channels
from Handlers.Channel.removeChannelConfirmCallback import remove_channel_confirm_callback

def remove_channel_callback(call, bot):
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    if len(list(get_channels())) > 0:
        channels = get_channels()
        for channel in channels:
            button = types.InlineKeyboardButton(f"{channel['full_name']}", callback_data=f'remove_channel_confirm_{channel["chat_id"]}')
            keyboard.add(button)

        # Add a "Back" button
        back_button = types.InlineKeyboardButton("Back 🔙", callback_data='channels_menu')
        keyboard.add(back_button)

        bot.edit_message_text("Select a channel to remove:", call.message.chat.id, call.message.message_id, reply_markup=keyboard)

    else:
        bot.send_message(call.message.chat.id, "There are no Channels.")

    # Remove channel confirm button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_channel_confirm_'))
    def handle_remove_channel_confirm_callback(call):
        remove_channel_confirm_callback(call, bot)