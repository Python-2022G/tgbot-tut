import requests
import time
from settings import TOKEN

def start(chat_id, first_name):
    url_for_sendmessage = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    params = {
        'chat_id': chat_id,
        'text': f'Hello *{first_name}*, I am echo bot',
        'parse_mode': 'MarkdownV2'
    }
    
    response = requests.get(url_for_sendmessage, params=params)
    return response

def get_last_update():
    url_for_getupdates = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

    response = requests.get(url_for_getupdates)

    updates = response.json()['result']
    last_update = updates[-1]

    return last_update

def send_message(chat_id, text):
    url_for_sendmessage = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    
    params = {
        'chat_id': chat_id,
        'text': text
    }
    
    response = requests.get(url_for_sendmessage, params=params)
    return response

def send_photo(chat_id, file_id):
    url_for_sendphoto = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    
    params = {
        'chat_id': chat_id,
        'photo': file_id,
        'caption': 'siz yuborgan rasmingiz',
    }
    
    response = requests.get(url_for_sendphoto, params=params)
    return response

def main():
    last_update_id = 0

    while True:
        curr_update = get_last_update()

        if last_update_id != curr_update['update_id']:
            chat_id = curr_update['message']['chat']['id']

            if 'text' in curr_update['message'].keys():
                text = curr_update['message']['text']
                
                if text == '/start':
                    first_name = curr_update['message']['chat']['first_name']
                    start(chat_id, first_name)
                else:
                    send_message(chat_id, text)
            
            elif 'photo' in curr_update['message'].keys():
                photo = curr_update['message']['photo'][-1]
                file_id = photo['file_id']
                send_photo(chat_id, file_id)

            last_update_id = curr_update['update_id'] 

        time.sleep(1)

main()
