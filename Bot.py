
import asyncio
from aiogram import executor, Dispatcher, Bot


from Avito import data,firstrun
from Autoru import autoruCars, firstAutoru
from Dromru import getDromruCars
from AutoruV2 import getdata

# список для сравнение с id старого поста


TOKEN = "5415251166:AAHnqC5exvCQxlWIEkoyLRoaptBuySfySGM"
# userId = "342756595"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
userId=[]




async def sendAvito(querry):
    while querry:
        asd = querry.pop(0)
        for chat in userId:
            await bot.send_message(chat, f"ВРЕМЯ ДОБАВЛЕНИЕ ТОВАРА: { asd['time_vrem']}\n"
                                          f"НАЗВАНИЕ ТОВАРА: {asd['name_product']}\n"
                                          f"ЦЕНА {asd['price']}\n"
                                          f"ОПИСАНИЕ: {asd['infor']}\n"
                                          f"ВЛАДЕЛЕЦ: {asd['name_user']}\n"
                                          f"ССЫЛКА: {asd['more']}", disable_notification=True)
#
# async def sendAutoru(querry):
#     while querry:
#         asd = querry.pop(0)
#         await bot.send_message(userId, f"НАЗВАНИЕ ТОВАРА: {asd['carName']}\n"
#                                        f"ГОД ВЫПУСКА: {asd['carYear']}\n"
#                                        f"ПРОБЕГ:  {asd['carRange']}\n"
#                                        f"ЦЕНА  {asd['carPrice']}\n"
#                                        f"МЕСТОПОЛОЖЕНИЕ:  {asd['carPlace']}\n"
#                                        f"ВЛАДЕЛЕЦ:  {asd['carSeller']}\n"
#                                        f"ССЫЛКА:  {asd['carHref']}", disable_notification=True)

async def sendAutoru2(querry):
    while querry:
        asd = querry.pop(0)
        adress=""
        if asd["address"]:
            adress= asd["address"]+" "+ asd["region_info"]
        else:
            adress=asd["region_info"]

        for chat in userId:
            await bot.send_message(chat, f"ВРЕМЯ ДОБАВЛЕНИЯ ОБЪЯВЛЕНИЯ: {asd['time']}\n"
                                       f"НАЗВАНИЕ ТОВАРА: {asd['car']}\n"
                                       f"ГОД ВЫПУСКА: {asd['year']}\n"
                                       f"ПРОБЕГ:  {asd['mileage']}\n"
                                       f"ЦЕНА  {asd['price']}\n"
                                       f"МЕСТОПОЛОЖЕНИЕ:  {adress}\n"
                                       f"ПТС: {asd['pts']}\n"
                                       f"КОЛИЧЕСТВО ВЛАДЕЛЬЦЕВ: {asd['owner_count']}\n"
                                       f"ССЫЛКА:  {asd['url']}", disable_notification=True)

async def sendDromru(querry):
    while querry:
        asd = querry.pop(0)

        for chat in userId:
            await bot.send_message(chat, f"НАЗВАНИЕ ТОВАРА: {asd['carName']}\n"
                                       f"ДАТА ПУБЛИКАЦИИ:  {asd['carTime']}\n"
                                       f"ЦЕНА  {asd['carPrice']}\n"
                                       f"МЕСТОПОЛОЖЕНИЕ:  {asd['carPlace']}\n"
                                       f"ССЫЛКА:  {asd['carHref']}", disable_notification=True)

# тест на таймер
async def scheduled(wait_for):

    while True:
        await asyncio.sleep(wait_for)



        # отлавливаем обрыв соединения
        try:
            print("Проверка на наличие товара")
            dromrucars = getDromruCars()
            
            await  sendDromru(dromrucars)

            # autoru=getdata()
            # await sendAutoru2(autoru)
            # # если нет товара
            # try:
            #     avitocars = data()
            #     await sendAvito(avitocars)
            # except:
            #     pass



        except:
            pass

def strt():
    # try:
    #     firstAutoru()
    # except:
    #     pass
    try:
        firstrun()
    except:
        pass
    try:
        pass
        # firstDromru()
    except:
        pass
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(10))


@dp.message_handler(commands=['start'])
async def start(message):
    global userId
    userId.append( message.from_user.id)
# strt()
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(10))

async def test(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        avitocars = data()
        await sendAvito(avitocars)

if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)