from telebot import types
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
