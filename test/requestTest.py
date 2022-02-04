import requests

files = {'file': ('picture.jpg', open('../asserts/1.jpg', 'rb'), 'image/jpeg')}
r = requests.post("http://127.0.0.1:8000/api/v1/pictures", files=files)
print(r.text)
