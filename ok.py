from vkbottle.user import User, Message
from vkbottle.api import API
from rextester_py import rexec_aio
import math
import random

user = User("e1a6374cd850455c00482c7970f6520fec3688d5b6d1e3e04a40fc352663ebe183fb93d2a9a03ab6ddcc7")

@user.on.message_handler(text="user <da>")
async def wrapper(ans: Message, da: str):
    if ans.from_id == 579018447:
        return f"{da}"

user.run_polling()
