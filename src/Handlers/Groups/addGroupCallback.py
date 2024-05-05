# addgroupCallback.py
from telebot import types

def add_group_callback(call, bot):
    # Add a "Back" button
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_groups_menu')
    keyboard.add(back_button)

    bot.edit_message_text("Go to Group and Add the Bot manually", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')

    bot.register_next_step_handler(call.message, bot)