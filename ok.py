from vkbottle.user import User, Message
from vkbottle import PhotoUploader
import random

blocked = ["porno365", "porno", "xnxx", "vto", "vto.pe", "ru", "com", "pe"]


user = User("f316473ce9ae540331f5fe8cbdc1bd1c7901324b1ca0b42648be820b589b00f17f7ccb94646b7d32cd9c2")

@user.on.message_handler(text=".иван <da> до <da1>", lower = True)
async def wrapper(ans: Message, da, da1):
	a = random.randint(da, da1)
	await ans("вам выпало {a}")


user.run_polling()
