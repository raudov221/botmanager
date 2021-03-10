from vkbottle.user import User, Message
from vkbottle.api import API
from rextester_py import rexec_aio
import math
import random

user = User("1a8b582c0be06bb4fcfa390811ac20106ecbecafa4590779b11f9f75573524795bc3619a85e6ad5699ea1")

@user.on.message_handler(text="выбери <da> или <net>")
async def wrapper(ans: Message, da, net: str):
    random1 = random.randint(1, 2)
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    if da in ["vto.ре", "https://vto.ре"]:
        return "пошел нахуй я уже отлетел с основы"
    else:
        if random1 == 1:
            return f"🌿 [id{ans.from_id}|{penis[0].first_name}], Я выбрал: {da}"
        else:
            return f"🌿 [id{ans.from_id}|{penis[0].first_name}], Я выбрал: {net}"
    if net in ["vto.ре", "https://vto.ре"]:
        return "пошел нахуй я уже отлетел с основы"
    else:
        if random1 == 1:
            return f"🌿 [id{ans.from_id}|{penis[0].first_name}], Я выбрал: {da}"
        else:
            return f"🌿 [id{ans.from_id}|{penis[0].first_name}], Я выбрал: {net}"

user.run_polling()
