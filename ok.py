from vkbottle.ext import Middleware
from vkbottle.user import User, Message
from vkbottle.api import API
from vkbottle import PhotoUploader
from rextester_py import rexec_aio
from urllib.request import urlopen
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import math, random, mc, json, sqlite3

db = sqlite3.connect('database.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users(
	id BIGINT,
	name TEXT,
	balance BIGINT,
	marry_date TEXT,
	marry_id BIGINT
)""")
db.commit()

user = User("b516fcaf9c73ae2b6fdb11558f29a10167a3dd8a8178f1cafafa563a503889d2e03510b836d41d4ec5c6c", mobile = True)
api = API("b516fcaf9c73ae2b6fdb11558f29a10167a3dd8a8178f1cafafa563a503889d2e03510b836d41d4ec5c6c")
photo_uploader = PhotoUploader(user.api, generate_attachment_strings=True) 

def banned_words(text: str):
	text = text.replace("vto.ре","").replace("https://vto.ре","").replace(".com","").replace(".ru","").replace(".lol","").replace("sex","").replace("porno","")
	return text

@user.middleware.middleware_handler()
class Registration(Middleware):
	async def pre(self, ans: Message):
		if ans.from_user and len(q.execute(f"SELECT * FROM users WHERE id = {ans.from_id}").fetchall()) == 0:
			await ans(f"ты зарегался уебок")

@user.on.message_handler(text = "выбери <da> или <net>", lower = True)
async def wrapper(ans: Message, da, net: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    return f"🌿 [id{ans.from_id}|{penis[0].first_name}], Я выбрал: {random.choice(banned_words(str(da)),banned_words(str(net)))}"
    
@user.on.message_handler(text="наградить медалью <da>", lower = True)
async def wrapper(ans: Message, da: str):
    if ans.from_id == 579018447:
        return f"🌿 [id{ans.from_id}|Пользователь], наградил [id{ans.reply_message.from_id}|вас] медалью {da}"
    else:
        return f"🌿 Недостаточно прав!"

@user.on.message_handler(text="?брак",lower = True)
async def wrapper(ans: Message):
    return f"🤗 [id{ans.from_id}|Пользователь], появились молодо жёны [id{ans.reply_message.from_id}|вам] =)"

@user.on.message_handler(text="?браки",lower = True)
async def wrapper(ans: Message):
    f = open("text.txt", "r")
    b = open("text2.txt", "r")
    return f"💞 Браки беседы\n\n1.[id{f.read()}|Любовь] 💚 [id{b.read()}|Морковь]"

@user.on.message_handler(text="Обнять",lower = True)
async def wrapper(ans: Message):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    return f"🤗 [id{ans.from_id}|{penis[0].first_name}] обнял кого то =)"

@user.on.message_handler(text="/me <da>", lower = True)
async def wrapper(ans: Message, da: str):
    return f"[id{ans.from_id}|Пользователь], {da}"

@user.on.message_handler(text = "кто <da>", lower = True)
async def wrapper(ans: Message, da: str):
	penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
	da = banned_words(da)
	users = await user.api.messages.get_conversation_members(peer_id=ans.peer_id)
	return f'🌀 [id{ans.from_id}|{penis[0].first_name}], я думаю что {da} @id{random.choice([member.id for member in users.profiles if member.id])} (он)!'

@user.on.message_handler(text="стикеры", lower = True)
async def wrapper(ans: Message):
	penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
	if ans.reply_message:
		all_stickers = await api.request('gifts.getCatalog', {'user_id': ans.reply_message.from_id})
		stickers = [f"{i['sticker_pack']['title']}" for i in all_stickers[1]['items'] if 'disabled' in i]
		if len(stickers) > 0:
			return f"🤑 [id{ans.from_id}|{penis[0].first_name}], у него есть {len(stickers)} стикерпака: \n\n{', '.join(stickers)}"
		else:
			return f"🤑 [id{ans.from_id}|{penis[0].first_name}], у него нету стикеров!"
	else:
		all_stickers = await api.request('gifts.getCatalog', {'user_id': ans.from_id})
		stickers = [f"{i['sticker_pack']['title']}" for i in all_stickers[1]['items'] if 'disabled' in i]
		if len(stickers) > 0:
			return f"🤑 [id{ans.from_id}|{penis[0].first_name}], у вас есть {len(stickers)} стикерпака: \n\n{', '.join(stickers)}"
		else:
			return f"🤑 [id{ans.from_id}|{penis[0].first_name}], у вас нету стикеров!"
		

@user.on.message_handler(text=["корень <da>","√<da>"],lower = True)
async def wrapper(ans: Message, da: str):
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    return f"🌿 [id{ans.from_id}|{penis[0].first_name}], ответ: {math.sqrt(int(da))}"

@user.on.message_handler(text="send <da>", lower = True)
async def wrapper(ans: Message, da: str):
    brawl = ans.from_id
    await user.api.messages.send(user_id=brawl, random_id=0, message=f'{da}')
    return f"Message from {ans.from_id} send"

@user.on.message_handler(text = "пример <da>", lower = True)
async def wrapper(ans: Message, da):
	penis = await user.api.users.get(user_ids = ans.from_id, fields='is_closed')
	list = [i for i in da if str(i) in ["1","2","3","4","5","6","7","8","9","0","+","-","/","*"]]
	if len(list) == len(da):
		return f"🌿 [id{ans.from_id}|{penis[0].first_name}], ответ: {'{0:,}'.format(eval(da))}"""
	else:
		return f"🌿 [id{ans.from_id}|{penis[0].first_name}], Я могу решить пример только из цифр."

