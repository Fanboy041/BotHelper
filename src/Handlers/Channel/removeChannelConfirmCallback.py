from telebot import types
from Database.MongoDB import channel_collection
from Handlers.Channel.removeChannelYesCallback import remove_channel_yes_callback

def remove_channel_confirm_callback(call, bot):
    channel_id = int(call.data.split('remove_channel_confirm_')[1])
    fullname = channel_collection.find_one({'chat_id': channel_id})['full_name']
    username = channel_collection.find_one({'chat_id': channel_id})['username']
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    yes_button = types.InlineKeyboardButton("Yes ✅", callback_data=f'remove_channel_yes_{channel_id}')
    back_button = types.InlineKeyboardButton("Back 🔙", callback_data=f'remove_channel_back_{channel_id}')  # Add a Back button
    keyboard.add(yes_button, back_button)

    bot.edit_message_text(
        f"Are you sure you want to remove this channel:\n\nName: <b>{fullname}</b>\nUsername: @{username}\nUserID: <code>{channel_id}</code>\n\nThis action can't be undone ?",
        call.message.chat.id,
        call.message.message_id, parse_mode='HTML', reply_markup=keyboard)

    # Remove channel yes button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_channel_yes_'))
    def handle_remove_channel_yes_callback(call):
        remove_channel_yes_callback(call,bot)