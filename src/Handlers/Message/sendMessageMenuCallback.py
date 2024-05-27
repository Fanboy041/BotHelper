from telebot import types
from .showChannelsCallback import show_channels_callback
from .showGroupsCallback import show_groups_callback

def send_message_menu_callback(call, bot):

    # Initial message with inline keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    show_channels = types.InlineKeyboardButton("Show Channels 📣", callback_data='show_channels')
    show_groups = types.InlineKeyboardButton("Show Groups 👥", callback_data='show_groups')
    back_to_options_menu = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_options_menu')

    keyboard.add(show_channels, show_groups, back_to_options_menu)

    bot.edit_message_text("📊 Sending Messages Control Panel:", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')

    # Remove channel and remove channel back button
    @bot.callback_query_handler(func=lambda call: call.data == 'show_channels')
    def handle_show_channels_callback(call):
        show_channels_callback(call, bot)

    # Remove channel and remove channel back button
    @bot.callback_query_handler(func=lambda call: call.data == 'show_groups')
    def handle_show_groups_callback(call):
        show_groups_callback(call, bot)