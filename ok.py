from vkbottle.bot import Bot, Message
from vkbottle.keyboard import Keyboard, Text
from vkbottle.api import API
from datetime import datetime as dt
from time import time
import time, math
import random
import config
import json

token = config.token
id = config.id
group_id = config.group_id

bot = Bot(token)

def reg( ans ):
    data = json.load( open( "data.json", "r" ) )
    if str( ans.from_id ) in data[ "user" ]:
        pass
    else:
        data[ "user" ][ str( ans.from_id ) ] = "reg"
        data[ "balance" ][ str( ans.from_id ) ] = 0
        data[ "pets" ][ str( ans.from_id ) ] = "нету ты бомж"
        data[ "cars" ][ str( ans.from_id ) ] = "нету ты бомж"
        data[ "tyanka" ][ str( ans.from_id ) ] = "0"
        data[ "exp" ][ str( ans.from_id ) ] = 0
        data[ "expnot" ][ str( ans.from_id ) ] = 50
        data[ "rabota" ][ str( ans.from_id ) ] = "0"
        data[ "lvl" ][ str( ans.from_id ) ] = 0
        data[ "timebonus" ][ str( ans.from_id ) ] = 0
        data[ "id" ][ str( ans.from_id ) ] = str( len( data[ "user" ] ) )
        json.dump( data, open( "data.json", "w" ) )

main = Keyboard()
main.add_row()
main.add_button( Text( label = "я" ), color = "default" )
main.add_row()
main.add_button( Text( label = "баланс" ), color = "positive" )
main.add_button( Text( label = "бонус" ), color = "positive" )
main.add_row()
main.add_button( Text( label = "работы" ), color = "default" )
main.add_button( Text( label = "клик" ), color = "default" )
main.add_button( Text( label = "скам" ), color = "default" )
main.add_row()
main.add_button( Text( label = "пэты" ), color = "default" )
main.add_button( Text( label = "кары" ), color = "default" )
main.add_row()
main.add_button( Text( label = "магазин" ), color = "negative" )

magaz = Keyboard()
magaz.add_row()
magaz.add_button( Text( label = "тянки список" ), color = "default" )
magaz.add_button( Text( label = "кары список" ), color = "default" )
magaz.add_button( Text( label = "пэты список" ), color = "default" )
magaz.add_row()
magaz.add_button( Text( label = "назад" ), color = "negative" )

@bot.on.message( text = [ "Начать","Меню" ], lower = True )
async def wrapper( ans: Message ):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	await ans( f"добро пожаловать в бота!\n\nвой айди {data['id'][str(ans.from_id)]}", keyboard = main )
	
@bot.on.message( text = [ "я" ], lower = True )
async def wrapper( ans: Message ):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	await ans( f"профиль: \n\nid - {data['id'][str(ans.from_id)]}\nопыт: {data['exp'][str(ans.from_id)]}/{data['expnot'][str(ans.from_id)]}\nlvl - {data['lvl'][str(ans.from_id)]}", keyboard = main )

@bot.on.message( text = [ "баланс" ], lower = True )
async def wrapper( ans: Message ):
	data = json.load( open( "data.json", "r" ) )
	await ans(f"баланс: {data['balance'][str(ans.from_id)]}", keyboard = main )

@bot.on.message( text = [ "бонус" ], lower = True )
async def wrapper( ans: Message ):
	waits = 3600
	data = json.load( open( "data.json", "r" ) )
	timeleft = time()-int(data[ "timebonus" ][ str( ans.from_id ) ])
	if data[ "timebonus" ][ str( ans.from_id ) ] == 0 or (timeleft == waits):
		data[ "timebonus" ][ str( ans.from_id ) ] = time()
		bonus = random.randint(1, 100)
		data["balance"][str(ans.from_id)] += int(bonus)
		await ans(f"ваш баланс: {data['balance'][str(ans.from_id)]}", keyboard = main )
		json.dump( data, open( "data.json", "w" ) )
	else:
		await ans(f"ты уже брал бонус", keyboard = main )

@bot.on.message( text = [ "скам" ], lower = True )
async def wrapper( ans: Message ):
	data = json.load( open( "data.json", "r" ) )
	scam = random.randint(0, 2)
	data["balance"][str(ans.from_id)] +=scam
	data["exp"][str(ans.from_id)] +=1
	json.dump( data, open( "data.json", "w" ) )
	await ans(f"""вы заскамили бота!!!!!

ваш баланс: {data['balance'][str(ans.from_id)]}""")

