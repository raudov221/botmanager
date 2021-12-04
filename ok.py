from vkbottle.user import User, Message
from vkbottle.api import API
from rextester_py import rexec_aio
import math
import random

user = User("279db29b3e03042c043dd724d7e876ee98744aea1c4268aa701a1b0f382a605c1f0da8b75b583d693e8b1")
api = API("279db29b3e03042c043dd724d7e876ee98744aea1c4268aa701a1b0f382a605c1f0da8b75b583d693e8b1")

@user.on.message_handler(text="стикеры")
async def wrapper(ans: Message):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    all_stickers = await api.request('gifts.getCatalog', {'user_id': ans.reply_message.from_id})
    stickers = [f"ID: {i['gift']['stickers_product_id']} - Название: {i['sticker_pack']['title']}"
    for i in all_stickers[1]['items'] if 'disabled' in i]
    stickers2 = '\n'.join(stickers)
    return f"🤑 [id{ans.from_id}|{penis[0].first_name}], его стикеры:\n\n{stickers2}"

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
