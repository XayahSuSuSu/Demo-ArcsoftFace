import time

import requests
from numpy import mean


def picture():
    files = {'file': ('picture.jpg', open('../asserts/1.jpg', 'rb'), 'image/jpeg')}
    form = {
        'name': '赵美延'
    }
    r = requests.post("http://127.0.0.1:3308/api/v1/pictures", data=form, files=files)
    print(r.text)


def face():
    start = time.time()
    files = {'file': ('picture.jpg', open('../asserts/2.jpg', 'rb'), 'image/jpeg')}
    r = requests.post("http://127.0.0.1:3308/api/v1/face", files=files)
    end = time.time()
    print(r.text)
    # print("耗时：{}".format(end - start))
    return end - start


# picture()
average = []
for i in range(1):
    average.append(face())
print("调试次数：{}，平均耗时：{}".format(len(average), mean(average)))
