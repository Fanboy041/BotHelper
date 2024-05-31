from telebot import types
from Database.MongoDB import get_channels
from Handlers.Back.backToOptionsMenuCallback import back_to_options_menu_callback

def send_channel_callback(call, bot):
    if call.data.split('_')[-1] != "All Channels":
        channel_id = int(call.data.split('_')[-1])
    else:
        channel_id = "All Channels"
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    yes_button = types.InlineKeyboardButton("Yes ✅", callback_data=f'send_confirm_yes_{channel_id}')
    no_button = types.InlineKeyboardButton("No ❌", callback_data=f'send_confirm_no_{channel_id}')
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='show_channels')
    keyboard.add(yes_button, no_button, back_button)

    bot.edit_message_text(chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    text="Do you want to attach buttons to the message? (yes/no)", reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data.startswith('send_confirm_'))
    def handle_view_channel_yes_callback(call):
        bot.delete_message(call.message.chat.id, call.message.id)
        parts = call.data.split('_')[2]
        channel_id = call.data.split('_')[3]
        if parts == "yes":
            bot.send_message(call.message.chat.id, "Send the button text and website separated by a dash (-)")
            bot.register_next_step_handler(call.message, process_yes_button, call, bot, channel_id)
        elif parts == "no":
            bot.send_message(call.message.chat.id, "What title would you like to use for your message?")
            bot.register_next_step_handler(call.message, process_sent_message, bot, channel_id, None, None, False)

    def process_yes_button(message, call, bot, channel_id):
        answer_message = message.id - 1
        keyboard1 = types.InlineKeyboardMarkup(row_width=1)
        if "-" in message.text:
            messageText = message.text.split('-')
            button_text = messageText[0]
            websiteCount = len(messageText)
            website = messageText[1]
            for i in range(2, websiteCount):
                website = website + '-' + messageText[i]
            if website.strip().lower().startswith('http'):
                channel_button = types.InlineKeyboardButton(button_text, url=website.strip())
                keyboard1.add(channel_button)

                bot.send_message(message.chat.id, "What title would you like to use for your message?")
                bot.register_next_step_handler(message, process_sent_message, bot, channel_id, keyboard1, channel_button, True)

            else:
                bot.delete_message(message.chat.id, answer_message)
                bot.delete_message(message.chat.id, message.id)
                bot.send_message(message.chat.id, "Send the button text and website separated by a dash (-), <b>Website should be as a Url</b>", parse_mode='HTML')
                bot.register_next_step_handler(call.message, process_yes_button, call, bot, channel_id)
        else:
            bot.delete_message(message.chat.id, answer_message)
            bot.delete_message(message.chat.id, message.id)
            bot.send_message(call.message.chat.id, "Send the button text and website separated by a dash (-)")
            bot.register_next_step_handler(call.message, process_yes_button, call, bot, channel_id)

def process_sent_message(message, bot, channel_id, keyboard1, channel_button, withButton):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    approve_button = types.InlineKeyboardButton("Approve sending?", callback_data=f'approve_sending_{channel_id}')
    if withButton == True:
        edit_button = types.InlineKeyboardButton("Edit sending?", callback_data=f'send_confirm_yes_{channel_id}')
    else:
        edit_button = types.InlineKeyboardButton("Edit sending?", callback_data=f'send_confirm_no_{channel_id}')
    back_button = types.InlineKeyboardButton("Back", callback_data='show_channels')
    if channel_button is not None:
        keyboard.add(channel_button, approve_button)
    else:
        keyboard.add(approve_button)
    keyboard.add(edit_button, back_button)
    bot.send_message(message.chat.id, message.text, reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data.startswith('approve_sending_'))
    def handle_approve_sending_callback(call):
        parts = call.data.split('_')
        channel_id = parts[2]
        if channel_id == "All Channels":
            channels_id = get_channels()
            for channel_id in channels_id:
                if keyboard1 is not None:
                    bot.send_message(channel_id["chat_id"], call.message.text, reply_markup=keyboard1)
                else:
                    bot.send_message(channel_id["chat_id"], call.message.text)
        else:
            if keyboard1 is not None:
                bot.send_message(channel_id, call.message.text, reply_markup=keyboard1)
            else:
                bot.send_message(channel_id, call.message.text)
        bot.answer_callback_query(call.id, "Message sent successfully.")
        back_to_options_menu_callback(call, bot)