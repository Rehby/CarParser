import requests
import json

getcars = []
carsId=[]
price=700000
radius=100
first=True
def getresponse():

    cookies = {
        'autoruuid': 'g62ac19b52vec2i0rtvtbsbbqa05mkcc.2af9859dd974f02a2fbba35fcc7b59f3',
        'suid': '86a8092a5e2a90d80f50b65c774b310f.a7bc70f1869dc5947d467689e643fce4',
        'yandexuid': '5580061191626176752',
        'my': 'YycCAAEA',
        '_ym_uid': '1626281942140756140',
        'counter_ga_all7': '1',
        'new-controls-notify-hidden': 'true',
        'hide-proauto-pimple': '1',
        'card_prevnext_swipe_info': '1',
        'autoru_sid': 'a%3Ag62ac19b52vec2i0rtvtbsbbqa05mkcc.2af9859dd974f02a2fbba35fcc7b59f3%7C1656050741781.604800.psvS9ZLA1VFaRfw2FVuArQ.oASuqrfGT5JXbCKwJh3tqA9VfqNxQ6kJoT93iFd3eJs',
        'bltsr': '1',
        'los': '1',
        'safe_deal_promo': '3',
        'yuidlt': '1',
        'ys': 'udn.cDpPbGVn%23c_chck.3556112206',
        'cmtchd': 'MTY1NjA3NzUxNTk4Mw==',
        'crookie': 'UP+mBIuRtAcy2SpRZiQi2/WBh+UY2hS0Tw/9+NAD3CHQHG95Kj9v0pz7krEXR+4QWR3btOttvNEQDgPbXNcqzN2BG24=',
        '_csrf_token': 'e57274a5d51949d4d32360c53482471a4e3d92e3cc7cd6e4',
        'from': 'direct',
        'gdpr': '0',
        '_ym_isad': '1',
        'sso_status': 'sso.passport.yandex.ru:blocked',
        'gids': '48',
        'spravka': 'dD0xNjU2MzI3MDkwO2k9MTQ1LjI1NS4yMi4yMjM7RD00QjU1RjdFNEVDMEU1NTU3QzlBMzgyMTA0RTk0NENFQTZBRDEyRDE0N0ZCODYwRjhDM0UyMDc2MTc4QTRCMEM0MjZCQThFNDA7dT0xNjU2MzI3MDkwODA3MzI4NTIyO2g9NDg2ODdmMmU3NzU5NTM3ZWY1N2QzZjExM2RiMzNiNzk=',
        'listing_view_session': '{}',
        'listing_view': '%7B%22output_type%22%3Anull%2C%22version%22%3A1%7D',
        'autoru-visits-count': '9',
        '_yasc': 'iKXlTJsuLLv1gaYc24U2dtkc5z8vHg88Ih5ngfLtpBiDteI+fZg=',
        'gradius': '100',
        'from_lifetime': '1656338849888',
        '_ym_d': '1656338854',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-RU;q=0.8,en;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'autoruuid=g62ac19b52vec2i0rtvtbsbbqa05mkcc.2af9859dd974f02a2fbba35fcc7b59f3; suid=86a8092a5e2a90d80f50b65c774b310f.a7bc70f1869dc5947d467689e643fce4; yandexuid=5580061191626176752; my=YycCAAEA; _ym_uid=1626281942140756140; counter_ga_all7=1; new-controls-notify-hidden=true; hide-proauto-pimple=1; card_prevnext_swipe_info=1; autoru_sid=a%3Ag62ac19b52vec2i0rtvtbsbbqa05mkcc.2af9859dd974f02a2fbba35fcc7b59f3%7C1656050741781.604800.psvS9ZLA1VFaRfw2FVuArQ.oASuqrfGT5JXbCKwJh3tqA9VfqNxQ6kJoT93iFd3eJs; bltsr=1; los=1; safe_deal_promo=3; yuidlt=1; ys=udn.cDpPbGVn%23c_chck.3556112206; cmtchd=MTY1NjA3NzUxNTk4Mw==; crookie=UP+mBIuRtAcy2SpRZiQi2/WBh+UY2hS0Tw/9+NAD3CHQHG95Kj9v0pz7krEXR+4QWR3btOttvNEQDgPbXNcqzN2BG24=; _csrf_token=e57274a5d51949d4d32360c53482471a4e3d92e3cc7cd6e4; from=direct; gdpr=0; _ym_isad=1; sso_status=sso.passport.yandex.ru:blocked; gids=48; spravka=dD0xNjU2MzI3MDkwO2k9MTQ1LjI1NS4yMi4yMjM7RD00QjU1RjdFNEVDMEU1NTU3QzlBMzgyMTA0RTk0NENFQTZBRDEyRDE0N0ZCODYwRjhDM0UyMDc2MTc4QTRCMEM0MjZCQThFNDA7dT0xNjU2MzI3MDkwODA3MzI4NTIyO2g9NDg2ODdmMmU3NzU5NTM3ZWY1N2QzZjExM2RiMzNiNzk=; listing_view_session={}; listing_view=%7B%22output_type%22%3Anull%2C%22version%22%3A1%7D; autoru-visits-count=9; _yasc=iKXlTJsuLLv1gaYc24U2dtkc5z8vHg88Ih5ngfLtpBiDteI+fZg=; gradius=100; from_lifetime=1656338849888; _ym_d=1656338854',
        'Origin': 'https://auto.ru',
        'Pragma': 'no-cache',
        'Referer': f'https://auto.ru/orenburg/cars/used/do-{price}/?sort=cr_date-desc',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'same-origin',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-client-app-version': '73.0.9633320',
        'x-client-date': '1656338869713',
        'x-csrf-token': 'e57274a5d51949d4d32360c53482471a4e3d92e3cc7cd6e4',
        'x-page-request-id': 'e5ecbbc79aa99bcbdab7aabc784ea58f',
        'x-requested-with': 'XMLHttpRequest',
        'x-retpath-y': f'https://auto.ru/orenburg/cars/used/do-{price}/?sort=cr_date-desc',
        'x-yafp': '{"a1":"xRSe5OGGTxjLwg==;0","a2":"xbm+baHBAsywXqcTEipWJ/Uyc7HBvQ==;1","a3":"CLRnkpJFU4yaXoeSai4/6g==;2","a4":"5ZQt5VDVPdGXODchCyBzv3RKcxyXq2Zo4VNp5oHbMVCZXJ5+q2fPFx6Yp/NXRg==;3","a5":"fGT+NjIf5+RHiA==;4","a6":"ODs=;5","a7":"muE+d2yXvrRDPg==;6","a8":"bcETWmUM2bA=;7","a9":"4EeXPyt0f3CLlg==;8","b1":"adk6jJYCLvc=;9","b2":"HF43h7h8xH7G1A==;10","b3":"bP4YiBy8lUkysw==;11","b4":"FRaXIdqqx2E=;12","b5":"Qp2MYYqYrFfuXQ==;13","b6":"hwEHxM5BDXomNg==;14","b7":"TVNe7Z/9vHEBkg==;15","b8":"+AEsf66yHhDCrA==;16","b9":"rCzBbkfKgphjXw==;17","c1":"GMzMjg==;18","c2":"hO6x+fD2Q+F+aKqjXbSGZQ==;19","c3":"b9rJr7hRrCv1ybUsPqOfQg==;20","c4":"6xgqyXol82I=;21","c5":"0FApRYBIS70=;22","c6":"JSqQHA==;23","c7":"bSQl1ehmgww=;24","c8":"pRY=;25","c9":"qkEuZhLm7MQ=;26","d1":"diVSgHH0604=;27","d2":"U70=;28","d3":"xbJySCrCp65kLQ==;29","d4":"lFR0F0+4aSA=;30","d5":"c+sqynz2Rcg=;31","d7":"E+lE8/mIx74=;32","d8":"Fycp9SiSIUjObM5Q3z96EyFOCCiYu636zeY=;33","d9":"CngQ/eBi3lk=;34","e1":"ATuTGojVFzYmPw==;35","e2":"MVpWoi0U/ug=;36","e3":"6QGMDLoxOmI=;37","e4":"87p7umTliZo=;38","e5":"yxKV148casTblw==;39","e6":"/wYsNQC6gLk=;40","e7":"QrszM5bCjlA5TA==;41","e8":"Ek6Qd3u/JU4=;42","e9":"RXiXpQ+oi9E=;43","f1":"SKJcwWHe6IF1JQ==;44","f2":"3W9ZmEwA2PQ=;45","f3":"+4Waxw0gHZP8rQ==;46","f4":"zt1pAhrzwlw=;47","f5":"LTz+Oi3QrMMLrA==;48","f6":"kNqz4aqZr2k56Q==;49","f7":"6+IjTyUBVyW8Eg==;50","f8":"SkQshKpujIvhxQ==;51","f9":"Xym359tfUW0=;52","g1":"FIuH93ejRcEUAw==;53","g2":"0b0D2HOXm1euCg==;54","g3":"jShYcxKSneY=;55","g4":"d4YHaMu8SJLBXw==;56","g5":"d1t8vrANrM8=;57","g6":"0TaTHEKMx8g=;58","g7":"vjdU3UrdWec=;59","g8":"0adlm+2Px94=;60","g9":"/HA0xN7q/7A=;61","h1":"cxYRTBJ9ZQvcDw==;62","h2":"Uq4Ct2KACkynhw==;63","h3":"p7bj/fBTCyzQWg==;64","h4":"S/2B27zQjhILKg==;65","h5":"J7irEmeq3cs=;66","h6":"b+jm0Z1B/FgvUQ==;67","h7":"2vHodKl0cDmBrqqPlDWAyMPYZPw1kc7Os53as+XrcdJYYVKN;68","h8":"xyOTSsve2/hn0Q==;69","h9":"LrMxj28IR8iZ4Q==;70","i1":"PDDlRv6kSTY=;71","i2":"37Abs+7NORA+aw==;72","i3":"nYnNn/h7oliS0g==;73","i4":"taa2iUZQTU3clg==;74","i5":"pnOU8sqqq+yfAw==;75","z1":"u2aJ3jyPFuyPLbvcs4JkSG76yZ6hWeS7lxfM8BryujLFu0AaGRmrJPBXfG73JeE0udXFhcieqY8SQM+rIV2Uxg==;76","z2":"7+NN69jiB4WEtKFHQUFslKANMEQHGWKhFMMUFpiuqkttAaCGV3f1njC0aSJG5KkOJfyw6F8ZYC66tnjJCyw2Xg==;77","y2":"hpWUPHODOODnvw==;78","y3":"Mcd6Z7EcXbqriQ==;79","y6":"FYZjDE2gS09Zpw==;80","y8":"bgxzREp92oOAtQ==;81","x4":"vZTy8TmDRbLVsA==;82","z5":"AF0tetpBK+Y=;83","z4":"ra4HllvMU6x2Mg==;84","z6":"lCkjsx1F7o9MGv9O;85","z7":"+mydYCDyYiWHVnUL;86","z8":"wyBmEDIJOm9rEZ5YoyE=;87","z9":"9G0vCz03PLYHflWN;88","y1":"hvCuEOQS8QnHHHXd;89","y4":"FNpKkY79+8rVB2Yu;90","y5":"ilscBl+nD/LoTa/wnS4=;91","y7":"eIq0SNGd0dQIqUdT;92","y9":"FyS4UOsX1s/B/ok5S0g=;93","y10":"9M9DH0vPmC5CUFVnGBY=;94","x1":"fCKRhDigf+Vpj/TY;95","x2":"7kCaSIar1h2dwK2OPXE=;96","x3":"wiz1HB8ClFJ2uA/+;97","x5":"cW/28YETmtEj+XRZ;98","z3":"xKbmxvCzSVmQcFUmCw7S6wkOWQbNV+i5u1MdkfnjNLw=;99","v":"6.3.1","pgrdt":"vrD7vxFc7t3n2ksFo3p4TmpHZEs=;100","pgrd":"ekZGN91gC6VDOPAD2oSFYO5uE1vXlr0WkOLhLYABIx7dpb5/Bv+IIL3I0Pkx9Fo6lUkGb4sOx9jqOo6A+EY/DSROLn8kEIq737EQMmP8oy8vsxI8lMFf8gaS4xWEOidyDZUpZmFkRcvYbskXzKDn+USglFNYgu7yH7auls51r2bD8ouItWX2JKhyFbNY4t5nQvV4TBAdp0AFascSvc6v1iqpKyo="}',
    }

    json_data = {
        'price_to': price,
        'section': 'used',
        'category': 'cars',
        'sort': 'cr_date-desc',
        'output_type': 'list',
        'geo_radius': 100,
        'geo_id': [
            48,
        ],
    }

    response = requests.post('https://auto.ru/-/ajax/desktop/listing/', cookies=cookies, headers=headers,
                             json=json_data).json()

    return response