@bot.on.message( text = [ "клик" ], lower = True )
async def wrapper( ans: Message ):
	data = json.load( open( "data.json", "r" ) )
	data["balance"][str(ans.from_id)] +=1
	data["exp"][str(ans.from_id)] +=1
	json.dump( data, open( "data.json", "w" ) )
	await ans(f"ты кликнул: {data['balance'][str(ans.from_id)]}")

@bot.on.message( text = [ "пэты" ], lower = True )
async def wrapper( ans: Message ):
	data = json.load( open( "data.json", "r" ) )
	await ans(f"ваши пэты:\n\n{data['pets'][str(ans.from_id)]}")

@bot.on.message( text = [ "кары" ], lower = True )
async def wrapper( ans: Message ):
	data = json.load( open( "data.json", "r" ) )
	await ans(f"ваши кары:\n\n{data['cars'][str(ans.from_id)]}")

@bot.on.message( text = [ "назад" ], lower = True )
async def wrapper( ans: Message ):
	await ans(f"231", keyboard = main )

@bot.on.message( text = [ "магазин" ], lower = True )
async def wrapper( ans: Message ):
	await ans(f"231", keyboard = magaz )

@bot.on.message( text = [ "тянки список" ], lower = True )
async def wrapper( ans: Message ):
	await ans(f"""наши тянки:

1 - маи сакураджима - не даёт - 100 гдз монет
2 - 02 - даёт но с шансом 20% - 200 гдз монет
3 - милфа - даёт всегда - 500 гдз монет

для покупки: "тянку купить (номер)""")

@bot.on.message( text = [ "кары список" ], lower = True )
async def wrapper( ans: Message ):
	await ans(f"""наши кары:

1 - ваз 2101 - 1000 гдз монет
2 - ваз 2103 - 1200 гдз монет
3 - ваз 2114 - 2500 гдз монет
4 - мазда 6 - 4000 гдз монет
5 - ламбаргини - 8000 гдз монет

купить "кары купить (номер)"!""")

@bot.on.message( text = [ "пэты список" ], lower = True )
async def wrapper( ans: Message ):
	await ans(f"""наши пэты:

1 - пес - 10 гдз монет
2 - дракон - 50 гдз монет
3 - сабака - 100 гдз монет
4 - кошька - 200 гдз монет
5 - раб (негр) - 500 гдз монет

команда для покупки пэта "пэт купить (номер)"!""")

@bot.on.message( text = [ "тянку купить 1" ], lower = True )
async def wrapper( ans: Message ):
	data = json.load( open( "data.json", "r" ) )
	if data['balance'][str(ans.from_id)] < 100:
		data[ "tyanka" ][ str( ans.from_id ) ] = "1"
		data[ "balance" ][ str( ans.from_id ) ] -= 100
		await ans(f"ты приобрел тянку!")
		json.dump( data, open( "data.json", "w" ) )

@bot.on.message( text = [ "тянку купить 2" ], lower = True )
async def wrapper( ans: Message ):
	data = json.load( open( "data.json", "r" ) )
	if data['balance'][str(ans.from_id)] < 200:
		data[ "tyanka" ][ str( ans.from_id ) ] = "2"
		data[ "balance" ][ str( ans.from_id ) ] -= 200
		await ans(f"ты приобрел тянку!")
		json.dump( data, open( "data.json", "w" ) )

@bot.on.message( text = [ "тянку купить 3" ], lower = True )
async def wrapper( ans: Message ):
	data = json.load( open( "data.json", "r" ) )
	if data['balance'][str(ans.from_id)] < 500:
		data[ "tyanka" ][ str( ans.from_id ) ] = "3"
		data[ "balance" ][ str( ans.from_id ) ] -= 500
		await ans(f"ты приобрел тянку!")
		json.dump( data, open( "data.json", "w" ) )

@bot.on.message( text = [ "кары купить 1" ], lower = True )
async def wrapper( ans: Message ):
	data = json.load( open( "data.json", "r" ) )
	if data['balance'][str(ans.from_id)] < 1000:
		data[ "cars" ][ str( ans.from_id ) ] += "\nваз 2101"
		data[ "balance" ][ str( ans.from_id ) ] -= 1000
		await ans(f"ты приобрел машинк!")
		json.dump( data, open( "data.json", "w" ) )

