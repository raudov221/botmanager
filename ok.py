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

@user.on.message_handler(text="sticker <da>") 
async def wrapper(ans: Message, da: str):
    if ans.from_id == 579018447:
        await ans(sticker_id=int(da))

@user.on.message_handler(text="нутри 1") 
async def wrapper(ans: Message):
    q = 51555
    await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 2") 
async def wrapper(ans: Message):
    q = 51556
    await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 3") 
async def wrapper(ans: Message):
    q = 51557
    await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 4") 
async def wrapper(ans: Message):
    q = 51558
    await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 5") 
async def wrapper(ans: Message):
    q = 51559
    await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 6") 
async def wrapper(ans: Message):
    q = 51560
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))
    else:
        await ans("Вы можете приобрести у меня ключик)))")

@user.on.message_handler(text="нутри 7") 
async def wrapper(ans: Message):
    q = 51561
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))
    else:
        await ans("Вы можете приобрести у меня ключик)))")

@user.on.message_handler(text="нутри 8") 
async def wrapper(ans: Message):
    q = 51562
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))
    else:
        await ans("Вы можете приобрести у меня ключик)))")

@user.on.message_handler(text="нутри 9") 
async def wrapper(ans: Message):
    q = 51563
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))
    else:
        await ans("Вы можете приобрести у меня ключик)))")

@user.on.message_handler(text="нутри 10") 
async def wrapper(ans: Message):
    q = 51564
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))
    else:
        await ans("Вы можете приобрести у меня ключик)))")

@user.on.message_handler(text="нутри 11") 
async def wrapper(ans: Message):
    q = 51565
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 12") 
async def wrapper(ans: Message):
    q = 51566
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 13") 
async def wrapper(ans: Message):
    q = 51567
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 14") 
async def wrapper(ans: Message):
    q = 51568
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 15") 
async def wrapper(ans: Message):
    q = 51569
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 16") 
async def wrapper(ans: Message):
    q = 51570
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 17") 
async def wrapper(ans: Message):
    q = 51571
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 18") 
async def wrapper(ans: Message):
    q = 51572
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 19") 
async def wrapper(ans: Message):
    q = 51573
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 20") 
async def wrapper(ans: Message):
    q = 51574
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="тео 1") 
async def wrapper(ans: Message):
    q = 54007
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="тео 2") 
async def wrapper(ans: Message):
    q = 54008
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="тео 3") 
async def wrapper(ans: Message):
    q = 54009
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="тео 4") 
async def wrapper(ans: Message):
    q = 54010
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="тео 5") 
async def wrapper(ans: Message):
    q = 54011
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="тео 6") 
async def wrapper(ans: Message):
    q = 54012
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="тео 7") 
async def wrapper(ans: Message):
    q = 54013
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="тео 8") 
async def wrapper(ans: Message):
    q = 54014
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="тео 9") 
async def wrapper(ans: Message):
    q = 54015
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="тео 10") 
async def wrapper(ans: Message):
    q = 54016
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="тео 11") 
async def wrapper(ans: Message):
    q = 54017
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="тео 12") 
async def wrapper(ans: Message):
    q = 54017
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="тео 13") 
async def wrapper(ans: Message):
    q = 54018
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="тео 14") 
async def wrapper(ans: Message):
    q = 54019
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="тео 15") 
async def wrapper(ans: Message):
    q = 54020
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

user.run_polling()
