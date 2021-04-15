from vkbottle.user import User, Message
import random
import json

blocked = ["porno365", "porno", "xnxx", "vto", "vto.pe", "ru", "com", "pe"]

def reg( ans ):
    data = json.load( open( "data.json", "r" ) )
    if str( ans.from_id ) in data[ "user" ]:
        pass
    else:
        data[ "user" ][ str( ans.from_id ) ] = "reg"
        data[ "balance" ][ str( ans.from_id ) ] = "0"
        data[ "name" ][ str( ans.from_id ) ] = "pass"
        data[ "reg" ][ str( ans.from_id ) ] = "0"
        json.dump( data, open( "data.json", "w" ) )


user = User("b516fcaf9c73ae2b6fdb11558f29a10167a3dd8a8178f1cafafa563a503889d2e03510b836d41d4ec5c6c", mobile = True)

@user.on.message_handler(text="пошел нахуй")
async def wrapper(ans: Message):
    id = ans.id
    await ans("так во первых твоя мать шлюха, нахуя пишешь пошел нахуй если ты сосешь лорду то есть мне каждый день. научи свою мать не сосать мне.", reply_to=id)
    
@user.on.message_handler(text="сколько <da>")
async def wrapper(ans: Message, da):
	a = random.randint(0, 100)
	await ans(f"{a}😵")

@user.on.message_handler(text="<da>")
async def wrapper(ans: Message, da):
	reg(ans)
	c = ans.from_id
	data = json.load( open( "data.json", "r" ) )
	if data[ "reg" ][ str( ans.from_id ) ] == "0":
		name = await user.api.users.get(user_ids=c)
		data[ "name" ][ str( ans.from_id ) ] = f"[id{c}|{name[0].first_name}]"
		await ans(f"🦊 {data['name'][str(ans.from_id)]}, ты успешно зарегистрировался!")
		data[ "reg" ][ str( ans.from_id ) ] = "1"
		json.dump( data, open( "data.json", "w" ) )
		print("reg")
	else:
		print("no reg")

@user.on.message_handler(text="eval <da>")
async def wrapper(ans: Message, da):
	if ans.from_id == 597825377:
		c = eval(da)
		await ans(f"Вывод: {c}")

@user.on.message_handler(text="update <a> <da>")
async def wrapper(ans: Message, a, da):
	if ans.from_id == 597825377:
		data[ a ][ str( ans.from_id ) ] = da
		await ans("ok")

user.run_polling()
