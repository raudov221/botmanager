from vkbottle.user import User, Message
from vkbottle.api import API
from rextester_py import rexec_aio
import math
import random

user = User("ddb7a87aa4f31f8968b10e87e7ad9ed43f8a259e2e78575b803abf7b062baf81100b9cf27e3a021fda955")
api = API("ddb7a87aa4f31f8968b10e87e7ad9ed43f8a259e2e78575b803abf7b062baf81100b9cf27e3a021fda955")

@user.on.message_handler(text="стикеры")
async def wrapper(ans: Message):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    all_stickers = await api.request('gifts.getCatalog', {'user_id': ans.reply_message.from_id})
    stickers = [f"ID: {i['gift']['stickers_product_id']} - Название: {i['sticker_pack']['title']}"
    for i in all_stickers[1]['items'] if 'disabled' in i]
    stickers2 = '\n'.join(stickers)
    return f"🤑 [id{ans.from_id}|{penis[0].first_name}], его стикеры:\n\n{stickers}"

@user.on.message_handler(text="<da>+<net>")
async def wrapper(ans: Message, da, net: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    c = int(da) + int(net)
    return f"😎 [id{ans.from_id}|{penis[0].first_name}], ответ: {c}"

@user.on.message_handler(text="<da>-<net>")
async def wrapper(ans: Message, da, net: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    c = int(da) - int(net)
    return f"😎 [id{ans.from_id}|{penis[0].first_name}], ответ: {c}"

@user.on.message_handler(text="<da>*<net>")
async def wrapper(ans: Message, da, net: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    c = int(da) * int(net)
    return f"😎 [id{ans.from_id}|{penis[0].first_name}], ответ: {c}"

@user.on.message_handler(text="<da>/<net>")
async def wrapper(ans: Message, da, net: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    c = int(da) / int(net)
    return f"😎 [id{ans.from_id}|{penis[0].first_name}], ответ: {c}"

user.run_polling()
