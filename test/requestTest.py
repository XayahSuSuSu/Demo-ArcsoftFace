import datetime
import time

import requests


def picture():
    files = {'file': ('picture.jpg', open('../asserts/1.jpg', 'rb'), 'image/jpeg')}
    r = requests.post("http://127.0.0.1:8000/api/v1/pictures", files=files)
    print(r.text)


def face():
    start = time.time()
    files = {'file': ('picture.jpg', open('../asserts/2.jpg', 'rb'), 'image/jpeg')}
    r = requests.post("http://127.0.0.1:8000/api/v1/face", files=files)
    end = time.time()
    print(r.text)
    print("耗时：{}ms".format(
        (datetime.datetime.fromtimestamp(start) - datetime.datetime.fromtimestamp(end)).microseconds / 1000))


# picture()
face()
