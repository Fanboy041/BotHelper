from telebot import types

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
    keyboard.add(add_group, remove_group, show_group, back_to_settings_menu)

    bot.edit_message_text("📊 Groups Control Panel:", call.message.chat.id, call.message.message_id, reply_markup=keyboard, parse_mode='Markdown')
