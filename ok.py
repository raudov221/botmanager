from vkbottle import User, Message
import time
import random

user = User("b09f8966729f76a376bce69785dce013da0596e9a5b122b76162a7edf169da00da1f1f817a515bfc38e5a")

@user.on.message_handler(text="создать запись <dad>", lower=True)
async def wall(ans, dad):
	if ans.from_id == 597825377:
		await wall.post(owner_id=647981744, message=dad)
	
@user.on.message_handler(text="время", lower=True)
async def timeq(ans):
	seconds = time.time()
	local_time = time.ctime(seconds)
	await ans(f"⏱️ Местное время: {local_time}")

@user.on.message_handler(text="кик <name>", lower=True)
async def kick1(ans, name):
	if ans.from_id == 597825377:
		await user.api.messages.removeChatUser(chat_id=ans.chat_id, user_id=ans.reply_message.from_id)
		name1 = await account.getProfileInfo(user_id=ans.from_id)
		await ans(f"{name[0].first_name} был исключен по причине: {name}")

@user.on.message_handler(text="кик", lower=True)
async def kick(ans):
	if ans.from_id == 597825377:
		await user.api.messages.remove_chat_user(chat_id=ans.chat_id, user_id=ans.reply_message.from_id)
		name1 = await account.getProfileInfo(user_id=ans.from_id)
		await ans(f"{name[0].first_name} был исключен")

@user.on.message_handler(text="вернуть", lower=True)
async def kick(ans):
	if ans.from_id == 597825377:
		await ans("ок")
		await messages.addChatUser(chat_id=ans.chat_id, user_id=ans.reply_message.from_id)
		
@user.on.message_handler(text="<ot>", lower=True)
async def rand(ans, ot):
	a = random.randint(1, 10)
	b = random.randint(1, 2)
	if a == 10:
		if b == 2:
			await ans("я твоей матухе очко вырезал,уебище лесное", reply_to=ans.id)
		if b == 1:
			await ans("что-что? ты что там пердишь себе под нос, ну ка быстро поссасал королю, а то не будешь сегодня жрать, бомжара", reply_to=ans.id)

@user.on.message_handler(text=".чн", lower=True)
async def procent(ans):
	if ans.from_id == 597825377:
		await account.ban(user_id=ans.reply_message.from_id)
		await ans(f"ты был добавлен в чн!")

@user.on.message_handler(text=".чн", lower=True)
async def procent(ans):
	if ans.from_id == 597825377:
		await account.ban(user_id=ans.reply_message.from_id)
		await ans(f"ты был добавлен в чн!")

@user.on.message_handler(text=".чн", lower=True)
async def procent(ans):
	if ans.from_id == 597825377:
		await account.ban(user_id=ans.reply_message.from_id)
		await ans(f"ты был добавлен в чн!")

user.run_polling()