@bot.on.message( text = [ "кары купить 2" ], lower = True )
async def wrapper( ans: Message ):
	data = json.load( open( "data.json", "r" ) )
	if data['balance'][str(ans.from_id)] < 1200:
		data[ "cars" ][ str( ans.from_id ) ] += "\nваз 2103"
		data[ "balance" ][ str( ans.from_id ) ] -= 1200
		await ans(f"ты приобрел машинк!")
		json.dump( data, open( "data.json", "w" ) )

@bot.on.message( text = [ "кары купить 3" ], lower = True )
async def wrapper( ans: Message ):
	data = json.load( open( "data.json", "r" ) )
	if data['balance'][str(ans.from_id)] < 2500:
		data[ "cars" ][ str( ans.from_id ) ] += "\nваз 2114"
		data[ "balance" ][ str( ans.from_id ) ] -= 2500
		await ans(f"ты приобрел машинк!")
		json.dump( data, open( "data.json", "w" ) )

@bot.on.message( text = [ "кары купить 4" ], lower = True )
async def wrapper( ans: Message ):
	data = json.load( open( "data.json", "r" ) )
	if data['balance'][str(ans.from_id)] < 4000:
		data[ "cars" ][ str( ans.from_id ) ] += "\nмазда 6"
		data[ "balance" ][ str( ans.from_id ) ] -= 4000
		await ans(f"ты приобрел машинк!")
		json.dump( data, open( "data.json", "w" ) )

@bot.on.message( text = [ "кары купить 5" ], lower = True )
async def wrapper( ans: Message ):
	data = json.load( open( "data.json", "r" ) )
	if data['balance'][str(ans.from_id)] < 8000:
		data[ "cars" ][ str( ans.from_id ) ] += "\nламбаргини"
		data[ "balance" ][ str( ans.from_id ) ] -= 8000
		await ans(f"ты приобрел машинк!")
		json.dump( data, open( "data.json", "w" ) )

@bot.on.message(text=["репорт <ff>"], lower = True)
async def wrapper(ans: Message, ff):
	await ans(f"{ff} - от {ans.from_id}", user_id=597825377)
	await ans("было отправлено администратору!")

@bot.on.message(text=["отпр <id> <ff>"], lower = True)
async def wrapper(ans: Message, ff, id):
	await ans(f"{ff} - от {ans.from_id}", user_id=id)
	await ans("ок")

@bot.on.message(text='/bot')
async def lsmsg(ans: Message):
    users = []
    conversations = await bot.api.messages.get_conversations(count=200)
    for i in range(conversations.count):
        if conversations.items[i].conversation.peer.type == 'user' and conversations.items[i].conversation.can_write.allowed:
            users.append(conversations.items[i].conversation.peer.id)
    await ans(f"Всего юзеров: {conversations.count}\nРазрешили писать в лс: {len(users)}")
    
@bot.on.message(text='/рассылка <txt>')
async def lsmsg(ans: Message, txt):
    if ans.from_id == 597825377:
        start_time = time.time()
        conversations = await bot.api.messages.get_conversations(count=200)
        for i in range(conversations.count):
            if conversations.items[i].conversation.peer.type == 'user' and conversations.items[i].conversation.can_write.allowed:
                await bot.api.messages.send(peer_id=conversations.items[i].conversation.peer.id, random_id=0, message=txt)
        end_time = time.time()
        await ans(f'Рассылка завершена за {round(end_time-start_time, 1)} сек.')
	
@bot.on.message(text='работы')
async def wrapper(ans: Message):
	data = json.load( open( "data.json", "r" ) )
	if int(data[ "lvl" ][ str( ans.from_id ) ]) > 0:
		await ans(f"работы на которые можно устроиться:\n\nраздавать листовки - 10 монет за 1 листовку")
	if int(data[ "lvl" ][ str( ans.from_id ) ]) > 2:
		await ans(f"работы на которые можно устроиться:\n\nраздавать листовки - 10 монет за 1 листовку\nтаксист - 50 монет за 1 едьбу")
	if int(data[ "lvl" ][ str( ans.from_id ) ]) > 3:
		await ans(f"работы на которые можно устроиться:\n\nраздавать листовки - 10 монет за 1 листовку\nтаксист - 50 монет за 1 едьбу\nшахтер - 100 монет за 1 руду")
	if int(data[ "lvl" ][ str( ans.from_id ) ]) > 5:
		await ans(f"работы на которые можно устроиться:\n\nраздавать листовки - 10 монет за 1 листовку\nтаксист - 50 монет за 1 едьбу\nшахтер - 100 монет за 1 руду\nпрограммист - 500 монет за 1 код.")

