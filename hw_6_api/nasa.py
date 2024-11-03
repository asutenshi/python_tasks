import requests

API_KEY = 'DEMO_KEY'
print('Фотография Земли из космоса')
print('Для ввода доступны даты начиная с 2015-06-17')
date = input('Введите дату в формате YYYY-MM-DD: ')

response = requests.get(f'https://api.nasa.gov/EPIC/api/enhanced/date/{date}?api_key={API_KEY}')

img_id = ''
json = response.json()

if response.status_code == 200 and json:
    img_id = json[0]['image']
else:
    print('Не удалось получить изображение')

url = f'https://api.nasa.gov/EPIC/archive/enhanced/{date[0:4]}/{date[5:7]}/{date[8:]}/png/{img_id}.png?api_key={API_KEY}'

response = requests.get(url)
json = response.json()
if response.status_code == 200 and json:
    print(f'Для просмотра фотографии перейдите по ссылке: {url}')
else:
    print('Не удалось скачать изображение')
