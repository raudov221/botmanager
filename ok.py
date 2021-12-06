from vkbottle.user import User, Message
from vkbottle.api import API
from rextester_py import rexec_aio
import math
import random

user = User("414b2b764ad3162d3757c1acc2c7b732eb0f5093846364626111956249eec8a80281c837764c183b0251d")
api = API("414b2b764ad3162d3757c1acc2c7b732eb0f5093846364626111956249eec8a80281c837764c183b0251d")


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
