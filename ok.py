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

@user.on.message_handler( text = [ "spam" ], lower = True )
async def wrapper( ans: Message ):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	if data[ "pets" ][ str( ans.from_id ) ] == "1":
		await ans( f"hash303191")
		data[ "pets" ][ str( ans.from_id ) ] == "0"
	else: 
		data[ "pets" ][ str( ans.from_id ) ] = "1"
		await ans( f"spam = 1")
	json.dump( data, open( "data.json", "w" ) )
	
	
@user.on.message_handler( text = [ "<da>" ], lower = True )
async def wrapper( ans: Message, da ):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	if data[ "pets" ][ str( ans.from_id ) ] == "1":
		random1 = random.randint(1, 5)
		if random1 == 5:
			filename = 'hate.txt'
			with open(filename) as f:
    				lines = f.readlines()
				await ans(random.choice(lines))
	
user.run_polling()
