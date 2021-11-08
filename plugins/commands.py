import os
import logging
import random
import asyncio
from Script import script
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import Media, get_file_details
from database.users_chats_db import db
from info import CHANNELS, ADMINS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION, LOG_CHANNEL, PICS
from utils import get_size, is_subscribed, temp

logger = logging.getLogger(__name__)

PHOTO = [
    "https://telegra.ph/file/17b664dd55dcb4dd81185.jpg",
    "https://telegra.ph/file/c6d58e58e003f036470da.jpg",
    "https://telegra.ph/file/c3fad6a10f05ece01b51d.jpg",
    "https://telegra.ph/file/bc74adbb9fa4ad32def73.jpg",
    "https://telegra.ph/file/3a2de7f981f0249309a1b.jpg",
    "https://telegra.ph/file/f5a444586a6f28d154f6c.jpg",
    "https://telegra.ph/file/f6bb83a00b1337b3e0a60.jpg",
    "https://telegra.ph/file/9690286c14706e018139b.jpg",
    "https://telegra.ph/file/6c14e6319d02b6ceb58bc.jpg",
    "https://telegra.ph/file/a8879a233eab699365352.jpg",
    "https://telegra.ph/file/2faea362c1ca8dfbeb145.jpg",
    "https://telegra.ph/file/28a1c0ec15b390489eade.jpg",
    "https://telegra.ph/file/3b43ac420e44701ac18ce.jpg",
    "https://telegra.ph/file/1d5f212f2a62cbbf67f85.jpg",
    "https://telegra.ph/file/fc2a4f43da7289eb64f49.jpg"
]

