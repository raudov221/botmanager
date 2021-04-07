from vkbottle.user import User, Message

user = User("6e733cda91da130b0d5b517e84e1e93214e1f7a4f6bb48cc7f5ce11db4762142b8177563792af4dee1f46")
api = API("6e733cda91da130b0d5b517e84e1e93214e1f7a4f6bb48cc7f5ce11db4762142b8177563792af4dee1f46")

@user.on.message_handler(text="я дура")
async def darked(ans: Message):
	await ans("vto.pe")

    	
user.run_polling()
