from telebot import types

def back_to_options_menu_callback(call, bot):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    antispam_button = types.InlineKeyboardButton("📨 Antispam", callback_data='antispam')
    keyboard.add(antispam_button)

    bot.edit_message_text("📊 Options:", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')
