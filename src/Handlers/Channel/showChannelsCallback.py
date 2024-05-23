# showChannelCallback.py
from telebot import types
from Database.MongoDB import (get_channel, channel_collection)

def show_channels_callback(call, bot):

    channels = channel_collection.find()

    if channels:

     
        # Create an empty InlineKeyboardMarkup object lately i will store every channel on single one

        keyboard = types.InlineKeyboardMarkup(row_width=1)

        # Loop through channels and create buttons for every one 

        for channel in channels:
            button = types.InlineKeyboardButton(f"{channel['full_name']}", callback_data=f'show_channels_callback{channel["chat_id"]}')
            keyboard.add(button)


        # Add a "Back" button which will display after all the channels
        back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_channels_menu')
        keyboard.add(back_button)
        


        
        bot.edit_message_text(
            "Select a channel:", call.message.chat.id, call.message.message_id, reply_markup=keyboard
        )
        
    else:
        bot.send_message(call.message.chat.id, "No channels found.")

