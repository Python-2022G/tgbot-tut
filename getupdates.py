import requests
from settings import TOKEN

URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(URL)

if response.status_code == 200:
    updates = response.json()['result']
    last_update = updates[-1]

    text = last_update['message']['text']
    chat_id = last_update['message']['chat']['id']

    print(chat_id, text)
    