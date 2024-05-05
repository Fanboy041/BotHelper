from telebot import types

def antispam_callback(call, bot):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    url_button = types.InlineKeyboardButton("URLs", callback_data='urls')
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_settings_menu')
    keyboard.add(url_button, back_button)

    bot.edit_message_text("📊 Antispam Settings Menu:",
    call.message.chat.id,
    call.message.message_id,
    reply_markup=keyboard, parse_mode='Markdown')