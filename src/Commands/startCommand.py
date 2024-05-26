from Database.MongoDB import (
    owner_collection, user_collection, save_owner, save_user, get_owner, get_admin)

def send_welcome(message, bot):
    if message.chat.type == "private":

        # User's informations
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        if last_name:
            full_name = first_name + " " + last_name
        else:
            full_name = first_name

        username = message.from_user.username
        chat_id = message.chat.id

        # Set owner if it's the first user and there is one owner only
        if owner_collection.count_documents({}) == 0:
            save_owner(full_name, username, chat_id)
            bot.send_message(message.chat.id, f"Welcome <b>{full_name}</b>\nYou are my owner from now on", parse_mode='HTML')

        else:
            # Counting the number of the users
            total_users = user_collection.count_documents({}) + 1

            # Save the user info in the database
            save_user(full_name, username, chat_id, total_users)

            if message.chat.id == get_owner()['chat_id']:
                bot.send_message(message.chat.id, f"Hey owner, <b>{full_name}</b>!\n\nThank you for interacting with me. I'm excited to have you on board. 🌹", parse_mode='HTML')
            elif get_admin(chat_id) != None and message.chat.id == get_admin(chat_id)['chat_id']:
                bot.send_message(message.chat.id, f"Hey admin, <b>{full_name}</b>!\n\nThank you for interacting with me. I'm excited to have you on board. 🌹", parse_mode='HTML')
            else:
                bot.send_message(message.chat.id, f"Welcome, <b>{full_name}</b>!\n\nThank you for interacting with our Telegram bot. We're excited to have you on board. 🌹", parse_mode='HTML')

    else:
        bot_username = bot.get_me().username
        if f"@{bot_username}" in message.text:
            bot.reply_to(message, "Please run the command in private")
