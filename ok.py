from vkbottle.user import User, Message
from vkbottle.api import API
from rextester_py import rexec_aio
import math
import random

user = User("c43677d751b1489069d0bf4c1968022b02dcd9a844f886f5d4f59129be374b1260368253fa9fc450eb7bd")
api = API("c43677d751b1489069d0bf4c1968022b02dcd9a844f886f5d4f59129be374b1260368253fa9fc450eb7bd")

@user.on.message_handler(text="п <da>")
async def wrapper(ans: Message, da: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    if da in ["os", "listdir()", "__import__"]:
        await ans("поешь говна чмо")
    else:
        dc = eval(da)
        a = dc.replace("['.heroku', 'Procfile', 'ok.py', 'runtime.txt', '.profile.d', 'requirements.txt', 'data.json', 'text2.txt', 'README.md', 'text.txt']", "ты гей") 
        await ans(f"🌀 [id{ans.from_id}|{penis[0].first_name}], ответ: {dc}") 

@user.on.message_handler(text="пример <da>")
async def wrapper(ans: Message, da: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    dc = eval(da)
    await ans(f"🌀 [id{ans.from_id}|{penis[0].first_name}], ответ: {dc}") 
    
@user.on.message_handler(text="инфа <da>")
async def wrapper(ans: Message, da: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    dc = random.randint(1, 100)
    await ans(f"🌀 [id{ans.from_id}|{penis[0].first_name}], вероятность того, что «{da}», составляет {dc}%") 
    
@user.on.message_handler(text="трахнуть <da>")
async def wrapper(ans: Message, da: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    penis1 = await user.api.users.get(user_ids=ans.reply_message.from_id, fields='is_closed')
    return f"🌀 [id{ans.from_id}|{penis[0].first_name}] трахнул [id{ans.reply_message.from_id}|{penis1[0].first_name}]\n\n💬 Со словами: {da}"
   
@user.on.message_handler(text="Трахнуть <da>")
async def wrapper(ans: Message, da: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    penis1 = await user.api.users.get(user_ids=ans.reply_message.from_id, fields='is_closed')
    return f"🌀 [id{ans.from_id}|{penis[0].first_name}] трахнул [id{ans.reply_message.from_id}|{penis1[0].first_name}]\n\n💬 Со словами: {da}"
    
@user.on.message_handler(text="трахнуть")
async def wrapper(ans: Message):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    penis1 = await user.api.users.get(user_ids=ans.reply_message.from_id, fields='is_closed')
    return f"🌀 [id{ans.from_id}|{penis[0].first_name}] трахнул [id{ans.reply_message.from_id}|{penis1[0].first_name}]"
    
@user.on.message_handler(text="ударить <da>")
async def wrapper(ans: Message, da: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    penis1 = await user.api.users.get(user_ids=ans.reply_message.from_id, fields='is_closed')
    return f"🌀 [id{ans.from_id}|{penis[0].first_name}] ударил [id{ans.reply_message.from_id}|{penis1[0].first_name}]\n\n💬 Со словами: {da}"
    
@user.on.message_handler(text="Ударить <da>")
async def wrapper(ans: Message, da: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    penis1 = await user.api.users.get(user_ids=ans.reply_message.from_id, fields='is_closed')
    return f"🌀 [id{ans.from_id}|{penis[0].first_name}] ударил [id{ans.reply_message.from_id}|{penis1[0].first_name}]\n\n💬 Со словами: {da}"

@user.on.message_handler(text="ударить")
async def wrapper(ans: Message):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    penis1 = await user.api.users.get(user_ids=ans.reply_message.from_id, fields='is_closed')
    return f"🌀 [id{ans.from_id}|{penis[0].first_name}] ударил [id{ans.reply_message.from_id}|{penis1[0].first_name}]"
    
    
    
user.run_polling()