@user.on.message_handler(text="py <da>", lower = True) 
async def wrapper(ans: Message, da: str):
    c = da.replace("~", "    ")
    rex = await rexec_aio(f"python 3", "{c}", None) 
    penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
    return f"🌿 [id{ans.from_id}|{penis[0].first_name}], вывод: {banned_words(rex.results)}"

@user.on.message_handler(text="shadow")
async def wrapper(ans: Message):
    await ans("шадоф", attachment="audio579018447_456239069")

@user.on.message_handler(text=['!затемни', '!Затемни'], lower = True)
async def darked(ans: Message):

	await ans(f'🖼 Пользователь, началась обработка фотографии..')

	if ans.reply_message: 
		img = ans.reply_message.attachments[0].photo.sizes[-1].url

	elif ans.fwd_messages:
		img = ans.fwd_messages[0].attachments[0].photo.sizes[-1].url

	else:
		img = ans.attachments[0].photo.sizes[-1].url


	source = Image.open(urlopen(img))
	result = Image.new('RGB', source.size)

	for x in range(source.size[0]):
		for y in range(source.size[1]):
			r, g, b = source.getpixel((x, y))

			red = min(255, max(0, int(r * 0.5)))
			green = min(255, max(0, int(g * 0.5)))
			blue = min(255, max(0, int(b * 0.5)))
			result.putpixel((x, y), (red, green, blue))

		fp = BytesIO()
		result.save(fp, 'PNG')
		setattr(fp, "name", "image.png")

		await ans('😇 Готово. Сохраняй!', attachment=await photo_uploader.upload(fp))

@user.on.message_handler(text="морген", lower = True)
async def wrapper(ans: Message):
    await ana("Твой морген)", attachment="audio542720500_67823365")

@user.on.message_handler(text="text <da>", lower = True)
async def darked(ans: Message, da):

	img = Image.new('RGB', (200,200), color=('#9ACEEB'))
	font_type = ImageFont.load_default()
	draw = ImageDraw.Draw(img)

	draw.multiline_text((100, 50), f"{da}", 56, font=font_type)
	img.save('photo1_watermarked.png')

	photo = await photo_uploader.upload_message_photo('photo1_watermarked.png')
	await ans('Держите фото:', attachment=photo)

@user.on.message_handler(text=".text <x> <y> <da>", lower = True)
async def darked(ans: Message, x, y, da):

	img = Image.new('RGB', (200,200), color=('#9ACEEB'))
	font_type = ImageFont.load_default()
	draw = ImageDraw.Draw(img)

	draw.multiline_text((int(x), int(y)), f"{da}", 56, font=font_type)
	img.save('photo1_watermarked.png')

	photo = await photo_uploader.upload_message_photo('photo1_watermarked.png')
	await ans('Держите фото:', attachment=photo)

@user.on.message_handler(text=".Хентай", lower = True)
async def wrapper(ans: Message):
	photo = await photo_uploader.upload_message_photo('1.jpg')
	await ans('🥺 Держите хентай:', attachment=photo)

@user.on.message_handler(text = "спам <da>; <count>", lower = True) 
async def wrapper(ans: Message, da, count):
	if ans.from_id in [579018447,447409965]:
		if count.isdigit():
			return str(da)*int(count)
		else:
			return "мб количество числом, не?"

@user.on.message_handler()
async def wrapper(ans: Message):
	data = json.load(open("words.json","r",encoding="utf-8"))
	procent = random.randint(1,25)
	if procent > 20:
		data["words"].append(ans.text)
		json.dump(data, open("words.json","w"),ensure_ascii=False)
		r1 = random.choice(data["words"])
		r2 = random.choice(data["words"])
		generator = mc.StringGenerator(samples = [r1,r2])
		result = generator.generate_string()
		await ans(f"{result}")

user.run_polling() 
