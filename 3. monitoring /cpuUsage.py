import psutil
import asyncio
import telegram

chatId = 111111
botToken = ''
result = psutil.getloadavg()[0]
async def send(chat, msg):
    await telegram.Bot(botToken).sendMessage(chat_id=chat, text=msg)

if result > 1:
    asyncio.run(send({chatId}, 'Load Average is high (' + result +')' ))
