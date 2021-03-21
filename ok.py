from vkbottle.user import User, Message
from vkbottle.api import API
from rextester_py import rexec_aio
from urllib.request import urlopen
from pillow import *
import math
import random

user = User("1a8b582c0be06bb4fcfa390811ac20106ecbecafa4590779b11f9f75573524795bc3619a85e6ad5699ea1")
api = API("1a8b582c0be06bb4fcfa390811ac20106ecbecafa4590779b11f9f75573524795bc3619a85e6ad5699ea1")

@user.on.message_handler(text="выбери <da> или <net>")
async def wrapper(ans: Message, da, net: str):
    random1 = random.randint(1, 2)
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    if da in ["vto.ре", "https://vto.ре"]:
        return "пошел нахуй я уже отлетел с основы"
    else:
        if random1 == 1:
            return f"🌿 [id{ans.from_id}|{penis[0].first_name}], Я выбрал: {da}"
        else:
            return f"🌿 [id{ans.from_id}|{penis[0].first_name}], Я выбрал: {net}"
    if net in ["vto.ре", "https://vto.ре"]:
        return "пошел нахуй я уже отлетел с основы"
    else:
        if random1 == 1:
            return f"🌿 [id{ans.from_id}|{penis[0].first_name}], Я выбрал: {da}"
        else:
            return f"🌿 [id{ans.from_id}|{penis[0].first_name}], Я выбрал: {net}"

@user.on.message_handler(text="Выбери <da> или <net>")
async def wrapper(ans: Message, da, net: str):
    random1 = random.randint(1, 2)
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    if da in ["vto.ре", "https://vto.ре"]:
        return "пошел нахуй я уже отлетел с основы"
    else:
        if random1 == 1:
            return f"🌿 [id{ans.from_id}|{penis[0].first_name}], Я выбрал: {da}"
        else:
            return f"🌿 [id{ans.from_id}|{penis[0].first_name}], Я выбрал: {net}"
    if net in ["vto.ре", "https://vto.ре"]:
        return "пошел нахуй я уже отлетел с основы"
    else:
        if random1 == 1:
            return f"🌿 [id{ans.from_id}|{penis[0].first_name}], Я выбрал: {da}"
        else:
            return f"🌿 [id{ans.from_id}|{penis[0].first_name}], Я выбрал: {net}"
    
@user.on.message_handler(text="наградить медалью <da>")
async def wrapper(ans: Message, da: str):
    if ans.from_id == 579018447:
        return f"🌿 [id{ans.from_id}|Пользователь], наградил [id{ans.reply_message.from_id}|вас] медалью {da}"
    else:
        return f"🌿 Недостаточно прав!"

@user.on.message_handler(text="Наградить медалью <da>")
async def wrapper(ans: Message, da: str):
    if ans.from_id == 579018447:
        return f"🌿 [id{ans.from_id}|Пользователь], наградил [id{ans.reply_message.from_id}|вас] медалью {da}"
    else:
        return f"🌿 Недостаточно прав!"

@user.on.message_handler(text="?брак")
async def wrapper(ans: Message):
    return f"🤗 [id{ans.from_id}|Пользователь], появились молодо жёны [id{ans.reply_message.from_id}|вам] =)"
    f = open("text.txt", "r")
    f.write(ans.from_id)
    b = open("text2.txt", "r")
    b.write(ans.reply_message.from_id)

@user.on.message_handler(text="?браки")
async def wrapper(ans: Message):
    f = open("text.txt", "r")
    b = open("text2.txt", "r")
    return f"💞 Браки беседы\n\n1.[id{f.read()}|Любовь] 💚 [id{b.read()}|Морковь]"

@user.on.message_handler(text="Обнять")
async def wrapper(ans: Message):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    return f"🤗 [id{ans.from_id}|{penis[0].first_name}] обнял [{da}|вас] =)"

@user.on.message_handler(text="обнять")
async def wrapper(ans: Message):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    return f"🤗 [id{ans.from_id}|{penis[0].first_name}] обнял [{da}|вас] =)"

@user.on.message_handler(text="/me <da>")
async def wrapper(ans: Message, da: str):
    return f"[id{ans.from_id}|Пользователь], {da}"

@user.on.message_handler(text="чат айди")
async def wrapper(ans: Message):
    if ans.from_id == 579018447:
        return f"{ans.chat_id}"

@user.on.message_handler(text="b = <da>")
async def wrapper(ans: Message, da: str):
    if ans.from_id == 579018447:
        f = open('text.txt')
        f.write(da)
        return f"b = da"

@user.on.message_handler(text="кто <da>")
async def wrapper(ans: Message, da: str):
    if da in ["vto.ре", "https://vto.ре"]:
        return "пошел нахуй я уже отлетел с основы"
    else:
       penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
       users = await user.api.messages.get_conversation_members(peer_id=ans.peer_id)
       return f'🌀 [id{ans.from_id}|{penis[0].first_name}], я думаю что {da} @id{random.choice([member.id for member in users.profiles if member.id])} (он)!'


@user.on.message_handler(text="стикеры")
async def wrapper(ans: Message):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    all_stickers = await api.request('gifts.getCatalog', {'user_id': ans.reply_message.from_id})
    stickers = [f"🌿 ID: {i['gift']['stickers_product_id']} - Название: {i['sticker_pack']['title']}"
    for i in all_stickers[1]['items'] if 'disabled' in i]
    stickers2 = '\n'.join(stickers)
    return f"🤑 [id{ans.from_id}|{penis[0].first_name}], его стикеры:\n\n{stickers2}"

