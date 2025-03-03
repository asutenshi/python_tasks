import requests
import re

def wl(account_id):
    URL = f'https://api.opendota.com/api/players/{account_id}/wl'
    req = requests.get(URL)
    if (req.status_code == 200):
        stats = req.json()
        print(stats)
    else:
        print('Ошибка при поиске игрока')


inp = input('Введите Steam32 account ID (xxxxxxxxx): ')
pattern = r'^\d{9}$'

if re.match(pattern, inp):
    wl(int(inp))
else:
    print('Неправильно введен Steam32 ID')
