from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

bot = Bot("6501673043:AAG1b669q83f9DJeeqnMhPc0n9Q2MIdkH2U")

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(msg: Message):
    await msg.answer('''🔥 Xush kelibsiz, siz bot orqali yuklab olishingiz mumkin

 • Instagram - istalgan formatdagi hikoyalar, postlar va IGTV!

 • TikTok - istalgan formatdagi moyboyoqsiz videolar!

 • YouTube shorts - istalgan formatdagi videolar!
 • Qo'shiqni topib berishim uchun, menga quyidagilardan birini yuboring:
 • Qo'shiq nomi yoki ijrochi ismi
 • Ovozli xabar
 • Video
 • Audio
 • Video xabar''')

@dp.inline_handler(lambda msg:True)
async def inline_handler(msg: 'InlineQuery'):
    text = msg.query

    results = [
        InlineQueryResultArticle(
            id ='1',title ='Your query',input_message_content=InputTextMessageContent(text)) for music in 
        ]

    await bot.answer_inline_query(inline_query_id=msg.id, results=results, cache_time=1)




executor.start_polling(dp)


