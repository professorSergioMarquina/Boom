class script(object):
    START_TXT = """𝙃𝙖𝙞 {},
𝙄 𝘼𝙢 𝘼 𝙋𝙧𝙚 𝙁𝙪𝙣𝙘𝙩𝙞𝙤𝙣𝙚𝙙 𝙍𝙤𝙗𝙤𝙩 𝙉𝙖𝙢𝙚𝙙,\n <a href='https://t.me/Imdbfilter_bot'>`×[¤ ​️🇮🇳𝘾𝙞𝙣𝙙𝙚𝙧𝙚𝙡𝙡𝙖 𝙏𝙜🇮🇳¤]×´</a>,\n✴️ 𝙅𝙪𝙨𝙩 𝘼𝙙𝙙 𝙈𝙚 𝙏𝙤 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥\n✴️ 𝙈𝙖𝙠𝙚 𝙈𝙚 𝘼𝙨 𝘼𝙙𝙢𝙞𝙣\n✴️ 𝙄 𝙒𝙄𝙇𝙇 𝙋𝙧𝙤𝙫𝙞𝙙𝙚 𝙈𝙊𝙑𝙄𝙀𝙎 𝙏𝙝𝙚𝙧𝙚\n✴️𝙏𝙝𝙚𝙣 𝙎𝙚𝙚 𝙈𝙮 𝙋𝙤𝙬𝙚𝙧𝙨 𝙊𝙣 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥✨️
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
©️MᴀɪɴᴛᴀɪɴᴇD Bʏ: <a href="https://t.me/PowerOfTG">𝙋𝙊𝙒𝙀𝙍 𝙊𝙁 𝙏𝙂 [𝙊𝙁𝙁𝙇𝙄𝙉𝙀]🇮🇳</a>"""
    HELP_TXT = """𝙃𝙚𝙮 {}
𝙃𝙚𝙧𝙚 𝙄𝙨 𝙏𝙝𝙚 𝙃𝙚𝙡𝙥 𝙁𝙤𝙧 𝙈𝙮 𝘾𝙤𝙢𝙢𝙖𝙣𝙙."""
    ABOUT_TXT = """
 𝙄 𝘼𝙢 𝙅𝙪𝙨𝙩 𝘼 𝘼𝙪𝙩𝙤 𝙁𝙞𝙡𝙩𝙚𝙧 𝘽𝙤𝙩 🚶‍♂️⚠️

➪ 𝙈𝙮 𝙉𝙖𝙢𝙚 : <a href="https://t.me/Imdbfilter_bot">`×[¤ ​️🇮🇳𝘾𝙞𝙣𝙙𝙚𝙧𝙚𝙡𝙡𝙖 𝙏𝙜🇮🇳¤]×´</a>
➪ 𝘾𝙧𝙚𝙖𝙩𝙤𝙧 : <a href="https://t.me/PowerOfTG">𝙋𝙊𝙒𝙀𝙍 𝙊𝙁 𝙏𝙂 [𝙊𝙁𝙁𝙇𝙄𝙉𝙀]🇮🇳</a>
➪ 𝘾𝙧𝙚𝙙𝙞𝙩𝙨 : <a href="https://t.me/PowerOfTG">𝙀𝙫𝙚𝙧𝙮𝙤𝙣𝙚 𝙞𝙣 𝙩𝙝𝙞𝙨 𝙟𝙤𝙪𝙧𝙣𝙚𝙮</a>
➪ 𝙇𝙞𝙗𝙧𝙖𝙧𝙮 : <a href="https://docs.pyrogram.org/">𝙋𝙮𝙧𝙤𝙜𝙧𝙖𝙢</a>📜
➪ 𝙇𝙖𝙣𝙜𝙪𝙖𝙜𝙚 : <a href="https://docs.pyrogram.org/">𝙋𝙮𝙩𝙝𝙤𝙣 3</a>
➪ 𝘿𝙖𝙩𝙖𝙗𝙖𝙨𝙚 : <a href="https://www.mongodb.com/">𝙈𝙤𝙣𝙜𝙤 𝘿𝘽</a>
➪ 𝘽𝙤𝙩 𝙎𝙚𝙧𝙫𝙚𝙧 : <a href="https://dashboard.heroku.com/apps">𝙃𝙚𝙧𝙤𝙠𝙪</a>
➪ 𝙎𝙤𝙪𝙧𝙘𝙚 𝘾𝙤𝙙𝙚 : <a href="https://github.com/EvamariaTG/EvaMaria">👉 𝘾𝙡𝙞𝙘𝙠 𝙃𝙚𝙧𝙚</a>
➪ 𝘽𝙪𝙞𝙡𝙙 𝙎𝙩𝙖𝙩𝙪𝙨 : <a href="https://t.me/Imdbautofilter_bot">𝙫1.0.1 [ 𝘽𝙀𝙏𝘼 ]</a>

"""
    SOURCE_TXT = """<b>NOTE:</b>
-<a href="https://t.me/Imdbfilter_bot">`×[¤ ​️🇮🇳𝘾𝙞𝙣𝙙𝙚𝙧𝙚𝙡𝙡𝙖 𝙏𝙜🇮🇳¤]×´</a> 𝙄𝙨 𝘼 𝙊𝙥𝙚𝙣 𝙎𝙤𝙪𝙧𝙘𝙚 𝙋𝙧𝙤𝙟𝙚𝙘𝙩💞
-<a href="https://github.com/EvamariaTG/EvaMaria">💞𝙎𝙤𝙪𝙧𝙘𝙚 𝘾𝙤𝙙𝙚💞</a> 𝘼𝙫𝙖𝙞𝙡𝙖𝙗𝙡𝙚

𝘿𝙚𝙫𝙨🤴:
➖➖➖
<a href="https://t.me/subinps">𝙎𝙐𝘽𝙄𝙉💞</a>
<a href="https://t.me/shamilhabeeb">𝙎𝙃𝘼𝙈𝙄𝙇 𝙃𝙖𝙗𝙚𝙚𝙗🇮🇳</a>
<a href="https://github.com/Mahesh0253">𝙈𝙖𝙝𝙚𝙨𝙝🤖</a>
<a href="https://github.com/pyrogram/pyrogram">𝘿𝘼𝙉🚀</a>
<a href="https://t.me/jack_of_tg">𝙅𝘼𝘾𝙆🤸‍♀️</a>
<a href="https://t.me/Physic_hybrid">𝙋𝙃𝙔𝙎𝙄𝘾_𝙃𝙔𝘽𝙍𝙄𝘿🇵🇹/🇦🇪</a>
<a href="https://github.com/trojanzhex">𝙏𝙧𝙤𝙟𝙖𝙣𝙯🤓</a>
<a href="https://t.me/PowerOfTG">𝙋𝙊𝙒𝙀𝙍 𝙊𝙁 𝙏𝙂 [𝙊𝙁𝙁𝙇𝙄𝙉𝙀]🇮🇳</a>
  """
    MANUELFILTER_TXT = """𝙃𝙚𝙡𝙥: <b>𝙁𝙞𝙡𝙩𝙚𝙧𝙨</b>

- 𝙁𝙞𝙡𝙩𝙚𝙧 𝙞𝙨 𝙩𝙝𝙚 𝙛𝙚𝙖𝙩𝙪𝙧𝙚 𝙬𝙚𝙧𝙚 𝙪𝙨𝙚𝙧𝙨 𝙘𝙖𝙣 𝙨𝙚𝙩 𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙚𝙙 𝙧𝙚𝙥𝙡𝙞𝙚𝙨 𝙛𝙤𝙧 𝙖 𝙥𝙖𝙧𝙩𝙞𝙘𝙪𝙡𝙖𝙧 𝙠𝙚𝙮𝙬𝙤𝙧𝙙  𝙬𝙞𝙡𝙡 𝙧𝙚𝙨𝙥𝙤𝙣𝙙 𝙬𝙝𝙚𝙣𝙚𝙫𝙚𝙧 𝙖 𝙠𝙚𝙮𝙬𝙤𝙧𝙙 𝙞𝙨 𝙛𝙤𝙪𝙣𝙙 𝙩𝙝𝙚 𝙢𝙚𝙨𝙨𝙖𝙜𝙚

<b>𝐍𝐎𝐓𝐄:</b>
1. <a href="https://t.me/Imdbfilter_bot">`×[¤ ​️🇮🇳𝘾𝙞𝙣𝙙𝙚𝙧𝙚𝙡𝙡𝙖 𝙏𝙜🇮🇳¤]×´</a> 𝙎𝙝𝙤𝙪𝙡𝙙 𝙃𝙖𝙫𝙚 𝘼𝙙𝙢𝙞𝙣 𝙋𝙧𝙞𝙫𝙞𝙡𝙡𝙖𝙜𝙚.
2. 𝙊𝙣𝙡𝙮 𝙂𝙧𝙤𝙪𝙥 𝘼𝙙𝙢𝙞𝙣𝙨 𝘾𝙖𝙣 𝘼𝙙𝙙 𝙁𝙞𝙡𝙩𝙚𝙧𝙨 𝙄𝙣 𝘼 𝘾𝙝𝙖𝙩.
3. 𝘼𝙡𝙚𝙧𝙩 𝘽𝙪𝙩𝙩𝙤𝙣𝙨 𝙃𝙖𝙫𝙚 𝘼 𝙇𝙞𝙢𝙞𝙩 𝙊𝙛 64 𝘾𝙝𝙖𝙧𝙚𝙘𝙩𝙚𝙧𝙨.

<b>𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:</b>
• /filter - 𝘼𝙙𝙙 𝙖 𝙛𝙞𝙡𝙩𝙚𝙧 𝙞𝙣 𝙘𝙝𝙖𝙩
• /filters - 𝙇𝙞𝙨𝙩 𝙖𝙡𝙡 𝙩𝙝𝙚 𝙛𝙞𝙡𝙩𝙚𝙧𝙨 𝙤𝙛 𝙖 𝙘𝙝𝙖𝙩
• /del - 𝘿𝙚𝙡𝙚𝙩𝙚 𝙖 𝙨𝙥𝙚𝙘𝙞𝙛𝙞𝙘 𝙛𝙞𝙡𝙩𝙚𝙧 𝙞𝙣 𝙘𝙝𝙖𝙩
• /delall - 𝘿𝙚𝙡𝙚𝙩𝙚 𝙩𝙝𝙚 𝙬𝙝𝙤𝙡𝙚 𝙛𝙞𝙡𝙩𝙚𝙧𝙨 𝙞𝙣 𝙖 𝙘𝙝𝙖𝙩 (𝙘𝙝𝙖𝙩 𝙤𝙬𝙣𝙚𝙧 𝙤𝙣𝙡𝙮)"""
    BUTTON_TXT = """𝐇𝐞𝐥𝐩: <b>𝘽𝙪𝙩𝙩𝙤𝙣𝙨</b>

- <a href="https://t.me/Imdbfilter_bot">`×[¤ ​️🇮🇳𝘾𝙞𝙣𝙙𝙚𝙧𝙚𝙡𝙡𝙖 𝙏𝙜🇮🇳¤]×´</a> 𝙎𝙪𝙥𝙥𝙤𝙧𝙩𝙨 𝙗𝙤𝙩𝙝 𝙪𝙧𝙡 𝙖𝙣𝙙 𝙖𝙡𝙚𝙧𝙩 𝙞𝙣𝙡𝙞𝙣𝙚 𝙗𝙪𝙩𝙩𝙤𝙣𝙨.

<b>𝐍𝐨𝐭𝐞:</b>
1. 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙬𝙞𝙡𝙡 𝙣𝙤𝙩 𝙖𝙡𝙡𝙤𝙬𝙨 𝙮𝙤𝙪 𝙩𝙤 𝙨𝙚𝙣𝙙 𝙗𝙪𝙩𝙩𝙤𝙣𝙨 𝙬𝙞𝙩𝙝𝙤𝙪𝙩 𝙖𝙣𝙮 𝙘𝙤𝙣𝙩𝙚𝙣𝙩, 𝙨𝙤 𝙘𝙤𝙣𝙩𝙚𝙣𝙩 𝙞𝙨 𝙢𝙖𝙣𝙙𝙖𝙩𝙤𝙧𝙮.
2. <a href="https://t.me/Imdbfilter_bot">`×[¤ ​️🇮🇳𝘾𝙞𝙣𝙙𝙚𝙧𝙚𝙡𝙡𝙖 𝙏𝙜🇮🇳¤]×´</a> 𝙨𝙪𝙥𝙥𝙤𝙧𝙩𝙨 𝙗𝙪𝙩𝙩𝙤𝙣𝙨 𝙬𝙞𝙩𝙝 𝙖𝙣𝙮 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙢𝙚𝙙𝙞𝙖 𝙩𝙮𝙥𝙚.
3. 𝘽𝙪𝙩𝙩𝙤𝙣𝙨 𝙨𝙝𝙤𝙪𝙡𝙙 𝙗𝙚 𝙥𝙧𝙤𝙥𝙚𝙧𝙡𝙮 𝙥𝙖𝙧𝙨𝙚𝙙 𝙖𝙨 𝙢𝙖𝙧𝙠𝙙𝙤𝙬𝙣 𝙛𝙤𝙧𝙢𝙖𝙩

<b>𝐔𝐑𝐋 𝐛𝐮𝐭𝐭𝐨𝐧𝐬:</b>
<code>[Button Text](buttonurl:https//t.me/Cinderella)</code>

<b>𝐀𝐥𝐞𝐫𝐭 𝐛𝐮𝐭𝐭𝐨𝐧𝐬:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """𝐇𝐞𝐥𝐩: <b>𝘼𝙪𝙩𝙤 𝙁𝙞𝙡𝙩𝙚𝙧</b>

