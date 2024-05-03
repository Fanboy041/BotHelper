# showChannelCallback.py
from telebot import types
from Database.MongoDB import channel_collection

def show_channel_callback(call, bot):

    channel_list = channel_collection.find_one()
    if channel_list:
        # Add a back button to go back
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_channel_menu')
        keyboard.add(back_button)
        
        # Display the channel username
        bot.edit_message_text(f"Channel username: @{channel_list['username']}", call.message.chat.id, call.message.message_id, reply_markup=keyboard)

    else:
        bot.send_message(call.message.chat.id, "Channel username not set.")