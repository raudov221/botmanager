from vkbottle.user import User, Message
import random

user = User("fa7173fc604f10a6664772707231425811ef9d66bd758357e6d0b799cbbed4261836b049220164c0d5da1")

@user.on.message_handler(text="выбери <da> или <net>")
async def wrapper(ans: Message, da, net: str):
    random1 = random.randint(1, 2)
    if random1 == 1:
        return f"🌿 [id{ans.from_id}|Пользователь], Я выбрал: {da}"
    else:
        return f"🌿 [id{ans.from_id}|Пользователь], Я выбрал: {net}"

@user.on.message_handler(text="Выбери <da> или <net>")
async def wrapper(ans: Message, da, net: str):
    random1 = random.randint(1, 2)
    if random1 == 1:
        return f"🌿 [id{ans.from_id}|Пользователь], Я выбрал: {da}"
    else:
        return f"🌿 [id{ans.from_id}|Пользователь], Я выбрал: {net}"
    
@user.on.message_handler(text="наградить медалью <da>")
async def wrapper(ans: Message, da: str):
    return f"🌿 [id{ans.from_id}|Пользователь], наградил [id{ans.reply_message.from_id}|вас] медалью {da}"

@user.on.message_handler(text="Наградить медалью <da>")
async def wrapper(ans: Message, da: str):
    return f"🌿 [id{ans.from_id}|Пользователь], наградил [id{ans.reply_message.from_id}|вас] медалью {da}"

@user.on.message_handler(text="<gay>")
async def wrapper(ans: Message, gay: str):
    random1 = random.randint(1, 5)
    random5 = random.randint(1, 100)
    asa = 0
    if random5 == 100:
        asa = 100
    if asa == 100:
        if random1 == 1:
            return "- Почему ваша кошка по субботам орет?\n- А мы ее моем.\n- Мы свою тоже моем по субботам...\n- А вы выжимать пробовали?"
            asa = 0
        if random1 == 2:
            return "- Почему в мультфильме Маша и Медведь не показывают родителей Маши?\n- Они, наверное, уже в дурдоме!"
            asa = 0
        if random1 == 3:
            return "Нетрезвый житель Ухрюпинска замахнулся на святое, но батюшка ударил раньше."
            asa = 0
        if random1 == 4:
            return "Ребята, сделайте меня пожалуйста замом министра чего угодно, мне чисто ипотеку закрыть и всё, я дальше сам уволюсь, обещаю. Я всё посчитал, чтобы закрыть ипотеку мне на таком посту потребуется 17 секунд."
            asa = 0
        if random1 == 5:
            return "Достаю из холодильника двухлитровую колу, директор: о, и мне налей!... и как объяснить, что она с вискарем уже?"
            asa = 0
    
user.run_polling()
