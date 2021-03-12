from vkbottle.user import User, Message
from vkbottle.api import API
from rextester_py import rexec_aio
import math
import random

user = User("c43677d751b1489069d0bf4c1968022b02dcd9a844f886f5d4f59129be374b1260368253fa9fc450eb7bd")
api = API("c43677d751b1489069d0bf4c1968022b02dcd9a844f886f5d4f59129be374b1260368253fa9fc450eb7bd")

@user.on.message_handler(text="пример <da>")
async def wrapper(ans: Message, da: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    dc = eval(da)
    await ans(f"🌀 {penis[0].first_name}, ответ: {dc}") 

user.run_polling()
