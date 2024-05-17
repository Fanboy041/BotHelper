# removeGroupYesCallback.py
from Database.MongoDB import get_group, group_collection
from Handlers.Antispam.antispamGroupCallback import antispam_group_callback

def antispam_group_activation_callback(bot, call):
    parts = call.data.split('_')
    # Check if there are enough parts to unpack
    if len(parts) >= 3:
        action, group_id = parts[2], int(parts[3])  # Correct the unpacking

    if action == 'activation':
        # If the callback was yes, antispam the group
        if get_group(group_id)["is_antispam"] == False:
            group_collection.update_one({"chat_id": group_id}, {"$set": {"is_antispam": True}})
            bot.send_message(call.message.chat.id, "Antispam is Activated")
            bot.send_message(call.message.chat.id, "make sure that the Bot is admin on the Group")
            bot.send_message(group_id, "Antispam is Activated")

        else: 
            group_collection.update_one({"chat_id": group_id}, {"$set": {"is_antispam": False}})
            bot.send_message(call.message.chat.id, "Antispam is Deactivated")
            bot.send_message(group_id, "Antispam is Deactivated")
            
        antispam_group_callback(call, bot)

    elif action == 'back':
        antispam_group_callback(call, bot)
        
    else:
        bot.send_message(call.message.chat.id, "Invalid action data.")
