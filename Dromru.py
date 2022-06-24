from bs4 import BeautifulSoup
from urllib.request import urlopen

oldhrefs = []
newPosts=[]


def getDromHtml():
    print("here")
    city = "orenburg."
    site = f"https://{city}drom.ru/"
    price = "700000"
    url = f"{site}/auto/all/?maxprice={price}"
    url = "https://auto.drom.ru/all/?maxprice=700000"
    print(url)
    classname = "css-5l099z ewrty961"
    # скармливаем bs4
    html = urlopen(url)

    bs0bj = BeautifulSoup(html, "html.parser")
     #
    cars = bs0bj.find_all('a', class_=classname)

    #
    return cars


def getDromruCars():
    global newPosts
    cars = getDromHtml()
    for car in cars:

        carHref = car['href']
        if oldhrefs.count(carHref) == 0:
            oldhrefs.append(carHref)
            carName = car.find('div', class_="css-17lk78h e3f4v4l2").find('span').text
            carPlace = car.find('div', class_="css-1x4jcds eotelyr0").find('span').text
            carTime = car.find('div', class_="css-1x4jcds eotelyr0").find('div').text
            carPrice=car.find('span', class_='css-46itwz e162wx9x0').find('span').text
            carRange=car.find('span', class_='/html/body/div[2]/div[4]/div[1]/div[1]/div[5]/div/div[2]/a[1]/div[2]/div[2]/span[5]')
            carPrice.replace("\xa0"," ")


            newPosts.append({"carHref":carHref,
                             "carName":carName,
                             "carTime":carTime,
                             "carPrice":carPrice,
                             "carPlace":carPlace,
                             "carRange":carRange})
    return newPosts


def dromrucars():
    global newPosts
    getDromruCars()
    return newPosts

def firstDromru():
    cars = getDromHtml()
    for car in cars:
        carHref = car['href']
        if oldhrefs.count(carHref) == 0:
            oldhrefs.append(carHref)

if __name__ == '__main__':
    getDromruCars()
    print(newPosts)


