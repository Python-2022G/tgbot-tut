import requests
from settings import TOKEN

URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'

chat_id = 1258594598

params = {
    'chat_id': chat_id, 
    'photo': 'https://images.unsplash.com/photo-1554080353-a576cf803bda?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80'
}

response = requests.get(URL, params=params)

    