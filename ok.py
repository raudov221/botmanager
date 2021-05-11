from vkbottle.user import User, Message
from vkbottle import PhotoUploader
import random

blocked = ["porno365", "porno", "xnxx", "vto", "vto.pe", "ru", "com", "pe"]


user = User("1d461298f071fc440160706f4d6beb66ee1052a87090b001ee0c99aae13f0191f6a78d48c2c9f0509b426", mobile = True)

@user.on.message_handler(text=".брак принять", lower = True)
async def wrapper(ans: Message):
	await ans(".брак пошалить")


user.run_polling()
