from telebot import types
from Database.MongoDB import get_channel
from Handlers.Settings.backToSettingsMenuCallback import back_to_settings_menu_callback

def send_channel_callback(call, bot):
    channel_id = int(call.data.split('_')[-1])
    channel = get_channel(channel_id)
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    yes_button = types.InlineKeyboardButton("Yes ✅", callback_data=f'send_confirm_yes_{channel["chat_id"]}')
    no_button = types.InlineKeyboardButton("No ❌", callback_data=f'send_confirm_no_{channel["chat_id"]}')
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data=f'view_channel_{channel["chat_id"]}')
    keyboard.add(yes_button, no_button, back_button)

    bot.edit_message_text(chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    text="Do you want to attach buttons to the message? (yes/no)", reply_markup=keyboard)
    
    @bot.callback_query_handler(func=lambda call: call.data.startswith('send_confirm_'))
    def handle_view_channel_yes_callback(call):

        parts = call.data.split('_')
        if parts[2] == "yes":
            back_to_settings_menu_callback(call, bot)
            bot.send_message(call.message.chat.id, "Send the button text and website separated by a dash (-)")
            bot.register_next_step_handler(call.message, process_yes_button, call, bot, channel_id)
        elif parts[2] == "no":
            back_to_settings_menu_callback(call, bot)
            bot.send_message(call.message.chat.id, "What do you want to send to this channel?")
            bot.register_next_step_handler(call.message, process_sent_message2, bot, channel_id)

    def process_yes_button(message, call, bot, channel_id):
        answer_message = message.id - 1
        keyboard1 = types.InlineKeyboardMarkup(row_width=1)
        if "-" in message.text:
            button_text, website = message.text.split('-')
            if website.strip().lower().startswith('http'):
                channel_button = types.InlineKeyboardButton(button_text, url=website.strip())
                keyboard1.add(channel_button)

                bot.delete_message(message.chat.id, answer_message)
                bot.delete_message(message.chat.id, message.id)
                bot.send_message(message.chat.id, "What do you want to send to this channel?")
                bot.register_next_step_handler(message, process_sent_message1, bot, channel_id, keyboard1, channel_button)

            else:
                bot.send_message(message.chat.id, "Website should be as a Url")
                bot.register_next_step_handler(call.message, process_yes_button, call, bot, channel_id)
        else: 

            bot.send_message(call.message.chat.id, "Send the button text and website separated by a dash (-)")
            bot.register_next_step_handler(call.message, process_yes_button, call, bot, channel_id)


def process_sent_message1(message, bot, channel_id, keyboard1, channel_button):
    answer_message = message.id - 1
    bot.delete_message(message.chat.id, answer_message)
    bot.delete_message(message.chat.id, message.id)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    approve_button = types.InlineKeyboardButton("Approve sending?", callback_data=f'approve_sending_{channel_id}')
    keyboard.add(channel_button, approve_button)
    bot.send_message(message.chat.id, message.text, reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data.startswith('approve_sending_'))
    def handle_approve_sending_callback(call):
        parts = call.data.split('_')
        channel_id = parts[2]
        bot.send_message(channel_id, message.text, reply_markup=keyboard1)
        bot.answer_callback_query(call.id, "Message sent successfully.")
        bot.delete_message(call.message.chat.id, call.message.id)
    

def process_sent_message2(message, bot, channel_id):
    answer_message = message.id - 1
    bot.delete_message(message.chat.id, answer_message)
    bot.delete_message(message.chat.id, message.id)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    approve_button = types.InlineKeyboardButton("Approve sending?", callback_data=f'approve_sending2_{channel_id}')
    keyboard.add(approve_button)
    bot.send_message(message.chat.id, message.text, reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data.startswith('approve_sending2_'))
    def handle_approve_sending_callback(call):
        parts = call.data.split('_')
        channel_id = parts[2]
        bot.send_message(channel_id, message.text)
        bot.answer_callback_query(call.id, "Message sent successfully.")
        bot.delete_message(call.message.chat.id, call.message.id)