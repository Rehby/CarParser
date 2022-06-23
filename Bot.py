
import asyncio
from aiogram import executor, Dispatcher, Bot


from Avito import data,firstrun
from Autoru import autoruCars, firstAutoru

# список для сравнение с id старого поста


TOKEN = "5415251166:AAHnqC5exvCQxlWIEkoyLRoaptBuySfySGM"
# userId = "342756595"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
userId=''




async def sendAvito(querry):
    while querry:
        asd = querry.pop(0)

        await bot.send_message(userId, f"ВРЕМЯ ДОБАВЛЕНИЕ ТОВАРА: { asd['time_vrem']}\n"
                                          f"НАЗВАНИЕ ТОВАРА: {asd['name_product']}\n"
                                          f"ЦЕНА {asd['price']}\n"
                                          f"ОПИСАНИЕ: {asd['infor']}\n"
                                          f"ВЛАДЕЛЕЦ: {asd['name_user']}\n"
                                          f"ССЫЛКА: {asd['more']}", disable_notification=True)

async def sendAutoru(querry):
    while querry:
        asd = querry.pop(0)
        await bot.send_message(userId, f"НАЗВАНИЕ ТОВАРА: {asd['carName']}\n"
                                       f"ГОД ВЫПУСКА: {asd['carYear']}\n"
                                       f"ПРОБЕГ:  {asd['carRange']}\n"
                                       f"ЦЕНА  {asd['carPrice']}\n"
                                       f"МЕСТОПОЛОЖЕНИЕ:  {asd['carPlace']}\n"
                                       f"ВЛАДЕЛЕЦ:  {asd['carSeller']}\n"
                                       f"ССЫЛКА:  {asd['carHref']}", disable_notification=True)

# тест на таймер
async def scheduled(wait_for):

    while True:

        # отлавливаем обрыв соединения
        try:
            await asyncio.sleep(wait_for)
            print("Проверка на наличие товара")
            # если нет товара
            try:
                avitocars = data()
                await sendAvito(avitocars)
            except:
                pass
            try:
                autorucars = autoruCars()
                await  sendAutoru(autorucars)
            except:
                pass

        except:
            pass

def strt():
    try:
        firstAutoru()
    except:
        pass
    try:
        firstrun()
    except:
        pass
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(10))


@dp.message_handler(commands=['start'])
async def start(message):
  global userId
  userId= message.from_user.id
  await bot.send_message(userId,f"{userId}")
  strt()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)