def add_car(car):
    global getcars
    if car.get('services')==[]:
        pass
    else:
        return False
    carid = car.get('saleId')
    if carsId.count(carid)>0:
        return True

    document = car.get('documents')
    owner_count = document.get('owners_number')
    year = document.get('year')
    if (document.get('pts_original')):
        pts = 'Оринигал'
    else:
        pts='Дубликат'
    time = car.get('additional_info').get('hot_info').get('start_time')
    price = car.get('price_info').get('RUR')
    location = car.get('seller').get('location')
    address = location.get('address')
    region_info = location.get('region_info').get('name')
    mileage = car.get('state').get('mileage')
    vehicle_info = car.get('vehicle_info')
    mark_info = vehicle_info.get('mark_info').get('name')
    mark=vehicle_info.get('mark_info').get('code')
    model_info = vehicle_info.get('model_info').get('name')
    model = vehicle_info.get('model_info').get('code')
    generation = vehicle_info.get('super_gen').get('name')
    car=f"{mark_info} {model_info} {generation}"
    url = f'https://auto.ru/cars/used/sale/{mark}/{model}/{carid}'

    carsId.append(carid)
    if not first :
        getcars.append({"carid": carid,
                    'url': url,
                    'time': time,
                    'car':car,
                    'owner_count': owner_count,
                    'pts': pts,
                    'year': year,
                    'mileage': mileage,
                    'price': price,
                    'address': address,
                    'region_info': region_info})
    return False

def getdata():
    global getcars,first
    response= getresponse()
    cars= response.get('offers')
    bol=False
    for car in cars:
        bol=add_car(car)
        if bol:
            break
    first=False
    return getcars



def main():
    getdata()

if __name__ == '__main__':
    main()