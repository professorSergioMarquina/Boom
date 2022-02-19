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

<b>NOTE:</b>
1. <a href="https://t.me/Imdbfilter_bot">`×[¤ ​️🇮🇳𝘾𝙞𝙣𝙙𝙚𝙧𝙚𝙡𝙡𝙖 𝙏𝙜🇮🇳¤]×´</a> 𝙎𝙝𝙤𝙪𝙡𝙙 𝙃𝙖𝙫𝙚 𝘼𝙙𝙢𝙞𝙣 𝙋𝙧𝙞𝙫𝙞𝙡𝙡𝙖𝙜𝙚.
2. 𝙊𝙣𝙡𝙮 𝙂𝙧𝙤𝙪𝙥 𝘼𝙙𝙢𝙞𝙣𝙨 𝘾𝙖𝙣 𝘼𝙙𝙙 𝙁𝙞𝙡𝙩𝙚𝙧𝙨 𝙄𝙣 𝘼 𝘾𝙝𝙖𝙩.
3. 𝘼𝙡𝙚𝙧𝙩 𝘽𝙪𝙩𝙩𝙤𝙣𝙨 𝙃𝙖𝙫𝙚 𝘼 𝙇𝙞𝙢𝙞𝙩 𝙊𝙛 64 𝘾𝙝𝙖𝙧𝙚𝙘𝙩𝙚𝙧𝙨.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- 𝕮𝖎𝖓𝖉𝖊𝖗𝖊𝖑𝖑𝖆  Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. 𝕮𝖎𝖓𝖉𝖊𝖗𝖊𝖑𝖑𝖆 supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/𝕮𝖎𝖓𝖉𝖊𝖗𝖊𝖑𝖑𝖆)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of 𝕮𝖎𝖓𝖉𝖊𝖗𝖊𝖑𝖑𝖆

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
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
