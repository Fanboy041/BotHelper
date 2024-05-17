import telebot, logging
import os
from telebot import types, util
from pymongo.mongo_client import MongoClient
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

# MongoDB database connection uri
uri = os.getenv("MONGO_URI")

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a new client and connect to the server
client = MongoClient(uri)

# Create "Permissions" database
db = client.permissions # Permissions is the name of the database

# Create "CGManaging" database
db2 = client.managing


""" # Create the collections
db.create_collection("owner_collection")
db.create_collection("admin_collection")
db.create_collection("user_collection")
db2.create_collection("channel_collection")
db2.create_collection("group_collection") """

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    logging.info("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Create a schema for owner that contains a full name and username and chat id of the owner
owner_schema = {
    "full_name": str,
    "username": str,
    "chat_id": int
}
# Create a schema for admins that contains a full name and username and chat id of the admin
admin_schema = {
    "full_name": str,
    "username": str,
    "chat_id": int
}
# Create a schema for users that contains a full name and username and chat id of the user
user_schema = {
    "full_name": str,
    "username": str,
    "chat_id": int,
    "total": int
}
# Create a schema for channels that contains a full name and username and chat id of the channel
channel_schema = {
    "full_name": str,
    "username": str,
    "chat_id": int
}
# Create a schema for groups that contains a full name and username and chat id of the group
group_schema = {
    "full_name": str,
    "username": str,
    "chat_id": int,
    "is_antispam": bool,
}

# Define the collections for owner, admins, users, channels, and groups
owner_collection = client.permissions.owner_collection

admin_collection = client.permissions.admin_collection

user_collection = client.permissions.user_collection

channel_collection = client.managing.channel_collection

group_collection = client.managing.group_collection

# Create a function to get the owner information from the database
def get_owner():
    return owner_collection.find_one()

# Create a function to get the admin information from the database
def get_admin(chat_id):
    return admin_collection.find_one({"chat_id": chat_id})

# Create a function to get the user information from the database
def get_user(chat_id):
    return user_collection.find_one({"chat_id": chat_id})

# Create a function to get all admins information from the database
def get_admins():
    return admin_collection.find()

# Create a function to get all users information from the database
def get_users():
    return user_collection.find()

# Create a function to get the channel information from the database
def get_channel():
    return channel_collection.find_one()

# Create a function to get the group information from the database
def get_group(chat_id):
    return group_collection.find_one({"chat_id": chat_id})

def get_groups():
    return group_collection.find()

def delete_group(chat_id):
    return group_collection.delete_one({'chat_id': chat_id})

def delete_user(chat_id):
    return user_collection.delete_one({'chat_id': chat_id})

# Create a function to save the owner information to the database
def save_owner(full_name, username, chat_id):
    owner_info = {
        "full_name": full_name,
        "username": username,
        "chat_id": chat_id
    }
    owner_existed = owner_collection.find_one({"chat_id": chat_id}) is not None
    
    if owner_existed:
        owner_collection.update_one({"chat_id": chat_id}, {"$set": owner_info})
        
    else:
        owner_collection.insert_one(owner_info)

# Create a function to save the admin information to the database
def save_admin(full_name, username, chat_id):
    admin_info = {
        "full_name": full_name,
        "username": username,
        "chat_id": chat_id
    }
    admin_existed = get_admin(chat_id) is not None
    chat_id_owner = get_owner()['chat_id']

    user = get_user(chat_id)
    if chat_id == user['chat_id']:
        delete_user(chat_id)
        if admin_existed:
            # admin_collection.update_one({"chat_id": chat_id}, {"$set": admin_info})
            admin_collection.update_one({"chat_id": chat_id}, {"$set": {"full_name": full_name, "username": username}})
            bot.send_message(chat_id_owner, f"Admin {full_name} (@{username}) updated successfully.")
            bot.send_message(chat_id, f"Admin {full_name} (@{username}) updated successfully.")
        
        else:
            admin_collection.insert_one(admin_info)
            bot.send_message(chat_id_owner, f"Admin {full_name} (@{username}) added successfully.")
            bot.send_message(chat_id, f"Admin {full_name} (@{username}) added successfully.")

# Create a function to save the user information to the database
def save_user(full_name, username, chat_id, total_users):
    user_info = {
        "full_name": full_name,
        "username": username,
        "chat_id": chat_id,
        "total_users": total_users
    }
    user_existed = user_collection.find_one({"chat_id": chat_id}) is not None
    
    if user_existed:
        user_collection.update_one({"chat_id": chat_id}, {"$set": {"full_name": full_name, "username": username}})
        
    else:
        if (owner_collection.find_one({"chat_id": chat_id}) is None) and (get_admin(chat_id) is None):
            user_collection.insert_one(user_info)
            # Send message to owner when a new member joined

            user = get_user(chat_id)
            
            # Get chat ID from owner document
            chat_id = owner_collection.find_one()['chat_id']
            if chat_id != user['chat_id']:
                bot.send_message(chat_id, f"🔥 New member:\n\n👤 <b>{full_name}</b>\n\nTotal users: {total_users}", parse_mode='HTML' )
        

# Create a function to save the channel information to the database
def save_channel(full_name, username, chat_id):
    channel_info = {
        "full_name": full_name,
        "username": username,
        "chat_id": chat_id
    }
    channel_existed = channel_collection.find_one({"chat_id": chat_id}) is not None
    
    if channel_existed:
        channel_collection.update_one({"chat_id": chat_id}, {"$set": channel_info})
        
    else:
        channel_collection.insert_one(channel_info)

# Create a function to save the group information to the database
def save_group(full_name, username, chat_id):
    group_info = {
        "full_name": full_name,
        "username": username,
        "chat_id": chat_id,
        "is_antispam": False
    }
    group_existed = group_collection.find_one({"chat_id": chat_id}) is not None
    
    if group_existed:
        group_collection.update_one({"chat_id": chat_id}, {"$set": group_info})
        
    else:
        group_collection.insert_one(group_info)
    
