from bs4 import BeautifulSoup
import asyncio
from aiogram import executor, Dispatcher, Bot
from urllib.request import urlopen

# список для сравнение с id старого поста


posts=[]
querry=[]


def goTelegram(product):
    time_vrem = product.find("div", {"data-marker": "item-date"}).get_text()

    # цена
    price = product.find("span", {"class": "price-text-_YGDY text-text-LurtD text-size-s-BxGpL"}).get_text()
    # название продукта
    name_product = product.find('h3', class_='title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO').get_text()

    # общая информация
    infor = product.find("div", {
        "class": "iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD text-size-s-BxGpL"}).get_text()
    # ссыка на товар

    more = product.find("div", class_="iva-item-titleStep-pdebR").find("a").get("href")
    more = "https://www.avito.ru" + more

    # имя владельца товара
    try:
        name_user = product.find("div", {"class": "style-title-_wK5H text-text-LurtD text-size-s-BxGpL"}).get_text()
    except:
        name_user="Отсутствует"
    # исправляем ошибки в кодировки
    rep = ["\u20bd", "\xb3", "\xb2", "\xd8", "\u2011", "\xa0"]
    for item in rep:
        if item in price:
            price = price.replace(item, "")
    return time_vrem, name_product, price, infor.replace('\n', ''), name_user, more

def getAvitoCars():
    url="https://www.avito.ru/orenburg/avtomobili/do-700000-rubley-ASgCAgECAUXGmgwWeyJmcm9tIjowLCJ0byI6NzAwMDAwfQ?i=1&presentationType=serp&radius=50&s=104&searchForm=true"
     # скармливаем bs4
    html = urlopen(url)
    bs0bj = BeautifulSoup(html, "html.parser")

    cars = bs0bj.find_all('div',
                                  class_="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum")

    return cars




def data():
    cars = getAvitoCars()

    for product in cars:
        if (posts.count(product['id']) == 0):

            posts.append(product['id'])
            time_vrem, name_product, price, infor, name_user, more = goTelegram(product)

            querry.append(
                {"time_vrem": time_vrem, "name_product": name_product, "price": price, "infor": infor,
                 "name_user": name_user, "more": more})
    return querry

def firstrun():
    cars = getAvitoCars()
    for product in cars:
        if (posts.count(product['id']) == 0):
            posts.append(product['id'])


if __name__ == "__main__":
    # first load
    firstrun()