@Client.on_message(filters.command("start"))
async def start(client, message):
    if message.chat.type in ['group', 'supergroup']:
        buttons = [[
            InlineKeyboardButton('♻️ 𝙶𝚛𝚘𝚞𝚙', url='https://t.me/Movies_Club_2019'),
            InlineKeyboardButton('⭕️ 𝙲𝚑𝚊𝚗𝚗𝚎𝚕', url='https://t.me/mcnewmovies')
            ],[
            InlineKeyboardButton('🕵‍♂️ 𝙰𝚗𝚢 𝙳𝚘𝚞𝚋𝚝𝚜 🕵‍♀️', url='http://t.me/EvaMariaSupport')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(script.START_TXT.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup)
        await asyncio.sleep(2) # 😢 https://github.com/EvamariaTG/EvaMaria/blob/master/plugins/p_ttishow.py#L17 😬 wait a bit, before checking.
        if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, "Unknown"))       
            await db.add_chat(message.chat.id, message.chat.title)
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
        buttons = [[
            InlineKeyboardButton('➕ 𝙰𝚍𝚍 𝙼𝚎 𝚃𝚘 𝚈𝚘𝚞𝚛 𝙶𝚛𝚘𝚞𝚙𝚜 ➕', url='http://t.me/Imdbfilter_bot?startgroup=true')
            ],[
            InlineKeyboardButton('ℹ️ 𝙷𝚎𝚕𝚙', callback_data='help'),
            InlineKeyboardButton('🤴 𝙳𝚎𝚟', url='https://t.me/Sanoob_Achu_18'),
            InlineKeyboardButton('😊 𝙰𝚋𝚘𝚞𝚝', callback_data='about')
            ],[
            InlineKeyboardButton('♻️ 𝙶𝚛𝚘𝚞𝚙', url='https://t.me/Movies_Club_2019'),
            InlineKeyboardButton('⭕️ 𝙲𝚑𝚊𝚗𝚗𝚎𝚕', url='https://t.me/mcnewmovies')
            ],[
            InlineKeyboardButton('🕵‍♂️ 𝙰𝚗𝚢 𝙳𝚘𝚞𝚋𝚝𝚜 🕵‍♀️', url='http://t.me/EvaMariaSupport')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=f"{random.choice(PHOTO)}",
            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html'
        )
        return
    if AUTH_CHANNEL and not await is_subscribed(client, message):
        try:
            invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
        except ChatAdminRequired:
            logger.error("Make sure Bot is admin in Forcesub channel")
            return
        btn = [
            [
                InlineKeyboardButton(
                    "🔰 ᴊᴏɪɴ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ🔰", url=invite_link.invite_link
                )
            ]
        ]

        if message.command[1] != "subscribe":
            btn.append([InlineKeyboardButton("🔄 Re-Try 🔄", callback_data=f"checksub#{message.command[1]}")])
        await client.send_message(
            chat_id=message.from_user.id,
            text="**🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭\n\nനിങ്ങൾക് സിനിമകൾ വേണോ🤧? അതിനായി അദ്യം ഞങ്ങളുടെ മെയിൻ ചാനലിൽ ജോയിൻ ചെയ്യുക... \n[🔰Click Join Channel🔰 And Join Then Click 🔃Re Try🔃] \nJoin ചെയ്ത ശേഷം🔃 TrY Again 🔃 ബട്ടൺ ക്ലിക്ക് ചെയ്താൽ മൂവി കിട്ടുന്നതാണ്..!**",
                    reply_markup=InlineKeyboardMarkup(btn),
            parse_mode="markdown"
            )
        return
    if len(message.command) ==2 and message.command[1] in ["subscribe", "error", "okay", "help"]:
        buttons = [[
            InlineKeyboardButton('➕ 𝙰𝚍𝚍 𝙼𝚎 𝚃𝚘 𝚈𝚘𝚞𝚛 𝙶𝚛𝚘𝚞𝚙𝚜 ➕', url='http://t.me/Imdbfilter_bot?startgroup=true')
            ],[
            InlineKeyboardButton('ℹ️ 𝙷𝚎𝚕𝚙', callback_data='help'),
            InlineKeyboardButton('🤴 𝙳𝚎𝚟', url='https://t.me/Sanoob_Achu_18'),
            InlineKeyboardButton('😊 𝙰𝚋𝚘𝚞𝚝', callback_data='about')
            ],[
            InlineKeyboardButton('♻️ 𝙶𝚛𝚘𝚞𝚙', url='https://t.me/Movies_Club_2019'),
            InlineKeyboardButton('⭕️ 𝙲𝚑𝚊𝚗𝚗𝚎𝚕', url='https://t.me/mcnewmovies')
            ],[
            InlineKeyboardButton('🕵‍♂️ 𝙰𝚗𝚢 𝙳𝚘𝚞𝚋𝚝𝚜 🕵‍♀️', url='http://t.me/EvaMariaSupport')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=f"{random.choice(PHOTO)}",
            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html'
        )
        return
    file_id = message.command[1]
    files_ = await get_file_details(file_id)
    if not files_:
        return await message.reply('No such file exist 😏.')
    files = files_[0]
    title = files.file_name
    size=get_size(files.file_size)
    f_caption=files.caption
    if CUSTOM_FILE_CAPTION:
        try:
            f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
        except Exception as e:
            print(e)
            f_caption=f_caption
    if f_caption is None:
        f_caption = f"{files.file_name}"
    await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption,
        )
                    

@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
           
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('logs') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))

@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Processing...📃", quote=True)
    else:
        await message.reply('🤭 Reply to file 🗂️ with /delete which you want to delete 🚮', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('😏 This is not supported file format')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'mime_type': media.mime_type
    })
    if result.deleted_count:
        await msg.edit('🗂️ File is successfully deleted from database 🚮')
    else:
        await msg.edit('🤧 File not found in database')


@Client.on_message(filters.command('deleteall') & filters.user(ADMINS))
async def delete_all_index(bot, message):
    await message.reply_text(
        '😏 This will delete all indexed files 🗂️.\n🙄 Do you want to continue??',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✅️ YES", callback_data="autofilter_delete"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="🚫 No", callback_data="close_data"
                    )
                ],
            ]
        ),
        quote=True,
    )


@Client.on_callback_query(filters.regex(r'^autofilter_delete'))
async def delete_all_index_confirm(bot, message):
    await Media.collection.drop()
    await message.answer()
    await message.message.edit('✅️Succesfully Deleted All The Indexed Files 🗂️.')

