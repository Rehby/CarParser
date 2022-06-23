import random
import time

from bs4 import BeautifulSoup
import asyncio
from aiogram import executor, Dispatcher, Bot
from urllib.request import urlopen


# список для сравнение с id старого поста
old_posts = []
oldhrefsautoru = []
TOKEN = "5415251166:AAHnqC5exvCQxlWIEkoyLRoaptBuySfySGM"
userId = "342756595"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


def getAvitoHtml():
    global old_posts
    # ресурс на который мы заходим
    html = urlopen(
        "https://www.avito.ru/rossiya/avtomobili/do-500000-rubley-ASgCAgECAUXGmgwWeyJmcm9tIjowLCJ0byI6NTAwMDAwfQ?cd=1&f=ASgCAQECAUD2xA0UvrA6AUXGmgwWeyJmcm9tIjowLCJ0byI6NTAwMDAwfQ&i=1&radius=50&s=104")
    # скармливаем bs4
    bs0bj = BeautifulSoup(html, "lxml")
    # вычисляем id первого поста

    return bs0bj


async def avito():
    # делаем глобальным чтобы он был доступен внутри функции
    bs0bj = getAvitoHtml()
    id_product = bs0bj.find('div',
                            class_="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum")
    new_post = id_product["id"]
    # смотрим есть ли новый товар
    if old_posts.count(new_post) == 0:
        # если есть, определяем его как старый, для слудущей итерации
        old_post = new_post
        old_posts.append(new_post)
        time_vrem = bs0bj.find("div", {"data-marker": "item-date"}).get_text()

        # цена
        price = bs0bj.find("span", {"class": "price-text-_YGDY text-text-LurtD text-size-s-BxGpL"}).get_text()
        # название продукта
        name_product = bs0bj.find('h3',
                                  class_='title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO').text

        # общая информация
        infor = bs0bj.find("div", {
            "class": "iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD text-size-s-BxGpL"}).get_text()
        # имя владельца товара
        name_user = bs0bj.find("div", {"class": "style-title-_wK5H text-text-LurtD text-size-s-BxGpL"}).get_text()
        # ссыка на товар
        more = bs0bj.find("div", class_="iva-item-titleStep-pdebR").find("a").get("href")
        more = "https://www.avito.ru" + more

        # исправляем ошибки в кодировки
        rep = ["\u20bd", "\xb3", "\xb2", "\xd8", "\u2011", "\xa0"]
        for item in rep:
            if item in price:
                price = price.replace(item, "")

        await bot.send_message(userId, f"ВРЕМЯ ДОБАВЛЕНИЕ ТОВАРА: {time_vrem}\n"
                                       f"НАЗВАНИЕ ТОВАРА: {name_product}\n"
                                       f"ЦЕНА {price}\n"
                                       f"ОПИСАНИЕ: {infor}\n"
                                       f"ВЛАДЕЛЕЦ: {name_user}\n"
                                       f"ССЫЛКА: {more}", disable_notification=True)

    elif old_posts.count(new_post) != 0:
        return "Нового товара ещё нет!"


def getAutoruHtml():
    site = "https://auto.ru"
    city = "orenburg/"
    city = ""
    type = "used"
    price = "500000"
    url = f"{site}/{city}cars/{type}/do-{price}/?sort=cr_date-desc&top_days=1&output_type=carousel"
    # url  = f"https://auto.ru/orenburg/cars/used/do-500000/?sort=cr_date-desc"
    # url = "https://auto.ru/orenburg/cars/all/?output_type=table"
    print(url)
    classname = "ListingItemWide"
    # скармливаем bs4
    html = urlopen(url)

    bs0bj = BeautifulSoup(html, "html.parser")
    html = bs0bj.prettify("utf-8")
    with open("test.html", "wb") as file:
        file.write(html)
    #
    cars = bs0bj.find_all('div', class_=classname)

    #
    return cars


async def getAutoruCars():
    cars = getAutoruHtml()
    for car in cars:
        try:
            carTime = car.find('span', class_='ListingItemWide__sellerInfoItem').text
        except:
            pass
        carHref = car.find('a', class_="ListingItemWide__link")
        carHref = carHref['href']
        if oldhrefsautoru.count(carHref) == 0:
            oldhrefsautoru.append(carHref)
            carSeller = car.find('span', class_='ListingItemWide__sellerInfoItem').text
            carName = car.find('h3', class_='ListingItemWide__title').text
            carPrice = car.find('div', class_='ListingItemPrice__content').text
            carYear = car.find('div', class_='ListingItemWide__year').text

            carPlace = car.find('span', class_='MetroListPlace__regionName MetroListPlace_space').text
            carRange = car.find('div', class_='ListingItemWide__kmAge').text
            await bot.send_message(userId, f"НАЗВАНИЕ ТОВАРА: {carName}\n"
                                           f"ГОД ВЫПУСКА: {carYear}\n"
                                           f"ПРОБЕГ: {carRange}\n"
                                           f"ЦЕНА {carPrice}\n"
                                           f"МЕСТОПОЛОЖЕНИЕ: {carPlace}\n"
                                           f"ВЛАДЕЛЕЦ: {carSeller}\n"
                                           f"ССЫЛКА: {carHref}", disable_notification=True)


# тест на таймер
async def scheduled(wait_for):
    while True:
        # отлавливаем обрыв соединения
        try:
            await asyncio.sleep(wait_for)
            print("Проверка на наличие товара")
            # если нет товара
            try:
                await getAutoruCars()
                await avito()

            except:
                pass

        except:
            print("Соединение востановлено")
            print("Проверка на наличие товара")
            # если нет товара
            try:
                await avito()
            except:
                pass


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(10))
    executor.start_polling(dp, skip_updates=True)