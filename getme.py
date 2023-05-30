import requests
from settings import TOKEN

URL = f'https://api.telegram.org/bot{TOKEN}/getMe'

response = requests.get(URL)

if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code)
    print(response.text)
