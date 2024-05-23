from Database.MongoDB import channel_collection
from Handlers.Settings.backToSettingsMenuCallback import back_to_settings_menu_callback

def remove_channel_yes_callback(call, bot):
    parts = call.data.split('_')
    channel_id = int(parts[3])

    if channel_collection.find_one({'chat_id': channel_id}):
        channel_collection.delete_one({'chat_id': channel_id})

        bot.send_message(call.message.chat.id, f"channel with ID {channel_id} removed successfully.")
    else:
        bot.send_message(call.message.chat.id, f"channel with ID {channel_id} not found.")

    back_to_settings_menu_callback(call, bot)

