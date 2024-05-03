# removeChannelBackCallback.py
from Handlers.Channel.removeChannelCallback import remove_channel_callback

def remove_channel_back_callback(call, bot):
        # Edit the message to show the "Select an admin ID to remove:" message
        remove_channel_callback(call, bot)