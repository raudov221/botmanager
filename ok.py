from vkbottle import Bot, Message, keyboard_gen, Branch, ExitBranch, Mailing
bot = Bot('1ae80fd1fc2e59106902a96597761f4802b05b1787c147dbafef93e57b76447f8ea735c2af528562616d0', group_id, debug=True)
mailing = Mailing('api_82735_N1cGUGYqt2f3oPL5YHFoLSSM', bot) # токен бери из настроек приложения 
group_id = 200759417

@bot.on.message('/mail <text>')
async def mail(ans: Message, text):
  m = mailing([1050338])
  m(text)
  await ans('Рассылка началась!')
  a = await m.run_now()

bot.run_polling()
