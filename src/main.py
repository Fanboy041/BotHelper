import telebot, logging
import os
import importlib
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

# load the .env file
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
    commands = {}

    # Loop through all the files in the "Commands" folder
    for foldername in os.listdir(commands_dir):
        # Check if the file is a Python script (ends with .py)
        if foldername.endswith('.py') and foldername != '__init__.py':
            # Get the module name without the .py extension
            command_name = os.path.splitext(foldername)[0]

            # Import the module dynamically
            command = importlib.import_module(f'Commands.{command_name}')
            commands[command_name] = command
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

    # New joined chat member handler
    @bot.message_handler(content_types=['new_chat_members'])
    def handle_add_group_chat_id(message):
        if 'addGroupChatId' in features:
            features['addGroupChatId'].add_group_chat_id(message, bot)

    # Left chat member handler
    @bot.message_handler(content_types=['left_chat_member'])
    def handle_add_group_chat_id(message):
        if 'deleteGroupChatId' in features:
            features['deleteGroupChatId'].delete_group_chat_id(message, bot)

    # Start command
    @bot.message_handler(commands=['start'])
    def handle_start_command(message):
        if 'startCommand' in commands:
            commands['startCommand'].send_welcome(message, bot)

    # Settings command
    @bot.message_handler(commands=['settings'])
    def handle_settings_command(message):
        if 'settingsCommand' in commands:
            commands['settingsCommand'].settings_command(message, bot)

    # Handle the urls that sent in groups
    @bot.message_handler(content_types=['text'])
    def handle_antispam_group(message):        
        if 'antispamGroup' in features:
            features['antispamGroup'].antispam_group(message, bot)

    
    bot.infinity_polling()
except KeyboardInterrupt:
    logging.info("Polling manually interrupted.")
