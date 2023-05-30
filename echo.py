import requests
from settings import TOKEN

url_for_getupdates = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(url_for_getupdates)

updates = response.json()['result']
last_update = updates[-1]

text = last_update['message']['text']
chat_id = last_update['message']['chat']['id']

print(chat_id, text)

url_for_sendmessage = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

params = {
    'chat_id': chat_id,
    'text': text
}
    
response = requests.get(url_for_sendmessage, params=params)

