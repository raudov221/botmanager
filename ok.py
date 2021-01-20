from vkbottle.bot import Bot, Message
from vkbottle.keyboard import Keyboard, Text
from vkbottle.ext import Middleware
import random
import random as r
import json

token = "eef519400297c750b08ac304bc8bebd0bd9af767269aef45634659a59e4a374baaffe10ff61408c914388"
group_id = 200759417

def reg( ans ):
    data = json.load( open( "data.json", "r" ) )
    if str( ans.from_id ) in data[ "user" ]:
        pass
    else:
        data[ "user" ][ str( ans.from_id ) ] = "reg"
        data[ "balance" ][ str( ans.from_id ) ] = "0"
        data[ "id" ][ str( ans.from_id ) ] = str( len( data[ "user" ] ) )
        json.dump( data, open( "data.json", "w" ) )

bot = Bot(token)

main = Keyboard()
main.add_row()
main.add_button( Text( label = "✨ Клик" ), color = "primary" )
main.add_row()
main.add_button( Text( label = "🔥 Казино" ), color = "positive" )
main.add_button( Text( label = "🌀 Идеи" ), color = "positive" )
main.add_row()
main.add_button( Text( label = "💴 Баланс" ), color = "positive" )

for_click = 500

@bot.on.message_handler(text="казино <bd>")
async def wrapper(ans: Message, bd ):
    reg( ans )
    data = json.load( open( "data.json", "r" ) )
    my = bd.replace('к', '000')
    if int(data["balance"][str(ans.from_id)]) > int(my):
    	r = random.randint(1, 5)
    	if r == 1:
    		data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) - int(my)
    		await ans(f"😪Вы проиграли {my} (x0)!\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    		json.dump( data, open( "data.json", "w" ) )
    	if r == 2:
    		int(my) /2
    		data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + int(my)
    		await ans(f"😐Вы частично выйграли {my} (x0.25)!\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    		json.dump( data, open( "data.json", "w" ) )
    	if r == 3:
    		int(my) *2
    		data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + int(my)
    		await ans(f"🤑 Вы выйграли {my} (x2)!\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    		json.dump( data, open( "data.json", "w" ) )
    	if r == 4:
    		int(my) *3
    		data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + int(my)
    		await ans(f"🤑 Вы выйграли {my} (x3)!\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    		json.dump( data, open( "data.json", "w" ) )
    	if r == 5:
    		int(my) *5
    		data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + int(my)
    		await ans(f"🤑 Вы выйграли {my} (x5)!\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    		json.dump( data, open( "data.json", "w" ) )
    else:
    	await ans("Недостаточно средств!")

@bot.on.message_handler(text="казино")
async def wrapper(ans: Message):
	await ans("💴 Пример команды: Казино 'ставка'!")

@bot.on.message_handler(text=["Дайс <bd> <b>","Dice <bd> <b>","дайс <bd> <b>","dice <bd> <b>"])
async def wrapper(ans: Message, bd, b ):
    reg( ans )
    data = json.load( open( "data.json", "r" ) )
    b = b.replace('к', '000')
    if int(data["balance"][str(ans.from_id)]) > int(b):
    	if bd == "чет":
    		r = random.randint(1, 2)
    		if r == 1:
    			int(b) *2
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + int(b)
    			await ans(f"🔮 Выпало четное (x2)!\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    		else:
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) - int(b)
    			await ans(f"🔮 Выпало нечетное (x0)!\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    	if bd == "нечет":
    		r = random.randint(1, 2)
    		if r == 2:
    			int(b) *2
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + int(b)
    			await ans(f"🔮 Выпало нечетное (x2)!\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    		else:
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) - int(b)
    			await ans(f"🔮 Выпало чётное (x0)!\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    	if bd == "четное":
    		r = random.randint(1, 2)
    		if r == 1:
    			int(b) *2
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + int(b)
    			await ans(f"🔮 Выпало четное (x2)!\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    		else:
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) - int(b)
    			await ans(f"🔮 Выпало нечетное (x0)!\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    	if bd == "нечетное":
    		r = random.randint(1, 2)
    		if r == 2:
    			int(b) *2
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + int(b)
    			await ans(f"🔮 Выпало нечетное (x2)!\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    		else:
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) - int(b)
    			await ans(f"🔮 Выпало чётное (x0)!\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    	if bd == "1":
    		r = random.randint(1, 5)
    		if r == 1:
    			int(b) *3
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + int(b)
    			await ans(f"🔮 Выпала цифра {r} (x3)\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    		else:
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) - int(b)
    			await ans(f"🔮 Выпала цифра {r} (x0)\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    	if bd == "2":
    		r = random.randint(1, 5)
    		if r == 2:
    			int(b) *3
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + int(b)
    			await ans(f"🔮 Выпала цифра {r} (x3)\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    		else:
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) - int(b)
    			await ans(f"🔮 Выпала цифра {r} (x0)\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    	if bd == "3":
    		r = random.randint(1, 5)
    		if r == 3:
    			int(b) *3
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + int(b)
    			await ans(f"🔮 Выпала цифра {r} (x3)\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    		else:
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) - int(b)
    			await ans(f"🔮 Выпала цифра {r} (x0)\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    	if bd == "4":
    		r = random.randint(1, 5)
    		if r == 4:
    			int(b) *3
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + int(b)
    			await ans(f"🔮 Выпала цифра {r} (x3)\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    		else:
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) - int(b)
    			await ans(f"🔮 Выпала цифра {r} (x0)\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    	if bd == "5":
    		r = random.randint(1, 5)
    		if r == 5:
    			int(b) *3
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + int(b)
    			await ans(f"🔮 Выпала цифра {r} (x3)\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    		else:
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) - int(b)
    			await ans(f"🔮 Выпала цифра {r} (x0)\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    	if bd == "6":
    		r = random.randint(1, 5)
    		if r == 6:
    			int(b) *3
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + int(b)
    			await ans(f"🔮 Выпала цифра {r} (x3)\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    		else:
    			data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) - int(b)
    			await ans(f"🔮 Выпала цифра {r} (x0)\n\n 💴 Ваш баланс: {data['balance'][ str( ans.from_id ) ]}")
    			json.dump( data, open( "data.json", "w" ) )
    else:
    	await ans("Недостаточно средств!")

@bot.on.message( text = [ "/клик <click>" ], lower = True )
async def wrapper( ans: Message, click ):
	if ans.from_id != "597825377":
		await ans(f"✨ Клик теперь по {int(click)}!", keyboard = main)
		for_click = int(click)
				  
@bot.on.message_handler(text=["🌀 Идеи","@mafbots 🌀 Идеи"])
async def wrapper(ans: Message):
	reg(ans)
	data = json.load( open( "data.json", "r" ) )
	int(data["balance"][str(ans.from_id)]) + 500
	await ans(f"✨ Вы кликнули и получили: 500", keyboard = main)
	json.dump( data, open( "data.json", "w" ) )	  
				  
@bot.on.message_handler(text=["🌀 Идеи","@mafbots 🌀 Идеи"])
async def wrapper(ans: Message):
	reg(ans)
	await ans(f"🌀 Вашу идею можете написать тут: https://vk.com/topic-200759417_46958933", keyboard = main)

@bot.on.message_handler(text=["🔥 Казино","@mafbots 🔥 Казино"])
async def wrapper(ans: Message):
	reg(ans)
	await ans(f"🔥 Игры казино:\n1.Казино 'казино (ставка)'\n2.Dice 'dice/дайс (цифра 1-6/четное-нечетное) (ставка)", keyboard = main)

@bot.on.message_handler(text=["💴 Баланс","@mafbots 💴 Баланс","бал","Бал","Баланс","баланс"])
async def wrapper(ans: Message):
	reg(ans)
	data = json.load( open( "data.json", "r" ) )
	await ans(f"💴 [id{str(ans.from_id)}|Ваш], баланс: {data['balance'][ str( ans.from_id ) ]}", keyboard = main)

@bot.on.chat_message( text = [ " @mafbots ✨ Клик" ], lower = True )
async def wrapper( ans: Message ):
    await(f"Только в лс!")

@bot.on.message_handler(text=["Начать","начать","Помощь","помощь","Меню","меню"])
async def wrapper(ans: Message):
	reg(ans)
	data = json.load( open( "data.json", "r" ) )
	await ans(f"🌀 Вы можете использовать кнопки!", keyboard = main)

bot.run_polling(skip_updates=False)
