import requests
from settings import TOKEN

URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

chat_id = 1258594598
text = 'Hello, world!'

params = {
    'chat_id': chat_id, 
    'text': text
}

response = requests.get(URL, params=params)

    