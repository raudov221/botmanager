from vkbottle.user import User, Message
from vkbottle.api import API
from rextester_py import rexec_aio
import math
import random

user = User("5fd5ac6e233fc14f2b7936ae51378d81cc88af854d76baa83706841cf08714103a40f1ec96b54929795dd")
api = API("5fd5ac6e233fc14f2b7936ae51378d81cc88af854d76baa83706841cf08714103a40f1ec96b54929795dd")

@user.on.message_handler(text="стикеры")
async def wrapper(ans: Message):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    all_stickers = await api.request('gifts.getCatalog', {'user_id': ans.reply_message.from_id})
    stickers = [f"{i['sticker_pack']['title']},"
    for i in all_stickers[1]['items'] if 'disabled' in i]
    return f"🤑 [id{ans.from_id}|{penis[0].first_name}], его стикеры:\n\n{stickers}"

@user.on.message_handler(text="<da>+<net>")
async def wrapper(ans: Message, da, net: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    c = da + net
    return f"😎 [id{ans.from_id}|{penis[0].first_name}], ответ: {c}"

@user.on.message_handler(text="<da>-<net>")
async def wrapper(ans: Message, da, net: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    c = da - net
    return f"😎 [id{ans.from_id}|{penis[0].first_name}], ответ: {c}"

@user.on.message_handler(text="<da>*<net>")
async def wrapper(ans: Message, da, net: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    c = da * net
    return f"😎 [id{ans.from_id}|{penis[0].first_name}], ответ: {c}"

@user.on.message_handler(text="<da>/<net>")
async def wrapper(ans: Message, da, net: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    c = da / net
    return f"😎 [id{ans.from_id}|{penis[0].first_name}], ответ: {c}"

user.run_polling()
