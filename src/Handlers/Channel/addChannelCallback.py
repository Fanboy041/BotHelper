# addChannelCallback.py
from telebot import types
from Database.MongoDB import save_channel

def add_channel_callback(call, bot):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_channel_menu')
    keyboard.add(back_button)

    bot.edit_message_text("Forward a message from your channel", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')

    # Set the next state to handle the channel username message
    bot.register_next_step_handler(call.message, process_channel_username, bot)
    
def process_channel_username(message, bot):
    try:

        full_name = message.forward_from_chat.title
        username = message.forward_from_chat.username 
        chat_id = message.forward_from_chat.id

        save_channel(full_name, username, chat_id)
        bot.send_message(message.chat.id, f"Channel username set to @{username}")
    except Exception as e:
        # Show error message to the user 
        bot.send_message(message.chat.id, f"Error: {str(e)}")