from telebot import types

def options_command(message, bot):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    antispam_button = types.InlineKeyboardButton("📨 Antispam", callback_data='antispam')
    keyboard.add(antispam_button)

    bot.send_message(message.chat.id, "📊 Options:", reply_markup=keyboard)