from telebot import types
from Database.MongoDB import get_channel

def send_channel_callback(call, bot):
    channel_id = int(call.data.split('_')[-1])
    channel = get_channel(channel_id)
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    yes_button = types.InlineKeyboardButton("Yes ✅", callback_data=f'show_channel_yes_{channel["chat_id"]}')
    no_button = types.InlineKeyboardButton("No ❌", callback_data=f'show_channel_no_{channel["chat_id"]}')
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data=f'view_channel_{channel["chat_id"]}')
    keyboard.add(yes_button, no_button, back_button)

    bot.edit_message_text(chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    text="Do you want to attach buttons to the message? (yes/no)", reply_markup=keyboard)
    
    @bot.callback_query_handler(func=lambda call: call.data.startswith('show_channel_'))
    def handle_view_channel_yes_callback(call):
        parts = call.data.split('_')
        if parts[2] == "yes":
            bot.send_message(call.message.chat.id, "Send the button text and website separated by a dash (-)")
            bot.register_next_step_handler(call.message, process_buttons, call, bot, channel_id)
        elif parts[2] == "no":
            bot.send_message(call.message.chat.id, "What do you want to send to this channel?")
            bot.register_next_step_handler(call.message, process_sent_message2, bot, channel_id)

    def process_buttons(message, call, bot, channel_id):
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        if "-" in message.text:
            button_text, website = message.text.split('-')
            if website.strip().lower().startswith('http'):
                button = types.InlineKeyboardButton(button_text, url=website.strip())
                keyboard.add(button)
            
                bot.send_message(message.chat.id, "What do you want to send to this channel?")

                bot.register_next_step_handler(message, process_sent_message1, bot, channel_id, keyboard)
            else:
                bot.send_message(message.chat.id, "Website should be as a Url")
                handle_view_channel_yes_callback(call)
        else: 

            handle_view_channel_yes_callback(call)

def process_sent_message1(message, bot, channel_id, keyboard):
    bot.send_message(channel_id, message.text, reply_markup=keyboard)
    

def process_sent_message2(message, bot, channel_id):

    bot.send_message(channel_id, message.text)




