from telebot import types
from Database.MongoDB import get_channel

def send_channel_callback(call, bot):

    channel_id = int(call.data.split('_')[-1])
    channel = get_channel(channel_id)
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    back_button = types.InlineKeyboardButton("Back 🔙", callback_data=f'view_channel_{channel["chat_id"]}')
    keyboard.add(back_button)

    bot.edit_message_text(chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                          text="Do you want to attach buttons to the message? (yes/no)", reply_markup=keyboard)

    bot.register_next_step_handler(call.message, process_answer, bot, channel_id)

def process_answer(message, bot, channel_id):

    if message.text == 'yes':
        bot.send_message(message.chat.id, "Send the button text and website separated by a dash (-)")
        bot.register_next_step_handler(message, process_buttons, bot, channel_id)
    elif message.text == 'no':
        bot.send_message(message.chat.id, "What do you want to send to this channel?")
        bot.register_next_step_handler(message, process_sent_message2, bot, channel_id)
    else:
        bot.send_message(message.chat.id, "Invalid answer. Please send 'yes' or 'no' next time.")


def process_buttons(message, bot, channel_id):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button_text, website = message.text.split('-')
    button = types.InlineKeyboardButton(button_text, url=website.strip())
    keyboard.add(button)

    bot.send_message(message.chat.id, "What do you want to send to this channel?")

    bot.register_next_step_handler(message, process_sent_message1, bot, channel_id, keyboard)



def process_sent_message1(message, bot, channel_id, keyboard):

    bot.send_message(channel_id, message.text, reply_markup=keyboard)
    

def process_sent_message2(message, bot, channel_id):

    bot.send_message(channel_id, message.text)