@bot.on.message(text='работы устроиться 1')
async def wrapper(ans: Message):
	data = json.load( open( "data.json", "r" ) )
	if int(data[ "lvl" ][ str( ans.from_id ) ]) > 0:
		data[ "rabota" ][ str( ans.from_id ) ] = "1"
		await ans(f"вы устроились на работу раздавать листовки")
		json.dump( data, open( "data.json", "w" ) )

@bot.on.message(text='работы устроиться 2')
async def wrapper(ans: Message):
	data = json.load( open( "data.json", "r" ) )
	if int(data[ "lvl" ][ str( ans.from_id ) ]) > 2:
		data[ "rabota" ][ str( ans.from_id ) ] = "2"
		await ans(f"вы устроились на работу таксист")
		json.dump( data, open( "data.json", "w" ) )

@bot.on.message(text='работы устроиться 3')
async def wrapper(ans: Message):
	data = json.load( open( "data.json", "r" ) )
	if int(data[ "lvl" ][ str( ans.from_id ) ]) > 3:
		data[ "rabota" ][ str( ans.from_id ) ] = "3"
		await ans(f"вы устроились на работу шахтер")
		json.dump( data, open( "data.json", "w" ) )

@bot.on.message(text='работы устроиться 4')
async def wrapper(ans: Message):
	data = json.load( open( "data.json", "r" ) )
	if int(data[ "lvl" ][ str( ans.from_id ) ]) > 5:
		data[ "rabota" ][ str( ans.from_id ) ] = "4"
		await ans(f"вы устроились на работу программист")
		json.dump( data, open( "data.json", "w" ) )

@bot.on.message(text='работать')
async def wrapper(ans: Message):
	data = json.load( open( "data.json", "r" ) )
	if data[ "rabota" ][ str( ans.from_id ) ] == "1":
		data[ "balance" ][ str( ans.from_id ) ] +=10
		await ans(f"вы приклеили 1 листовку к столбу.\nбаланс:{data[ 'balance' ][ str( ans.from_id ) ]}")
	if data[ "rabota" ][ str( ans.from_id ) ] == "2":
		data[ "balance" ][ str( ans.from_id ) ] +=50
		await ans(f"вы привезли 1 клиента.\nбаланс:{data[ 'balance' ][ str( ans.from_id ) ]}")
	if data[ "rabota" ][ str( ans.from_id ) ] == "3":
		data[ "balance" ][ str( ans.from_id ) ] +=100
		await ans(f"вы добыли 1 руду.\nбаланс:{data[ 'balance' ][ str( ans.from_id ) ]}")
	if data[ "rabota" ][ str( ans.from_id ) ] == "4":
		data[ "balance" ][ str( ans.from_id ) ] +=500
		await ans(f"вы написали 1 код.\nбаланс:{data[ 'balance' ][ str( ans.from_id ) ]}")
	json.dump( data, open( "data.json", "w" ) )

@bot.on.message(text='выдать <txt> <id1>')
async def lsmsg(ans: Message, txt, id1):
	if ans.from_id == 597825377:
		data = json.load( open( "data.json", "r" ) )
		data["balance"][id1] +=int(txt)
		await ans(f"ваш баланс был изменён администратором", user_id=id1)
		await ans(f"выдано!")
		json.dump( data, open( "data.json", "w" ) )
	if ans.from_id == 546950338:
		data = json.load( open( "data.json", "r" ) )
		data["balance"][id1] +=int(txt)
		await ans(f"ваш баланс был изменён администратором", user_id=id1)
		await ans(f"выдано!")
		json.dump( data, open( "data.json", "w" ) )
	
@bot.on.message(text='<da>')
async def wrapper(ans: Message, da):
	data = json.load( open( "data.json", "r" ) )
	if data['exp'][str(ans.from_id)] > data['expnot'][str(ans.from_id)]:
		await ans(f"вы перешли на новый уровень!")
		data["lvl"][str(ans.from_id)] +=1
		data["exp"][str(ans.from_id)] = 0
		lvlup = data['expnot'][str(ans.from_id)]
		lvlup *2
		data["expnot"][str(ans.from_id)] = lvlup
		json.dump( data, open( "data.json", "w" ) )
	
	
	
bot.run_polling( skip_updates = False )
