import requests
from settings import TOKEN

URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

chat_id = 1258594598
text = 'Hey'


inline_btn1 = {
    'text': 'Google',
    'url': 'https://google.com'
}
inline_btn2 = {
    'text': 'Youtube',
    'url': 'https://youtube.com'
}

inline_keyboard = [
    [inline_btn1],
    [inline_btn2]
]

params = {
    'chat_id': chat_id,
    'text': text,
    'reply_markup': {
        'inline_keyboard': inline_keyboard
    }
}

response = requests.post(URL, json=params)
