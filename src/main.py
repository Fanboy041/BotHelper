# main.py
import telebot, logging
import os
import importlib
from telebot import types, util
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
# from Commands.startCommand import send_welcome
from Database.MongoDB import (
    get_owner, get_admin, get_user, get_channel, get_group,
    save_owner, save_user
)

load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

try:
    logging.info("Main script runs successfully, Bot is working")

    # Logging configuration
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # RotatingFileHandler
    max_log_size_mb = 5  # Set your desired maximum log size in megabytes
    file_handler = RotatingFileHandler('../logs/bot.log', maxBytes=max_log_size_mb * 1024 * 1024, backupCount=1)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_handler)

    # Get the directory path of the "Commands" folder
    commands_dir = os.path.join(os.path.dirname(__file__), 'Commands')

    # Create an empty dictionary to store the module objects
    modules = {}

    # Loop through all the files in the "Commands" folder
    for filename in os.listdir(commands_dir):
        # Check if the file is a Python script (ends with .py)
        if filename.endswith('.py') and filename != '__init__.py':
            # Get the module name without the .py extension
            module_name = os.path.splitext(filename)[0]

            # Import the module dynamically
            module = importlib.import_module(f'Commands.{module_name}')
            modules[module_name] = module
            # Now you can access the functions or classes in the imported module

    # Logging commands
    # print(modules)

    # Get the directory path of the "Commands" folder
    handlers_dir = os.path.join(os.path.dirname(__file__), 'Handlers')

    # Create an empty dictionary to store the module objects
    handlers = {}

    # Loop through all the files in the "Commands" folder
    for filename in os.listdir(handlers_dir):
        # Check if the file is a Python script (ends with .py)
        if filename.endswith('.py') and filename != '__init__.py':
            # Get the module name without the .py extension
            handler_name = os.path.splitext(filename)[0]

            # Import the module dynamically
            handler = importlib.import_module(f'Handlers.{handler_name}')
            handlers[handler_name] = handler
            # Now you can access the functions or classes in the imported module

    # Logging callbacks
    # print(handlers)


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
    @bot.callback_query_handler(func=lambda call: call.data == 'admins')
    def handle_admins_callback(call):
        if 'adminsCallback' in handlers:
            handlers['adminsCallback'].admins_callback(call, bot)

    # Back to settings menu button
    @bot.callback_query_handler(func=lambda call: call.data == 'back_to_settings_menu')
    def handle_back_to_settings_menu_callback(call):
        if 'backToSettingsMenuCallback' in handlers:
            handlers['backToSettingsMenuCallback'].back_to_settings_menu_callback(call, bot)

    # Channel button
    @bot.callback_query_handler(func=lambda call: call.data == 'channel')
    def handle_channel_callback(call):
        if 'channelCallback' in handlers:
            handlers['channelCallback'].channel_callback(call, bot)
    
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
    @bot.callback_query_handler(func=lambda call: call.data == 'back_to_channel_menu')
    def handle_back_to_channel_menu_callback(call):
        if 'backToChannelMenuCallback' in handlers:
            handlers['backToChannelMenuCallback'].back_to_channel_menu_callback(call, bot)

    # Remove channel button
    @bot.callback_query_handler(func=lambda call: call.data == 'remove_channel')
    def handle_remove_channel_callback(call):
        if 'removeChannelCallback' in handlers:
            handlers['removeChannelCallback'].remove_channel_callback(call, bot)
            

    bot.infinity_polling()
except KeyboardInterrupt:
    logging.info("Polling manually interrupted.")
