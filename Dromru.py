import json
from bs4 import BeautifulSoup
from urllib.request import urlopen

oldhrefs = []
newPosts=[]


def getDromHtml():
    city = "orenburg"
    site = f"https://{city}.drom.ru"
    price = "7000000"
    url = f"{site}/auto/all/?maxprice={price}"
    allurl='https://auto.drom.ru/all/?maxprice=7000000'
    print(url)
    classname = "css-xb5nz8 ewrty961"
    # скармливаем bs4
   
    html = urlopen(url)
    
    bs0bj = BeautifulSoup(html, "html.parser")

    cars = bs0bj.find_all('a', class_=classname)

    return cars


def getDromruCars():
    
    cars = getDromHtml()
    for car in cars:
        try:
            carHref = car['href']
            
            if oldhrefs.count(carHref) == 0:
                oldhrefs.append(carHref)    
                carName = car.find('div', class_="css-17lk78h e3f4v4l2").text
                
                carPlace = car.find('span', class_="css-1488ad e162wx9x0").text
            
                carTime = car.find('div', class_="css-1x4jcds eotelyr0").find('div').text
                
                carPrice=car.find('span', class_='css-46itwz e162wx9x0').find('span').text
                

                newPosts.append({   "carHref":carHref,
                                    "carName":carName,
                                    "carTime":carTime,
                                    "carPrice":carPrice,
                                    "carPlace":carPlace
                                    })
        except:
            print("here1")
        
  
    return newPosts


def dromrucars():
    global newPosts
    getDromruCars()
    return newPosts

# def firstDromru():
#     global oldhrefs
#     cars = getDromHtml()
#     for car in cars:
#         carHref = car['href']
#         if oldhrefs.count(carHref) == 0:
#             oldhrefs.append(carHref)

if __name__ == '__main__':
    
    getDromHtml()


