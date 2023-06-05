import requests
from settings import TOKEN

URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

chat_id = 1258594598
text = 'Hello, world!'

btn1 = {
    'text': 'Button 1',
    'request_contact': True
}
btn2 = {
    'text': 'Button 2',
    'request_location': True
}

keyboard = [
    [btn1]
]

params = {
    'chat_id': chat_id,
    'text': text,
    'reply_markup': {
        'keyboard': keyboard
    }
}

response = requests.post(URL, json=params)
