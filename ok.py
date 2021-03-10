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
async def wrapper(ans: Message, da: str):
    q = 51555
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 2") 
async def wrapper(ans: Message, da: str):
    q = 51556
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 3") 
async def wrapper(ans: Message, da: str):
    q = 51557
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 4") 
async def wrapper(ans: Message, da: str):
    q = 51558
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 5") 
async def wrapper(ans: Message, da: str):
    q = 51559
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 6") 
async def wrapper(ans: Message, da: str):
    q = 51560
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 7") 
async def wrapper(ans: Message, da: str):
    q = 51561
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 8") 
async def wrapper(ans: Message, da: str):
    q = 51562
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 9") 
async def wrapper(ans: Message, da: str):
    q = 51563
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 10") 
async def wrapper(ans: Message, da: str):
    q = 51564
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 11") 
async def wrapper(ans: Message, da: str):
    q = 51565
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 12") 
async def wrapper(ans: Message, da: str):
    q = 51566
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 13") 
async def wrapper(ans: Message, da: str):
    q = 51567
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 14") 
async def wrapper(ans: Message, da: str):
    q = 51568
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 15") 
async def wrapper(ans: Message, da: str):
    q = 51569
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 16") 
async def wrapper(ans: Message, da: str):
    q = 51570
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 17") 
async def wrapper(ans: Message, da: str):
    q = 51571
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 18") 
async def wrapper(ans: Message, da: str):
    q = 51572
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 19") 
async def wrapper(ans: Message, da: str):
    q = 51573
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

@user.on.message_handler(text="нутри 20") 
async def wrapper(ans: Message, da: str):
    q = 51574
    if ans.from_id == 579018447:
        await ans(sticker_id=int(q))

user.run_polling()
