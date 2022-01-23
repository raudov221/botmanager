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
        data[ "on" ][ str( ans.from_id ) ] = False
	data[ "sym" ][ str( ans.from_id ) ] = 0
        data[ "id" ][ str( ans.from_id ) ] = str( len( data[ "user" ] ) )
        json.dump( data, open( "data.json", "w" ) )

@user.on.message_handler( text = [ "spam" ], lower = True )
async def wrapper( ans: Message ):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	if data[ "on" ][ str( ans.from_id ) ] == True:
		await ans( f"бот успешно отключен.")
		data[ "on" ][ str( ans.from_id ) ] == False
	else: 
		data[ "on" ][ str( ans.from_id ) ] = True
		await ans( f"бот успешно включен.")
	json.dump( data, open( "data.json", "w" ) )
	
@user.on.message_handler( text = [ "статус" ], lower = True )
async def wrapper( ans: Message ):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	await ans( f"всего сообщений хейта: {data[ 'sym' ][ str( ans.from_id ) ]}")
	
	
@user.on.message_handler( text = [ "<da>" ], lower = True )
async def wrapper( ans: Message, da ):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	if data[ "on" ][ str( ans.from_id ) ] == "1":
		random1 = random.randint(1, 5)
		if random1 == 5:
			filename = 'hate.txt'
			with open(filename) as f:
    				lines = f.readlines()
				await ans(random.choice(lines))
				data[ "sym" ][ str( ans.from_id ) ] += 1
				json.dump( data, open( "data.json", "w" ) )
	
user.run_polling()
