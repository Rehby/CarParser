from bs4 import BeautifulSoup
from urllib.request import urlopen

oldhrefsautoru = []
newPosts=[]


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
    #
    cars = bs0bj.find_all('div', class_=classname)

    #
    return cars


def getAutoruCars():
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

            newPosts.append({"carHref":carHref,
                             "carSeller":carSeller,
                             "carName":carName,
                             "carPrice":carPrice,
                             "carYear":carYear,
                             "carPlace":carPlace,
                             "carRange":carRange})

def autoruCars():
    getAutoruCars()
    return newPosts

def firstAutoru():
    cars = getAutoruHtml()
    for car in cars:
        carHref = car.find('a', class_="ListingItemWide__link")
        carHref = carHref['href']
        if oldhrefsautoru.count(carHref) == 0:
            oldhrefsautoru.append(carHref)
