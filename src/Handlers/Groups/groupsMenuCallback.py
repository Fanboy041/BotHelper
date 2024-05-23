from telebot import types
from Handlers.Groups.showGroupsCallback import show_groups_callback
from Handlers.Groups.removeGroupCallback import remove_group_callback
from Handlers.Settings.backToSettingsMenuCallback import back_to_settings_menu_callback
from Database.MongoDB import get_owner

def groups_menu_callback(call, bot):

    # Initial message with inline keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    # Put the rights
    right = types.ChatAdministratorRights(
        is_anonymous = False, 
        can_manage_chat = True, 
        can_delete_messages = True, 
        can_manage_video_chats = True, 
        can_restrict_members = True, 
        can_promote_members = True, 
        can_change_info = True, 
        can_invite_users = True, 
        can_post_messages = True, 
        can_edit_messages = True, 
        can_pin_messages = True, 
        can_manage_topics = True, 
        can_post_stories = True, 
        can_edit_stories = True, 
        can_delete_stories = True)
    
    bot.set_my_default_administrator_rights(right, for_channels = False)
    add_group = types.InlineKeyboardButton("Add group 🔈", url=f"http://t.me/{bot.get_me().username}?startgroup=botstart")
    remove_group = types.InlineKeyboardButton("Remove group ✖️", callback_data='remove_group')
    show_group = types.InlineKeyboardButton("Show groups 📝", callback_data='show_groups')
    back_to_settings_menu = types.InlineKeyboardButton("Back 🔙", callback_data='back_to_settings_menu')

    if get_owner()['chat_id'] == call.message.chat.id:
        keyboard.add(add_group, remove_group, show_group, back_to_settings_menu)
    else:
        keyboard.add(add_group, show_group, back_to_settings_menu)
    

    bot.edit_message_text("📊 Groups Control Panel:", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')

    # Show groups button
    @bot.callback_query_handler(func=lambda call: call.data == 'show_groups')
    def handle_show_groups_callback(call):
        show_groups_callback(call, bot)

    # Remove group and remove group back button
    @bot.callback_query_handler(func=lambda call: call.data == 'remove_group')
    def handle_remove_group_callback(call):
        remove_group_callback(call, bot)