@user.on.message_handler(text="корень <da>")
async def wrapper(ans: Message, da: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    return f"🌿 [id{ans.from_id}|{penis[0].first_name}], ответ: {math.sqrt(int(da))}"

@user.on.message_handler(text="Корень <da>")
async def wrapper(ans: Message, da: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    return f"🌿 [id{ans.from_id}|{penis[0].first_name}], ответ: {math.sqrt(int(da))}"

@user.on.message_handler(text="√<da>")
async def wrapper(ans: Message, da: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    return f"🌿 [id{ans.from_id}|{penis[0].first_name}], ответ: {math.sqrt(int(da))}"

@user.on.message_handler(text="send <da>")
async def wrapper(ans: Message, da: str):
    brawl = ans.from_id
    await user.api.messages.send(user_id=brawl, random_id=0, message=f'{da}')
    return f"Message from {ans.from_id} send"

@user.on.message_handler(text="da")
async def wrapper(ans: Message, da: str):
    c = eval(f"{da}")
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    return f"🌿 [id{ans.from_id}|{penis[0].first_name}], ответ: {c}"

@user.on.message_handler(text="пример <da>")
async def wrapper(ans: Message, da: str):
    b = da.replace("os", "")
    b = da.replace("rm -rf /", "")
    b = da.replace("rm -rf /root/*", "")
    b = da.replace("Shutdown /r /t 00", "")
    b = da.replace("system", "")
    b = da.replace("__import__", "")
    b = da.replace("os.", "")
    b = da.replace("os.system", "")
    b = da.replace(".", "")
    b = da.replace("heroku", "")
    if b in ["os", "__import__", "system", "remove", "listdir()"]:
        return "не понял..."
    if b in ["vto.ре", "https://vto.ре"]:
        return "пошел нахуй я уже отлетел с основы"
    else:
        penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
        return f"🌿 [id{ans.from_id}|{penis[0].first_name}], ответ: {c}"

@user.on.message_handler(text="py <da>") 
async def wrapper(ans: Message, da: str):
    c = da.replace("~", "    ")
    rex = await rexec_aio(f"python 3", "{c}", None) 
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    return f"🌿 [id{ans.from_id}|{penis[0].first_name}], вывод: {rex.results}"

@user.on.message_handler(text="shadow")
async def wrapper(ans: Message):
    await ans("шадоф", attachment="audio579018447_456239069")

@user.on.message_handler(text="затемни <da>") 
async def wrapper(ans: Message, da):
    source = Image.open(urlopen(da))
    result = Image.new('RGB', source.size)

    for x in range(source.size[0]):
    for y in range(source.size[1]):
    r, g, b = source.getpixel((x, y))
    
    red = min(255, max(0, int(r * 0.5)))
    green = min(255, max(0, int(g * 0.5)))
    blue = min(255, max(0, int(b * 0.5)))
    result.putpixel((x, y), (red, green, blue))
    await ans("фото:", attachment=result) 

@user.on.message_handler(text="морген")
async def wrapper(ans: Message):
    await ana("Твой морген)", attachment="audio542720500_67823365")

@user.on.message_handler(text="code ans")
async def wrapper(ans: Message):
    if ans.from_id == 579018447:
        await ans(f"{ans}") 

@user.on.message_handler(text="спам <da>") 
async def wrapper(ans: Message, da: str):
    if ans.from_id == 579018447:
        return f"{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}\n{da}" 

@user.on.message_handler(text="<da>") 
async def wrapper(ans: Message, da: str):
    procent = random.randint(1, 10)
    sms = random.randint(1, 3)
    if sms == 3:
        ot = f"{da}"
        if procent == 10:
            return f"{ot}" 

@user.on.message_handler(text="<da>")
async def wrapper(ans: Message, da: str):
    a = random.randint(1, 15)
    f = open('text.txt')
    b = f.read()
    if b == 0:
        print("h") 
    else:
        if ans.chat_id == b:
            if a == 1:
                return "ты че ахуела чекни базар даун"
            if a == 2:
                return "подведём итоги ты лох тупой и у тебя мать здохла, ты пиздишь всегда и выебываешься своими 5мм, так что соси мой пол метровый столб, хуйло ебанное!" 
            if a == 3:
                return "ты лох тупой чекни мать имбицыл"
            if a == 4:
                return "ты че имбицыл на забив в 9 утра хуйло понял пизда тебе пидорасина!"
            if a == 5:
                return "соболезную твоими 5мм"
            if a == 6:
                return "помнишь я твоей матери дилдо подарил и она тебя им избила?"
            if a == 7:
                return "/me отпиздил твоего кота и убил твою мать"
            if a == 8:
                return "твой отец тебя обоссал, выебал и ушел из семьи, все это не снимая штанов" 
            if a == 9:
                return "у твоего отца пол сантимнтра по этому твоя мать лягушка, сука она кричала от боли моего пол метрового столба"
            if a == 10:
                return "что-что? что ты там пищиж мразь я блять таких как ты по 10 штук в день обоссываю а ты ещё возникаешь хуепутало, если тебе не нравится мой хуй не соси ето же ты кричала э"

user.run_polling()
