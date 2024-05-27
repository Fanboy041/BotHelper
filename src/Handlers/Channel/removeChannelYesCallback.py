from Database.MongoDB import get_channel, delete_channel
from Handlers.Back.backToSettingsMenuCallback import back_to_settings_menu_callback

def remove_channel_yes_callback(call, bot):
    parts = call.data.split('_')
    channel_id = int(parts[3])

    if get_channel(channel_id):
        bot.leave_chat(channel_id)
        delete_channel(channel_id)

        bot.send_message(call.message.chat.id, f"channel with ID {channel_id} removed successfully.")
    else:
        bot.send_message(call.message.chat.id, f"channel with ID {channel_id} not found.")

    back_to_settings_menu_callback(call, bot)

