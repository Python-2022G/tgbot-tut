import requests
from settings import TOKEN

URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

chat_id = 1258594598
text = 'Hello, world!'

btn1 = 'Button 1'
btn2 = 'Button 2'
btn3 = 'Button 3'

keyboard = [
    [btn1, btn2],
    [btn3]
]

params = {
    'chat_id': chat_id,
    'text': text,
    'reply_markup': {
        'keyboard': keyboard
    }
}

response = requests.post(URL, json=params)
