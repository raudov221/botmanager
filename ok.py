from vkbottle.bot import Bot, Message
from vkbottle import vkscript
from vkbottle.keyboard import Keyboard, Text
from googlesearch import search
import random
import random as r
import json
import math

token = "bfd9b4ba0ec9739a49f46081f98b59751ba31766914b3245d524d6be68d13ad575fdb9a9d778303dae035"
group_id = 201150448

bot = Bot(token)

def reg( ans ):
    data = json.load( open( "data.json", "r" ) )
    if str( ans.from_id ) in data[ "user" ]:
        pass
    else:
        data[ "user" ][ str( ans.from_id ) ] = "reg"
        data[ "balance" ][ str( ans.from_id ) ] = "0"
        data[ "replenish" ][ str( ans.from_id ) ] = "0"
        data[ "received" ][ str( ans.from_id ) ] = "0"
        data[ "admin" ][ str( ans.from_id ) ] = "0"
        data[ "pred" ][ str( ans.from_id ) ] = "0"
        data[ "id" ][ str( ans.from_id ) ] = str( len( data[ "user" ] ) )
        json.dump( data, open( "data.json", "w" ) )

@bot.on.chat_message(text=["Помощь"])
async def wrapper(ans: Message):
    data = json.load( open( "data.json", "r" ) )
    await ans(f'🤩 Мои команды: \nДля игроков и админов: \n 1.!скажи <ваша фраза>\n 2.!выбери <ваш текст без пробелов> <второй текст без пробелов> \n 3.Клик \n 4.Баланс \n5.!регистрация \n\n😎 Для админов: Кик <причина>')
    reg( ans )

@bot.on.chat_message(text=["!скажи <you>"])
async def wrapper(ans: Message, you):
    reg( ans )
    await ans(f'Меня попросили сказать: {you}')
    await bot.api.messages.send(peer_id = ans.peer_id, random_id = 0, sticker_id = 51564)

@bot.on.chat_message(text=["!регистрация"])
async def wrapper(ans: Message):
    data = json.load( open( "data.json", "r" ) )
    await ans(f'Вы успешно зарегистрировались!')
    reg( ans )

@bot.on.chat_message( text = [ "💰 Баланс","Баланс", "бал" ], lower = True )
async def wrapper( ans: Message ):
    data = json.load( open( "data.json", "r" ) )
    reg( ans )
    await ans( f"💸 Ваш баланс - {data[ 'balance' ][ str( ans.from_id ) ]}" )

@bot.on.chat_message( text = [ "казино" ], lower = True )
async def wrapper( ans: Message ):
    data = json.load( open( "data.json", "r" ) )
    reg( ans )
    await ans( f"⛔ Недопустимый формат! <казино (ставка)>" )

@bot.on.chat_message( text = [ "казино <sum>" ], lower = True )
async def wrapper( ans: Message, sum ):
    data = json.load( open( "data.json", "r" ) )
    json.dump( data, open( "data.json", "w" ) )
    reg( ans )
    if int( int( data[ "balance" ][ str( ans.from_id ) ] ) < sum ):
        await ans( f"⛔ Недостаточно средств!" )

@bot.on.chat_message(text=["!клик"])
async def wrapper(ans: Message):
    data = json.load( open( "data.json", "r" ) )
    reg( ans )
    data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + int( data[ "for_click" ] )
    await ans(f'Вы кликнули!')

@bot.on.chat_message(text=["!выбери <sum> или <sim>"])
async def wrapper(ans: Message, sum, sim):
    reg( ans )
    await ans(f'Я выбрал: {random.choice([sum, sim])}')

@bot.on.chat_message(text=["@all", "*all" "@all," "*all,"])
async def wrapper(ans: Message):
    reg( ans )
    ban = ans.from_id
    await ans(f"Тебя исключили по причине: all")
    await bot.api.messages.remove_chat_user(
        chat_id=ans.peer_id - 2000000000, member_id=ban
    )


@bot.on.chat_message(text=["!кик <da>", "кик <da>"])
async def wrapper(ans: Message, da):
    reg( ans )
    user = ans.reply_message.from_id
    members = await bot.api.messages.getConversationMembers(peer_id=ans.peer_id, fields="users")
    users = members['items']
    if data[ "admin" ][ str( ans.from_id ) ] == "0":
        await ans('Вы не можете исключить участника т.к. не являетесь администратором беседы')
    else:
        await ans(f"Тебя исключили")
        await bot.api.messages.remove_chat_user(
            chat_id=ans.peer_id - 2000000000, member_id=user
        )
              
@bot.on.chat_message(text=["!найти <da>", "найти <da>", "Найти {da}", "!Найти {da}"])
async def wrapper(ans: Message, da):
    reg( ans )
    for url in search(f'"{da}" {da}', stop=3):
        await ans(f"Я нашел: {url}")

@vkscript
def my_execute(api, user_ids=()):
    message_ids = []
    for user_id in user_ids:
        user = api.users.get(user_ids=user_id)[0]
        message_ids.append(api.messages.send(message=f"{user.first_name}, спасибо что зашел на чай", random_id=0, peer_id=user_id))
    return message_ids
              
@bot.on.chat_message(text=["стаканчик <sum> <stak>"])
async def wrapper(ans: Message, sum, stak):
    reg( ans )
    data = json.load( open( "data.json", "r" ) )
    if int(data["balance"][str(ans.from_id)]) > str(sum):
        await ans(f'бабла нет')
    else:
        if int(stak) > 5:
            await ans('ты стаканчик больше 5 написал слепой')
        else:
            random.choice(1,5) 
            if int(stak) == random.choice:
                await ans('ема ты молодец выйграл')
                data[ "balance" ][ str( ans.from_id ) ] = int( data[ "balance" ][ str( ans.from_id ) ] ) + str(sum)
            else:
                await ans('ты проиграл удача не на твоей стороне.') 
                data["balance"][str(ans.from_id)] = int(data["balance"][str(ans.from_id) ]) - str(sum)

bot.run_polling( skip_updates = False )
await api.execute(code=my_execute(user_ids=[10, 11, 12]))
