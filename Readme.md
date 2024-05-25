# BotHelper

## Table of Contents

1. [Introduction](#introduction)
2. [Creating a Bot on Telegram](#creating-a-bot-on-telegram)
3. [Cloning the Repository](#cloning-the-repository)
4. [Setting Up the Workspace](#setting-up-the-workspace)
5. [Running the Bot](#running-the-bot)
6. [Project Structure](#project-structure)
7. [Documentation](#documentation)

## Introduction

This project provides a template for creating a Telegram bot using Python. Before getting started, ensure you have installed Git and the latest version of Python.

## Creating a Bot on Telegram

1. Open Telegram and go to [BotFather](https://t.me/BotFather).
2. Start the BotFather bot and send the command: `/newbot`.
3. Follow the instructions to name your bot and set a username.
4. BotFather will provide you with an API token. Keep this token for the next steps.

## Cloning the Repository

1. Install Git from [Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
2. Install Python from [Installing Python](https://python.org/downloads/).
3. Create a new folder on your system.
4. Open PowerShell in the new folder (Shift + Right-click > Open PowerShell window here).
5. Open the folder in your code editor:
    ```
    code .
    ```
6. In the terminal, clone the repository:
    ```
    git clone https://github.com/Fanboy041/BotHelper.git
    ```

## Setting Up the Workspace

1. Install the required libraries by running:
    ```
    pip install -r requirements.txt
    ```
2. Create a `.env` file in the root directory with the following content:
    ```
    MONGO_URI=""
    BOT_TOKEN=""
    ```
    Replace the placeholders with your MongoDB URI and the bot API token from BotFather.

## Running the Bot

To start the bot, run:
```
python ./src/main.py
```
If you're using Termux, you need to add the following to the main script:
```
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
```

## Project Structure

- **requirements.txt**: Lists the required libraries.
- **src**:
  - **Commands**: Scripts for bot commands (e.g., `/start`).
  - **Database**: Scripts for database interactions with MongoDB.
  - **Features**: Additional features for the bot.
  - **Handlers**: Scripts for handling callback queries (actions triggered by inline buttons).
  - **main.py**: The main script that integrates all components.

### Directory Layout

```
├── src
│    ├── Commands
│    │    ├── settingsCommand.py
│    │    └── startCommand.py
│    ├── Database
│    │    └── MongoDB.py
│    ├── Features
│    │    ├── addGroupChatId.py
│    │    ├── antispamGroup.py
│    │    └── deleteGroupChatId.py
│    ├── Handlers
│    │    ├── Admins
│    │    │    ├── addAdminCallback.py
│    │    │    ├── adminsMenuCallback.py
│    │    │    ├── removeAdminCallback.py
│    │    │    ├── removeAdminConfirmCallback.py
│    │    │    ├── removeAdminYesCallback.py
│    │    │    └── showAdminsCallback.py
│    │    ├── Antispam
│    │    │    ├── antispamGroupActicationCallback.py
│    │    │    ├── antispamGroupCallback.py
│    │    │    ├── antispamGroupConfirmCallback.py
│    │    │    ├── antispamGroupDecisionCallback.py
│    │    │    ├── banUserFromGroupCallback.py
│    │    │    └── kickUserFromGroupCallback.py
│    │    ├── Channel
│    │    │    ├── addChannelCallback.py
│    │    │    ├── channelsMenuCallback.py
│    │    │    ├── removeChannelCallback.py
│    │    │    ├── removeChannelConfirmCallback.py
│    │    │    ├── removeChannelYesCallback.py
│    │    │    └── showChannelsCallback.py
│    │    ├── Groups
│    │    │    ├── groupsMenuCallback.py
│    │    │    ├── removeGroupCallback.py
│    │    │    ├── removeGroupConfirmCallback.py
│    │    │    ├── removeGroupYesCallback.py
│    │    │    └── showGroupsCallback.py
│    │    ├── Settings
│    │    │    └── backToSettingsMenuCallback.py
│    │    └── Users
│    │         ├── removeUserCallback.py
│    │         ├── removeUserConfirmCallback.py
│    │         ├── removeUserYesCallback.py
│    │         ├── showUsersCallback.py
│    │         └── antispamGroupDecisionCallback.py
│    └── main.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Documentation

For more information on contributing to this project and understanding the methods used, refer to the following resources:

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)
- [PyMongo](https://pymongo.readthedocs.io/en/stable/)
