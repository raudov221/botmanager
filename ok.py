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

@user.on.message_handler(text="<da>+<net>")
async def wrapper(ans: Message, da, net: str):
    c = int(da)+int(net)
    return f"🌿 [id{ans.from_id}|Пользователь], ответ: {c}"

@user.on.message_handler(text="<da>-<net>")
async def wrapper(ans: Message, da, net: str):
    c = int(da)-int(net)
    return f"🌿 [id{ans.from_id}|Пользователь], ответ: {c}"

@user.on.message_handler(text="<da>*<net>")
async def wrapper(ans: Message, da, net: str):
    c = int(da)*int(net)
    return f"🌿 [id{ans.from_id}|Пользователь], ответ: {c}"

@user.on.message_handler(text="<da>/<net>")
async def wrapper(ans: Message, da, net: str):
    c = int(da)/int(net)
    return f"🌿 [id{ans.from_id}|Пользователь], ответ: {c}"

@user.on.message_handler(text="обнять")
async def wrapper(ans: Message):
    return f"🤗 [id{ans.from_id}|Пользователь], обнял [id{ans.reply_message.from_id}|вас] =)"

@user.on.message_handler(text="?брак")
async def wrapper(ans: Message):
    return f"🤗 [id{ans.from_id}|Пользователь], появились молодо жёны [id{ans.reply_message.from_id}|вам] =)"
    f = open('text.txt')
    f.write(ans.from_id)
    b = open('text2.txt')
    b.write(ans.reply_message.from_id)

@user.on.message_handler(text="?браки")
async def wrapper(ans: Message):
    f = open('text.txt')
    b = open('text2.txt')
    return f"💞 Браки беседы\n\n1.[id{f.read()}|Любовь] 💚 [id{b.read()|Морковь]"

@user.on.message_handler(text="Обнять")
async def wrapper(ans: Message):
    return f"🤗 [id{ans.from_id}|Пользователь], обнял [id{ans.reply_message.from_id}|вас] =)"

@user.on.message_handler(text="обнять @<da>")
async def wrapper(ans: Message, da: str):
    return f"🤗 [id{ans.from_id}|Пользователь], обнял [{da}|вас] =)"

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
                return "что-что? что ты там пищиж мразь я блять таких как ты по 10 штук в день обоссываю а ты ещё возникаешь хуепутало, если тебе не нравится мой хуй не соси ето же ты кричала эй эй дядя дайте хуй пососать а я вам сотку дам блять токо прикол в том чо сотку я тебе не отдам такчто ты пойдешь просто нахуй поэтому соси пока есть возможность выбиться в люди"
            if a == 11:
                return f"- знаешь почему у твоей мамы всегда зубы свежие?\n- потому что мой хуй со вкусом тик така"
            if a == 12:
                return "угадай кто сегодня идет в кинотеатр с твоей матерью"
            if a == 13:
                return "имбицил ебаный хватит хуи сосать внатуре"
            if a == 14:
                return "научи свою мать не сосать хуй, если сам умеешь"
            if a == 15:
                return "тебе мудопиздюку не раз было сказано не сосать хуй"
            if a == 16:
                return "моргенштерн топ"
            if a == 17:
                return "бравл старс топ"
            if a == 18:
                return "аниме говно, Аллах топ"
 
@user.on.message_handler(text="Обнять @<da>")
async def wrapper(ans: Message, da: str):
    return f"🤗 [id{ans.from_id}|Пользователь], обнял [{da}|вас] =)"

@user.on.message_handler(text="трахнуть")
async def wrapper(ans: Message):
    return f"🤗 [id{ans.from_id}|Пользователь], трахнул [id{ans.reply_message.from_id}|вас] =)"

@user.on.message_handler(text="Трахнуть")
async def wrapper(ans: Message):
    return f"🤗 [id{ans.from_id}|Пользователь], трахнул [id{ans.reply_message.from_id}|вас] =)"

@user.on.message_handler(text="инфа <da>")
async def wrapper(ans: Message, da: str):
    random1 = random.randint(1, 100)
    return f"🤗 [id{ans.from_id}|Пользователь], я думаю что {da} - {random1}%"

@user.on.message_handler(text="Инфа <da>")
async def wrapper(ans: Message, da: str):
    random1 = random.randint(1, 100)
    return f"🤗 [id{ans.from_id}|Пользователь], я думаю что {da} - {random1}%"

@user.on.message_handler(text="бот <da>")
async def wrapper(ans: Message, da: str):
    return f"🤗 [id{ans.from_id}|Пользователь], привет"

@user.on.message_handler(text="Бот <da>")
async def wrapper(ans: Message, da: str):
    return f"🤗 [id{ans.from_id}|Пользователь], привет"

@user.on.message_handler(text="Иван <da>")
async def wrapper(ans: Message, da: str):
    return f"🤗 [id{ans.from_id}|Пользователь], привет"

@user.on.message_handler(text="<da> иван")
async def wrapper(ans: Message, da: str):
    return f"🤗 [id{ans.from_id}|Пользователь], привет"

@user.on.message_handler(text="<da> Иван")
async def wrapper(ans: Message, da: str):
    return f"🤗 [id{ans.from_id}|Пользователь], привет"

@user.on.message_handler(text="<da> бот")
async def wrapper(ans: Message, da: str):
    return f"🤗 [id{ans.from_id}|Пользователь], привет"

@user.on.message_handler(text="<da> Бот")
async def wrapper(ans: Message, da: str):
    return f"🤗 [id{ans.from_id}|Пользователь], привет"

@user.on.message_handler(text="Команды")
async def wrapper(ans: Message, da: str):
    return f"🤗 [id{ans.from_id}|Пользователь], все команды доступны по этой ссылке:\n\nvk.com/@579018447-komandy"

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
