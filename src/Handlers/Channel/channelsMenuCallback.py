from telebot import types
from Handlers.Channel.removeChannelCallback import remove_channel_callback
from Database.MongoDB import get_owner

def channels_menu_callback(call, bot):

    # Initial message with inline keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    add_channel = types.InlineKeyboardButton("Add Channel 🔈", url=f"http://t.me/{bot.get_me().username}?startchannel=botstart")
    remove_channel = types.InlineKeyboardButton("Remove Channel ✖️", callback_data='remove_channel')
    back_to_settings_menu = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_settings_menu')

    if get_owner()['chat_id'] == call.message.chat.id:
        keyboard.add(add_channel, remove_channel, back_to_settings_menu)
    else:
        keyboard.add(add_channel, back_to_settings_menu)

    bot.edit_message_text("📊 Channels Control Panel:", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')

    # Remove channel and remove channel back button
    @bot.callback_query_handler(func=lambda call: call.data == 'remove_channel')
    def handle_remove_channel_callback(call):
        remove_channel_callback(call, bot)