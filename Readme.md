# Explanation for contributers:

- Commands

The Commands folder contains the bot commands which you can add a new command to the bot by adding a new exampleCommand.py to the folder

- Handlers

The Handlers folder contains the call back queries for the bot keyboard buttons call backs which you can add a new exampleCallback.py to the folder

- Database

The Database folder contains the configurations for the MongoDB database but the owner of this repo will change its structure in future so it's not necessary to understand the database script all you need to know is these functions to help you build new commands and callbacks

- get_owner()
to get the owner's object that contains (fullname, username and chat id) of the owner from the database

- get_admin()
to get the admin's object that contains (fullname, username and chat id) of the owner from the database

- get_user()
to get the user's object that contains (fullname, username and chat id) of the owner from the database

- get_channel()
to get the channel's object that contains (fullname, username and chat id) of the owner from the database

- get_group()
to get the group's object that contains (fullname, username and chat id) of the owner from the database

Also these functions to save the data of owner, admin, user, channels and groups to the database:

- save_owner(full_name, username, chat_id)

- save_admin(full_name, username, chat_id)

- save_user(full_name, username, chat_id, total_users)

- save_channel(full_name, username, chat_id)

- save_group(full_name, username, chat_id)

Finally your tasks will be adding new call back queries to the code to finish the main reason of this bot:

1- sending custom messages (with or without inline keyboard) to specific or all channels and groups

2- sending custom messages (with or without inline keyboard) to specific or all users

3- add ban messages with URL's on groups

4- add ban for bad words

Note: sending messages it's a role for owner and admins only

to let you know the structure of the objects this is an example to the owner schema:

```
owner_schema = {
    "full_name": str,
    "username": str,
    "chat_id": int
}
```
