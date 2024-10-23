import requests

API_KEY = '3287a4d67ca464c9eefc402211b413ff'
print('Программа для вывода погоды с OpenWeatherMap')
city = input('Введите название города с большой буквы на русском языке: ')

response = requests.get('https://api.openweathermap.org/data/2.5/weather', params={'lang':'ru', 'q':city, 'units':'metric' 'appid':API_KEY})

if response.status_code == 200:
    json = response.json()
    weather = json['weather'][0]['description']
    temp = json['main']['temp']
    feels_like = json['main']['feels_like']
    humidity = json['main']['humidity']
    wind_speed = json['wind']['speed']

else: print('Неправильно введён город')