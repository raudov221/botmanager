from vkbottle.user import User, Message
from vkbottle.api import API
import json
import math
import random

user = User("79af1c575e6b2fc4242d50bd0fd78d286bab2da2711c2b619d4109a85e47c30540a7959f0944483da33b5")
api = API("79af1c575e6b2fc4242d50bd0fd78d286bab2da2711c2b619d4109a85e47c30540a7959f0944483da33b5")

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
        data[ "rabot" ][ str( ans.from_id ) ] = 0
        data[ "lvl" ][ str( ans.from_id ) ] = 0
        data[ "timebonus" ][ str( ans.from_id ) ] = 0
        data[ "id" ][ str( ans.from_id ) ] = str( len( data[ "user" ] ) )
        json.dump( data, open( "data.json", "w" ) )

@user.on.message_handler( text = [ "ку","привет" ], lower = True )
async def wrapper( ans: Message ):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	await ans( f"здарова!, {data[ 'pets' ][ str( ans.from_id ) ]},\n\nтвой айди {data['id'][str(ans.from_id)]}")

@user.on.message_handler( text = [ "я" ], lower = True )
async def wrapper( ans: Message ):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	await ans( f"{data[ 'pets' ][ str( ans.from_id ) ]}, профиль: \n\nid - {data['id'][str(ans.from_id)]}\nопыт: {data['exp'][str(ans.from_id)]}/{data['expnot'][str(ans.from_id)]}\nlvl - {data['lvl'][str(ans.from_id)]}\n\nстатус: {data[ 'cars' ][ str( ans.from_id ) ]}")

@user.on.message_handler( text = [ "баланс" ], lower = True )
async def wrapper( ans: Message ):
	data = json.load( open( "data.json", "r" ) )
	await ans(f"{data[ 'pets' ][ str( ans.from_id ) ]}, баланс: {data['balance'][str(ans.from_id)]}")

@user.on.message_handler( text = [ "скам" ], lower = True )
async def wrapper( ans: Message):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	a = random.randint(0, 5)
	data[ "balance" ][ str( ans.from_id ) ] += int(a)
	await ans(f"{data[ 'pets' ][ str( ans.from_id ) ]}, ты получить {a} монет. иди нахуй.")
	json.dump( data, open( "data.json", "w" ) )

@user.on.message_handler( text = [ "ник <bebra>" ], lower = True )
async def wrapper( ans: Message, bebra):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	data[ "pets" ][ str( ans.from_id ) ] = f"{bebra}"
	await ans(f"{data[ 'pets' ][ str( ans.from_id ) ]}, твой новый ник!!!11!1!")
	json.dump( data, open( "data.json", "w" ) )
	
@user.on.message_handler( text = [ "статус <bebra>" ], lower = True )
async def wrapper( ans: Message, bebra):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	data[ "cars" ][ str( ans.from_id ) ] = f"{bebra}"
	await ans(f"{data[ 'pets' ][ str( ans.from_id ) ]}, твой новый статус!!!11!1!")
	json.dump( data, open( "data.json", "w" ) )
	
@user.on.message_handler( text = [ "да" ], lower = True )
async def wrapper( ans: Message):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	await ans(f"{data[ 'pets' ][ str( ans.from_id ) ]}, пизда.")
	
@user.on.message_handler( text = [ "моя" ], lower = True )
async def wrapper( ans: Message):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	await ans(f"{data[ 'pets' ][ str( ans.from_id ) ]}, твоя.")
	
user.run_polling()