<b>𝐍𝐎𝐓𝐄:</b>
1. 𝙈𝙖𝙠𝙚 𝙢𝙚 𝙩𝙝𝙚 𝙖𝙙𝙢𝙞𝙣 𝙤𝙛 𝙮𝙤𝙪𝙧 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙞𝙛 𝙞𝙩'𝙨 𝙥𝙧𝙞𝙫𝙖𝙩𝙚.
2. 𝙢𝙖𝙠𝙚 𝙨𝙪𝙧𝙚 𝙩𝙝𝙖𝙩 𝙮𝙤𝙪𝙧 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙙𝙤𝙚𝙨 𝙣𝙤𝙩 𝙘𝙤𝙣𝙩𝙖𝙞𝙣𝙨 𝙘𝙖𝙢 𝙧𝙞𝙥, 𝙥𝙤𝙧𝙣 𝙖𝙣𝙙 𝙛𝙖𝙠𝙚 𝙛𝙞𝙡𝙚𝙨.
3. 𝙁𝙤𝙧𝙬𝙖𝙧𝙙 𝙩𝙝𝙚 𝙡𝙖𝙨𝙩 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙩𝙤 𝙢𝙚 𝙬𝙞𝙩𝙝 𝙦𝙪𝙤𝙩𝙚𝙨.
4. 𝙄'𝙡𝙡 𝙖𝙙𝙙 𝙖𝙡𝙡 𝙩𝙝𝙚 𝙛𝙞𝙡𝙚𝙨 𝙞𝙣 𝙩𝙝𝙖𝙩 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙩𝙤 𝙢𝙮 𝙙𝙗."""
    CONNECTION_TXT = """𝐇𝐞𝐥𝐩: <b>𝘾𝙤𝙣𝙣𝙚𝙘𝙩𝙞𝙤𝙣𝙨</b>

- 𝙐𝙨𝙚𝙙 𝙩𝙤 𝙘𝙤𝙣𝙣𝙚𝙘𝙩 𝙗𝙤𝙩 𝙩𝙤 𝙋𝙈 𝙛𝙤𝙧 𝙢𝙖𝙣𝙖𝙜𝙞𝙣𝙜 𝙛𝙞𝙡𝙩𝙚𝙧𝙨 
- 𝙞𝙩 𝙝𝙚𝙡𝙥𝙨 𝙩𝙤 𝙖𝙫𝙤𝙞𝙙 𝙨𝙥𝙖𝙢𝙢𝙞𝙣𝙜 𝙞𝙣 𝙜𝙧𝙤𝙪𝙥𝙨.

<b>𝐍𝐎𝐓𝐄:</b>
1. 𝙊𝙣𝙡𝙮 𝙖𝙙𝙢𝙞𝙣𝙨 𝙘𝙖𝙣 𝙖𝙙𝙙 𝙖 𝙘𝙤𝙣𝙣𝙚𝙘𝙩𝙞𝙤𝙣.
2. 𝙎𝙚𝙣𝙙 <code>/connect</code> 𝙛𝙤𝙧 𝙘𝙤𝙣𝙣𝙚𝙘𝙩𝙞𝙣𝙜 𝙢𝙚 𝙩𝙤 𝙪𝙧 𝙋𝙈

<b>𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """𝐇𝐞𝐥𝐩: <b>Extra Modules</b>

