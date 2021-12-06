from vkbottle.user import User, Message
from vkbottle.api import API
from rextester_py import rexec_aio
import math
import random

user = User("279db29b3e03042c043dd724d7e876ee98744aea1c4268aa701a1b0f382a605c1f0da8b75b583d693e8b1")
api = API("279db29b3e03042c043dd724d7e876ee98744aea1c4268aa701a1b0f382a605c1f0da8b75b583d693e8b1")


user.run_polling()

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

@bot.on.message( text = [ "ку","привет" ], lower = True )
async def wrapper( ans: Message ):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	await ans( f"здарова!\n\nтвой айди {data['id'][str(ans.from_id)]}")

@bot.on.message( text = [ "я" ], lower = True )
async def wrapper( ans: Message ):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	await ans( f"профиль: \n\nid - {data['id'][str(ans.from_id)]}\nопыт: {data['exp'][str(ans.from_id)]}/{data['expnot'][str(ans.from_id)]}\nlvl - {data['lvl'][str(ans.from_id)]}", keyboard = main )

@bot.on.message( text = [ "баланс" ], lower = True )
async def wrapper( ans: Message ):
	data = json.load( open( "data.json", "r" ) )
	await ans(f"баланс: {data['balance'][str(ans.from_id)]}", keyboard = main )


user.run_polling()
