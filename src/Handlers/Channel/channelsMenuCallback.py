from telebot import types
from Handlers.Channel.addChannelCallback import add_channel_callback
from Handlers.Channel.removeChannelCallback import remove_channel_callback
from Handlers.Channel.showChannelsCallback import show_channels_callback
from Handlers.Settings.backToSettingsMenuCallback import back_to_settings_menu_callback
from Database.MongoDB import get_owner

def channels_menu_callback(call, bot):

    # Initial message with inline keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    add_cahnnel = types.InlineKeyboardButton("Add Channel 🔈", callback_data='add_channel')
    remove_channel = types.InlineKeyboardButton("Remove Channel ✖️", callback_data='remove_channel')
    show_channel = types.InlineKeyboardButton("Show Channels 📝", callback_data='show_channels')
    back_to_settings_menu = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_settings_menu')

    if get_owner()['chat_id'] == call.message.from_user.id:
        keyboard.add(add_cahnnel, remove_channel, show_channel, back_to_settings_menu)
    else:
        keyboard.add(show_channel, back_to_settings_menu)

    bot.edit_message_text("📊 Channels Control Panel:", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')

    # Add chnnel button
    @bot.callback_query_handler(func=lambda call: call.data == 'add_channel')
    def handle_add_channel_callback(call):
        add_channel_callback(call, bot)

    # Show channels button
    @bot.callback_query_handler(func=lambda call: call.data == 'show_channels')
    def handle_show_channel_callback(call):
        show_channels_callback(call, bot)

    # Remove channel and remove channel back button
    @bot.callback_query_handler(func=lambda call: call.data == 'remove_channel')
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_channel_back_'))
    def handle_remove_channel_callback(call):
        remove_channel_callback(call, bot)

    # Back to settings menu button
    @bot.callback_query_handler(func=lambda call: call.data == 'back_to_settings_menu')
    def handle_back_to_settings_menu_callback(call):
        back_to_settings_menu_callback(call, bot)