import os
from pyrogram import Client, filters
from pyrogram.types import Message, User



@Client.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"Welcome {message.from_user.mention} brooh!💞 to {message.chat.username} ,  Please Provide Correct Spelling Of Movie To Get That✌️Either Not Get Movie... Enjoy.... 😛",chat_id=chatid)
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"😏 Bye ,  {message.from_user.mention} , ഇനി ഈ പരിസരത്തു കണ്ട് പോവരുത്🤧",chat_id=chatid)
	

