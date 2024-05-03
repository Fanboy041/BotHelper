# removeAdminBackCallback.py
from Handlers.Admins.removeAdminCallback import remove_admin_callback

def remove_admin_back_callback(call, bot):
        # Edit the message to show the "Select an admin ID to remove:" message
        remove_admin_callback(call, bot)