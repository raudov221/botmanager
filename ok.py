from vkbottle.user import User, Message
import time
import json
import random

user = User("9dfe8d5d73be0a5004b6be0f087c2101e2763a7a7408fc789dece8c04b8892e16aa239baf5563a2590956", mobile=True)

def reg( ans ):
    data = json.load( open( "data.json", "r" ) )
    if str( ans.from_id ) in data[ "user" ]:
        pass
    else:
        data[ "user" ][ str( ans.from_id ) ] = "reg"
        data[ "balance" ][ str( ans.from_id ) ] = 0
        data[ "role" ][ str( ans.from_id ) ] = "noob"
        json.dump( data, open( "data.json", "w" ) )

roles = []

@user.on.message_handler(text=["я", "проф", "профиль"], lower=True)
async def wrapper(ans: Message):
	reg( ans )
	penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
	
	data = json.load( open( "data.json", "r" ) )
	await ans(f"🔮 [id{ans.from_id}|{penis[0].first_name}], \n\n💵 Баланс: {data['balance'][str(ans.from_id)]}\n💜 Роль: {data['role'][str(ans.from_id)]}")

@user.on.message_handler(text="роли", lower=True)
async def wrapper(ans: Message):
	reg( ans )
	penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
	data = json.load( open( "data.json", "r" ) )
	await ans(f"🦊 [id{ans.from_id}|{penis[0].first_name}], Все роли:\n\n{roles}\n\n 💸 Создать свою роль: /роль купить 'ваша роль' 100 монет.")
	
@user.on.message_handler(text="/роль купить <role>", lower=True)
async def wrapper(ans: Message, role):
	reg( ans )
	penis = await user.api.users.get(user_ids=ans.from_id, fields='is_closed')
	data = json.load( open( "data.json", "r" ) )
	if data["balance"][str(ans.from_id)] > 100:
		data["balance"][str(ans.from_id)] -= 100
		data["role"][str(ans.from_id)] = f"{role}"
		roles + [f"{penis[0].first_name} - {data['role'][str(ans.from_id)]}"]
		await ans(f"📄 [id{ans.from_id}|{penis[0].first_name}], Вы приобрели свою роль.")

@user.on.message_handler(text="<sum>", lower=True)
async def wrapper(ans: Message, sum):
	reg( ans )
	data = json.load( open( "data.json", "r" ) )
	data["balance"][str(ans.from_id)] += 1
	json.dump( data, open( "data.json", "w" ) )

user.run_polling()