<b>𝐍𝐎𝐓𝐄:</b>
these are the extra features of 𝕮𝖎𝖓𝖉𝖊𝖗𝖊𝖑𝖑𝖆

<b>𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """𝐇𝐞𝐥𝐩: <b>Admin mods</b>

<b>𝐍𝐎𝐓𝐄:</b>
This module only works for my admins

<b>𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """✪ 𝑻𝒐𝒕𝒂𝒍 𝒇𝒊𝒍𝒆𝒔: <code>{}</code>
✪ 𝑻𝒐𝒕𝒂𝒍 𝑼𝒔𝒆𝒓𝒔: <code>{}</code>
✪ 𝑻𝒐𝒕𝒂𝒍 𝑪𝒉𝒂𝒕𝒔: <code>{}</code>
✪ 𝑼𝒔𝒆𝒅 𝑺𝒕𝒐𝒓𝒂𝒈𝒆: <code>{}</code> 𝙼𝚒𝙱
✪ 𝑭𝒓𝒆𝒆 𝑺𝒕𝒐𝒓𝒂𝒈𝒆: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """👩‍👩‍👦‍👦New Fam👩‍👩‍👦‍👦
♻️Group = {}(<code>{}</code>)
👩‍👩‍👦‍👦Total Members = <code>{}</code>
➕️Added By - {}
"""
    LOG_TEXT_P = """💞New Chunk💞
☯️ID - <code>{}</code>
🗣️Name - {}
"""
