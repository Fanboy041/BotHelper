First of all you need to create a bot on telegram to interact with it when maintaining the code

# Creating Bot On Telegram:
- Open Telegram then go to [Bot Father](https://t.me/BotFather) 

Which is a bot provided by Telegram its-self to create bots on their application which can give you an API Token and you can edit your bot using it, you need the API Token to make a connection between your code and your bot on telegram

When you start the bot you need to send this command: /newbot

![image](https://github.com/Fanboy041/Telegram-Bot-Template/assets/163625032/d52fa285-d8e6-4450-b7c7-b355d980c4b1)


- Now you need to prepare the bot by at first sending to the BotFather the name of your bot:

![image](https://github.com/Fanboy041/Telegram-Bot-Template/assets/163625032/ace1f19e-3605-44ac-97fe-346bfa664a8f)

- Then type your new bot username:

![image](https://github.com/Fanboy041/Telegram-Bot-Template/assets/163625032/709e16e5-3b59-4eac-9259-bc880ea635ca)


- After that it gives you your new API Token to use it in your code, 
in this case it’s : 7173715947:AAHQCwqidZadBtcdRnqheHZ9ktmrL7bZ9kQ

    keep it for the next step

# Cloning Into Workspace Github Repo:
You need to install “git” and latest “Python” version on your workstation if it’s not installed, see:
-	[Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
-	[Installing Python](https://python.org/downloads/)

After “git” being installed, assuming you’re using Windows, create a new folder then hold shift and press right click:

![image](https://github.com/Fanboy041/Telegram-Bot-Template/assets/163625032/897f281c-e049-4a09-b75d-238676c91388)

- Open the PowerShell then type “code .” and hit enter to open the directory in your code editor:

![image](https://github.com/Fanboy041/Telegram-Bot-Template/assets/163625032/de0ed58a-fb15-4bb9-ad6d-3451117ca4de)

- Reach to “Terminal” in your code editor to type the cloning command to clone the repo:

        git clone https://github.com/Fanboy041/Telegram-Bot-Template.git

- You’re gonna find something similar to this:

![image](https://github.com/Fanboy041/Telegram-Bot-Template/assets/163625032/d2fb100e-4d07-4454-8118-ac54314061e8)

# Preparing The Workspace To Start:
- Before you take any action you need to install the requirements by typing in your terminal:

    pip install -r requirements.txt

- after that you need to create a file in the root directory called “.env” to store “MONGO_URI” the database connection uri and your “BOT_TOKEN” the api token for your bot you just created:

```
    MONGO_URI=""
    BOT_TOKEN=""
```

NOTE: Put your mogo uri and bot token inside these double quotations.

- Finally, you are ready to start the bot by running :
python ./src/main.py

# Documentation Part:
For more info on how to contribute with us to code telegram bots with python you should understand all the methods in Telegram API so you need to visit Telegram Bot API and the python library for telegram bots pyTelegramBotAPI and pymongo library documentation for the database coding

See:

For Telegram Bot API:
-	https://core.telegram.org/bots/api


For pyTelegramBotAPI:
-	https://pypi.org/project/pyTelegramBotAPI/


For pymongo:
-	https://pymongo.readthedocs.io/en/stable/

# Explain How The Code Is Being Wrote:
- __requirements.txt__ file is important to install the required libraries which is being used to write the code

- __Commands__ contains any command script, command in telegram bots it's any text message being sent to the bot that starts with __/__ character for example: /start

- __Database__ contains the script that link the code with [MongoDB](https://www.mongodb.com/) Database, it contains alot of methods you better read it before start coding in this repo

- __Features__ contains extra features that we add it to the bot, it's not a message handler or callback query handler

- __Handlers__ contains all callback queries scripts

  NOTE: Callback query is the action that being sent to the bot when pressing an inline button in the bot

- __main.py__ is the main script that the bot interact with, inside this script there is an automatic importing from the Commands, Features and Handlers contents to _main.py_ so you can easily call any function inside those scripts in the _main.py_ script directly, also you should know that any new file you add in the folders up there you need to handle what you wrote in the _main.py_ so the bot can see that new file

```
├── src
│    ├── Commands
│    │    ├── settingsCommand.py
│    │    └── startCommand.py
│    │
│    ├── Database
│    │    └── MongoDB.py
│    │
│    ├── Features
│    │    ├── addGroupChatId.py
│    │    ├── antispamGroup.py
│    │    └── deleteGroupChatId.py
│    │
│    ├── Handlers
│    │    ├── Admins
│    │    │    ├── addAdminCallback.py
│    │    │    ├── adminsMenuCallback.py
│    │    │    ├── removeAdminCallback.py
│    │    │    ├── removeAdminConfirmCallback.py
│    │    │    ├── removeAdminYesCallback.py
│    │    │    └── showAdminsCallback.py
│    │    │
│    │    ├── Antispam
│    │    │    ├── antispamGroupCallback.py
│    │    │    ├── antispamGroupConfirmCallback.py
│    │    │    ├── antispamGroupdisallowedCallback.py
│    │    │    ├── antispamGroupYesCallback.py
│    │    │    └── kickUserFromGroupCallback.py
│    │    │
│    │    ├── Channel
│    │    │    ├── addChannelCallback.py
│    │    │    ├── channelsMenuCallback.py
│    │    │    ├── removeChannelConfirmCallback.py
│    │    │    ├── removeChannelYesCallback.py
│    │    │    └── showChannelsCallback.py
│    │    │
│    │    ├── Groups
│    │    │    ├── addGroupCallback.py
│    │    │    ├── groupsMenuCallback.py
│    │    │    ├── removeGroupCallback.py
│    │    │    ├── removeGroupConfirmCallback.py
│    │    │    └── showGroupsCallback.py
│    │    │
│    │    ├── Settings
│    │    │    └── backToSettingsMenuCallback.py
│    │    │
│    │    └── Users
│    │         ├── removeUserCallback.py
│    │         ├── removeUserConfirmCallback.py
│    │         ├── removeUserYesCallback.py
│    │         ├── showUsersCallback.py
│    │         └── usersMenuCallback.py
│    │
│    └── main.py
│
├── .gitignore
│
├── Readme.md
│
└── requirements.txt

```
