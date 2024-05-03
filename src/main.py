# main.py
import telebot, logging
import os
import importlib
# from telebot import types, util
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
# from Commands.startCommand import send_welcome
# from Database.MongoDB import (
#     get_owner, get_admin, get_user, get_channel, get_group,
#     save_owner, save_user
# )

load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

try:
    # Logging configuration
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    logging.info("Main script runs successfully, Bot is working")

    # RotatingFileHandler
    max_log_size_mb = 5  # Set your desired maximum log size in megabytes
    file_handler = RotatingFileHandler('./bot.log', maxBytes=max_log_size_mb * 1024 * 1024, backupCount=1)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_handler)

    # Get the directory path of the "Commands" folder
    commands_dir = os.path.join(os.path.dirname(__file__), 'Commands')

    # Create an empty dictionary to store the module objects
    modules = {}

    # Loop through all the files in the "Commands" folder
    for foldername in os.listdir(commands_dir):
        # Check if the file is a Python script (ends with .py)
        if foldername.endswith('.py') and foldername != '__init__.py':
            # Get the module name without the .py extension
            module_name = os.path.splitext(foldername)[0]

            # Import the module dynamically
            module = importlib.import_module(f'Commands.{module_name}')
            modules[module_name] = module
            # Now you can access the functions or classes in the imported module

    # Get the directory path of the "Features" folder
    handlers_dir = os.path.join(os.path.dirname(__file__), 'Handlers')

    # Create an empty dictionary to store the module objects
    handlers = {}

    # Loop through all the files in the "Handlers" folder
    for foldername in os.listdir(handlers_dir):
        if foldername != '__init__.py':
            # Loop through all the folders in the "Handlers" folder
            for filename in os.listdir(os.path.join(os.path.dirname(__file__), f'Handlers\\{foldername}')):
                 # Check if the file is a Python script (ends with .py)
                if filename.endswith('.py'):
                    # Get the module name without the .py extension
                    handler_name = os.path.splitext(filename)[0]

                    # Import the module dynamically
                    handler = importlib.import_module(f'Handlers.{foldername}.{handler_name}')
                    handlers[handler_name] = handler
                # Now you can access the functions or classes in the imported module

    # Get the directory path of the "Features" folder
    features_dir = os.path.join(os.path.dirname(__file__), 'Features')

    # Create an empty dictionary to store the module objects
    features = {}

    # Loop through all the files in the "Features" folder
    for foldername in os.listdir(features_dir):
        # Check if the file is a Python script (ends with .py)
        if foldername.endswith('.py') and foldername != '__init__.py':
            # Get the module name without the .py extension
            feature_name = os.path.splitext(foldername)[0]

            # Import the module dynamically
            feature = importlib.import_module(f'Features.{feature_name}')
            features[feature_name] = feature
            # Now you can access the functions or classes in the imported module

    @bot.message_handler(content_types=['new_chat_members'])
    def handle_add_group_chat_id(message):
        if 'addGroupChatId' in features:
            features['addGroupChatId'].add_group_chat_id(message, bot)

    @bot.message_handler(content_types=['new_chat_members'])
    def handle_delete_join_message(message):
        if 'muteJoinedGroupMembers' in features:
            features['muteJoinedGroupMembers'].delete_join_message(message, bot)

    # Start command
    @bot.message_handler(commands=['start'])
    def handle_start_command(message):
        if 'startCommand' in modules:
            modules['startCommand'].send_welcome(message, bot)

    # Settings command
    @bot.message_handler(commands=['settings'])
    def handle_settings_command(message):
        if 'settingsCommand' in modules:
            modules['settingsCommand'].settings_command(message, bot)

    # Admins button
    @bot.callback_query_handler(func=lambda call: call.data == 'admins_menu')
    def handle_admins_callback(call):
        if 'adminsMenuCallback' in handlers:
            handlers['adminsMenuCallback'].admins_callback(call, bot)

    # Back to settings menu button
    @bot.callback_query_handler(func=lambda call: call.data == 'back_to_settings_menu')
    def handle_back_to_settings_menu_callback(call):
        if 'backToSettingsMenuCallback' in handlers:
            handlers['backToSettingsMenuCallback'].back_to_settings_menu_callback(call, bot)

    # Channels button
    @bot.callback_query_handler(func=lambda call: call.data == 'channels_menu')
    def handle_channel_callback(call):
        if 'channelsMenuCallback' in handlers:
            handlers['channelsMenuCallback'].channels_menu_callback(call, bot)
    
    # Add chnnel button
    @bot.callback_query_handler(func=lambda call: call.data == 'add_channel')
    def handle_add_channel_callback(call):
        if 'addChannelCallback' in handlers:
            handlers['addChannelCallback'].add_channel_callback(call, bot)

    # Show channel button
    @bot.callback_query_handler(func=lambda call: call.data == 'show_channel')
    def handle_show_channel_callback(call):
        if 'showChannelCallback' in handlers:
            handlers['showChannelCallback'].show_channel_callback(call, bot)

    # Back to channel menu button
    @bot.callback_query_handler(func=lambda call: call.data == 'back_to_channels_menu')
    def handle_back_to_channel_menu_callback(call):
        if 'channelsMenuCallback' in handlers:
            handlers['channelsMenuCallback'].channels_menu_callback(call, bot)

    # Remove channel button
    @bot.callback_query_handler(func=lambda call: call.data == 'remove_channel')
    def handle_remove_channel_callback(call):
        if 'removeChannelCallback' in handlers:
            handlers['removeChannelCallback'].remove_channel_callback(call, bot)
    
    # Show admins button
    @bot.callback_query_handler(func=lambda call: call.data == 'show_admins')
    def handle_show_admins_callback(call):
        if 'showAdminsCallback' in handlers:
            handlers['showAdminsCallback'].show_admins_callback(call, bot)
    
    # Add admin button
    @bot.callback_query_handler(func=lambda call: call.data == 'add_admin')
    def handle_add_admin_callback(call):
        if 'addAdminCallback' in handlers:
            handlers['addAdminCallback'].add_admin_callback(call, bot)

    # Back to admin menu button
    @bot.callback_query_handler(func=lambda call: call.data == 'back_to_admins_menu')
    def handle_back_to_admin_menu_callback(call):
        if 'adminsMenuCallback' in handlers:
            handlers['adminsMenuCallback'].admins_callback(call, bot)

    # Remove admin button
    @bot.callback_query_handler(func=lambda call: call.data == 'remove_admin')
    def handle_remove_admin_callback(call):
        if 'removeAdminCallback' in handlers:
            handlers['removeAdminCallback'].remove_admin_callback(call, bot)

    # Remove admin confirm button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_admin_confirm_'))
    def handle_remove_admin_confirm_callback(call):
        if 'removeAdminConfirmCallback' in handlers:
            handlers['removeAdminConfirmCallback'].remove_admin_confirm_callback(call, bot)
    
    # Remove admin back button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_admin_back_'))
    def handle_remove_admin_back_callback(call):
        if 'removeAdminCallback' in handlers:
            handlers['removeAdminCallback'].remove_admin_callback(call, bot)

    # Remove admin yes button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_admin_yes_'))
    def handle_remove_admin_yes_callback(call):
        if 'removeAdminYesCallback' in handlers:
            handlers['removeAdminYesCallback'].remove_admin_yes_callback(call, bot)

    # Remove channel confirm button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_channel_confirm_'))
    def handle_remove_channel_confirm_callback(call):
        if 'removeChannelConfirmCallback' in handlers:
            handlers['removeChannelConfirmCallback'].remove_channel_confirm_callback(call, bot)

    # Remove channel yes button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_channel_yes_'))
    def handle_remove_channel_yes_callback(call):
        if 'removeChannelYesCallback' in handlers:
            handlers['removeChannelYesCallback'].remove_channel_yes_callback(call,bot)

    # Remove channel back button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_channel_back_'))
    def handle_remove_channel_back_callback(call):
        if 'removeChannelCallback' in handlers:
            handlers['removeChannelCallback'].remove_channel_callback(call, bot)

    # Groups button
    @bot.callback_query_handler(func=lambda call: call.data == 'groups_menu')
    def handle_group_callback(call):
        if 'groupsMenuCallback' in handlers:
            handlers['groupsMenuCallback'].groups_menu_callback(call, bot)

    # Show groups button
    @bot.callback_query_handler(func=lambda call: call.data == 'show_groups')
    def handle_show_groups_callback(call):
        if 'showGroupsCallback' in handlers:
            handlers['showGroupsCallback'].show_groups_callback(call, bot)

    # Add group button
    @bot.callback_query_handler(func=lambda call: call.data == 'add_group')
    def handle_add_group_callback(call):
        if 'addGroupCallback' in handlers:
            handlers['addGroupCallback'].add_group_callback(call, bot)

    # Back to group menu button
    @bot.callback_query_handler(func=lambda call: call.data == 'back_to_group_menu')
    def handle_back_to_group_menu_callback(call):
        if 'groupsMenuCallback' in handlers:
            handlers['groupsMenuCallback'].groups_menu_callback(call, bot)

    # Show users button
    @bot.callback_query_handler(func=lambda call: call.data == 'show_users')
    def handle_show_users_callback(call):
        if 'showUsersCallback' in handlers:
            handlers['showUsersCallback'].show_users_callback(call, bot)

    # User menu button
    @bot.callback_query_handler(func=lambda call: call.data == 'users_menu')
    def handle_user_menu_callback(call):
        if 'usersMenuCallback' in handlers:
            handlers['usersMenuCallback'].users_menu_callback(call, bot)

    # Back to user menu button
    @bot.callback_query_handler(func=lambda call: call.data == 'back_to_users_menu')
    def handle_user_menu_callback(call):
        if 'usersMenuCallback' in handlers:
            handlers['usersMenuCallback'].users_menu_callback(call, bot)

    # Remove user button
    @bot.callback_query_handler(func=lambda call: call.data == 'remove_user')
    def handle_remove_user_callback(call):
        if 'removeUserCallback' in handlers:
            handlers['removeUserCallback'].remove_user_callback(call, bot)

    # Remove admin confirm button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_user_confirm_'))
    def handle_remove_user_confirm_callback(call):
        if 'removeUserConfirmCallback' in handlers:
            handlers['removeUserConfirmCallback'].remove_user_confirm_callback(call, bot)

    # Remove admin yes button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_user_yes_'))
    def handle_remove_user_yes_callback(call):
        if 'removeUserYesCallback' in handlers:
            handlers['removeUserYesCallback'].remove_user_yes_callback(call, bot)

    # Remove user back button
    @bot.callback_query_handler(func=lambda call: call.data.startswith('remove_user_back_'))
    def handle_remove_user_callback(call):
        if 'removeUserCallback' in handlers:
            handlers['removeUserCallback'].remove_user_callback(call, bot)

    # @bot.message_handler(content_types=['text'])

    bot.infinity_polling()
except KeyboardInterrupt:
    logging.info("Polling manually interrupted.")
