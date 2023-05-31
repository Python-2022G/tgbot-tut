import requests
from settings import TOKEN

URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'

chat_id = 1258594598

def send_photo_by_url(chat_id, url):
    params = {
        'chat_id': chat_id, 
        'photo': url
    }
    
    response = requests.get(URL, params=params)
    return response

def send_photo_by_file(chat_id, file):
    params = {
        'chat_id': chat_id, 
    }
    
    files = {
        'photo': open(file, 'rb')
    }
    
    response = requests.post(URL, params=params, files=files)
    return response

# igm_url = 'https://images.unsplash.com/photo-1554080353-a576cf803bda?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80'
# response = send_photo_by_url(chat_id, igm_url)

file = 'image.jpg'
response = send_photo_by_file(chat_id, file)
