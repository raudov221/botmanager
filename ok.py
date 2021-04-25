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
        data[ "car" ][ str( ans.from_id ) ] = "pass"
        data[ "carname" ][ str( ans.from_id ) ] = "pass"
        data[ "reg" ][ str( ans.from_id ) ] = "0"
        json.dump( data, open( "data.json", "w" ) )


user = User("8765abf0de381e03f5fe3a5f5a8f38e286e7283501c397ee47cdd5e3840d3b4f86e7824574e32838a51f9", mobile = True)

@user.on.message_handler(text="пошел нахуй")
async def wrapper(ans: Message):
    id = ans.id
    await ans("так во первых твоя мать шлюха, нахуя пишешь пошел нахуй если ты сосешь лорду то есть мне каждый день. научи свою мать не сосать мне.", reply_to=id)
    
@user.on.message_handler(text="сколько <da>")
async def wrapper(ans: Message, da):
	a = random.randint(0, 100)
	await ans(f"{a}😵")

@user.on.message_handler(text="eval <da>")
async def wrapper(ans: Message, da):
	if ans.from_id == 597825377:
		c = eval(da)
		await ans(f"Вывод: {c}")

@user.on.message_handler(text="скам")
async def wrapper(ans: Message):
	data = json.load( open( "data.json", "r" ) )
	a = random.randint(500, 4000)
	if a == 500:
		await ans("🦊 На ваш пожаловались, за обман на деньги и вам пришлось отдать долг.")
	else:
		data["balance"][str(ans.from_id)] + int(a)
		json.dump( data, open( "data.json", "w" ) )
		await ans(f"📄 Вы успешно обманули на {a}! Ваш баланс: {data['balance'][str(ans.from_id)]} монет", reply_to=ans.id)

@user.on.message_handler(text="баланс", lower = True)
async def wrapper(ans: Message):
	data = json.load( open( "data.json", "r" ) )
	await ans(f"💸 {data['name'][str(ans.from_id)]}, ваш баланс: {data['balance'][str(ans.from_id)]}")
	
@user.on.message_handler(text="машины", lower = True)
async def wrapper(ans: Message):
	data = json.load( open( "data.json", "r" ) )
	await ans(f"🚙 {data['name'][str(ans.from_id)]}, машины:\n\n🚚 1. Aveo - 200к\n🚗 2. Polo VI - 500к\n🏎️ 3. Aventador - 1кк\n\n🔘 Для покупки авто вы должны написать команду - 'купить машину <номер машины>'!")
	
@user.on.message_handler(text="купить машину <nomer>")
async def wrapper(ans: Message, nomer):
	data = json.load( open( "data.json", "r" ) )
	if int(nomer) < 3:
		await ans("🚙 Данного номера авто нету!")
	else:
		a = nomer.replace("1","Aveo")
		a = nomer.replace("2","Polo VI")
		a = nomer.replace("3","Aventador")
		if int(nomer) == 1:
			if int(data['balance'][str(ans.from_id)]) > 200000:
				await ans("🔮 Вы приобрели авто под номером 1!")
				data["balance"][str(ans.from_id)] -200000
				data["carname"][str(ans.from_id)] = str(a)
				data["car"][str(ans.from_id)] = int(nomer)
				json.dump( data, open( "data.json", "w" ) )
		if int(nomer) == 2:
			if int(data['balance'][str(ans.from_id)]) > 500000:
				await ans("🔮 Вы приобрели авто под номером 1!")
				data["balance"][str(ans.from_id)] -500000
				data["carname"][str(ans.from_id)] = str(a)
				data["car"][str(ans.from_id)] = int(nomer)
				json.dump( data, open( "data.json", "w" ) )
		if int(nomer) == 3:
			if int(data['balance'][str(ans.from_id)]) > 1000000:
				await ans("🔮 Вы приобрели авто под номером 1!")
				data["balance"][str(ans.from_id)] -1000000
				
				data["carname"][str(ans.from_id)] = str(a)
				data["car"][str(ans.from_id)] = int(nomer)
				json.dump( data, open( "data.json", "w" ) )

@user.on.message_handler(text="клик")
async def wrapper(ans: Message):
	a = 100
	data = json.load( open( "data.json", "r" ) )
	data["balance"][str(ans.from_id)] + int(a)
	await ans(f"💸 {data['name'][str(ans.from_id)]}, вы кликнули и получили 100 монет, ваш баланс: {data['balance'][str(ans.from_id)]}")
	json.dump( data, open( "data.json", "w" ) )

@user.on.message_handler(text="профиль", lower = True)
async def wrapper(ans: Message):
	data = json.load( open( "data.json", "r" ) )
	await ans(f"🦊 {data['name'][str(ans.from_id)]}, ваш профиль:\n\n💵 Баланс: {data['balance'][str(ans.from_id)]}\n🚗 Машина: {data['carname'][str(ans.from_id)]}\n🪐 Id: {ans.from_id}")

@user.on.message_handler(text="дроби <num1>/<num2> - <num3>/<num4>", lower = True)
async def wrapper(ans: Message, num1, num2, num3, num4):
	c = num2 * num4
	x = num1 - num3
	id = ans.id
	data = json.load( open( "data.json", "r" ) )
	await ans(f"{data['name'][str(ans.from_id)]}, решение: \n{num1}/{num2}-{num3}/{num4} = {num1}-{num3}/{c} = {x}/{c}", reply_to = id) 

@user.on.message_handler(text="<da>")
async def wrapper(ans: Message, da):
	reg(ans)
	c = ans.from_id
	id = ans.id
	data = json.load( open( "data.json", "r" ) )
	if data[ "reg" ][ str( ans.from_id ) ] == "0":
		name = await user.api.users.get(user_ids=c)
		data[ "name" ][ str( ans.from_id ) ] = f"[id{c}|{name[0].first_name}]"
		await user.api.messages.send(user_id=c, random_id=0, message=f"🦊 {data['name'][str(ans.from_id)]}, ты успешно зарегистрировался!")
		data[ "reg" ][ str( ans.from_id ) ] = "1"
		json.dump( data, open( "data.json", "w" ) )
		print("reg")
	else:
		print("no reg")


user.run_polling()
