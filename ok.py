from vkbottle.bot import Bot, Message
from vkbottle import vkscript
from vkbottle.keyboard import Keyboard, Text
from googlesearch import search
import random
import random as r
import json
import math

token = "1ae80fd1fc2e59106902a96597761f4802b05b1787c147dbafef93e57b76447f8ea735c2af528562616d0"
group_id = 200759417

bot = Bot(token)
addd = 0

def reg( ans ):
    data = json.load( open( "data.json", "r" ) )
    if str( ans.from_id ) in data[ "user" ]:
        pass
    else:
        data[ "user" ][ str( ans.from_id ) ] = "reg"
        data[ "reg" ][ str( ans.from_id ) ] = "0"
        data[ "admin" ][ str( ans.from_id ) ] = "0"
        data[ "pred" ][ str( ans.from_id ) ] = "0"
        data[ "id" ][ str( ans.from_id ) ] = str( len( data[ "user" ] ) )
        json.dump( data, open( "data.json", "w" ) )

@bot.on.chat_message(text=["Помощь"])
async def wrapper(ans: Message):
    data = json.load( open( "data.json", "r" ) )
    await ans(f'🤩 Мои команды: \nДля игроков и админов: \n 1.!скажи <ваша фраза>\n 2.!выбери <ваш текст без пробелов> <второй текст без пробелов> \n 3.Клик \n 4.Баланс \n5.!регистрация \n\n😎 Для админов: Кик <причина>')
    reg( ans )

bot.on.chat_message(text=["<da>"])
async def wrapper(ans: Message, da):
    user = ans.from_id
    data = json.load( open( "data.json", "r" ) )
    if data['reg'][str(ans.from_id)] == "0":
        await ans(f"[id{str(ans.from_id)}|Пользователь], вы успешно зарегистрировались!")
        reg( ans )
        data['reg'][str(ans.from_id)] = "0"
    else:
        pass

bot.run_polling( skip_updates = False )
