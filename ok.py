from vkbottle.user import User, Message
from vkbottle.user import *
import random
import json

user = User("7dbedbfcd99fa3d128bf19fc63b1c5b7b748559c080979cf5e2f5602b3490bfc301c013f4cc6afc068a65")

def reg(ans):
    data = json.load(open("data.json", "r"))
    if str(ans.from_id) in data["user"]:
        pass
    else:
        data["user"][str(ans.from_id)] = "reg"
        data["status"][str(ans.from_id)] = "нету"
        data["id"][str(ans.from_id)] = str(len(data["user"]))
        json.dump(data, open("data.json", "w"))

@user.on.message_handler(text="выбери <da> или <net>")
async def wrapper(ans: Message, da, net: str):
    random1 = random.randint(1, 2)
    if random1 == 1:
        return f"я выбрал {da}"
    else:
        return f"я выбрал {net}"

@user.on.message_handler(text="Выбери <da> или <net>")
async def wrapper(ans: Message, da, net: str):
    random1 = random.randint(1, 2)
    if random1 == 1:
        return f"я выбрал {da}"
    else:
        return f"я выбрал {net}"

@user.on.message_handler(text="скажи <gay>")
async def wrapper(ans: Message, gay: str):
    if gay == "я гей":
        return "сам гей"
    else:
        return f"{gay}"

@user.on.message_handler(text="Скажи <gay>")
async def wrapper(ans: Message, gay: str):
    if item in ["гей", "ты гей", "батя твой гей"]:
        return "сам гей"
    else:
        return f"{gay}"

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
