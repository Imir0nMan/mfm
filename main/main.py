import codecs

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='5316993267:AAEy6Pqkt7c8fIKpXedwtIe8BSwdnntRoag')

dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message : types.message):
    File=codecs.open("data.txt","r","utf-8")
    arr=File.readlines()
    arr.append("\n"+str(message.chat.id))
    File=codecs.open("data.txt","w","utf-8")
    File.writelines(arr)


executor.start_polling(dp, skip_updates=False)