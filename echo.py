import requests
import time
from settings import TOKEN


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


def main():
    last_update_id = 0

    while True:
        curr_update = get_last_update()

        if last_update_id != curr_update['update_id']:

            text = curr_update['message']['text']
            chat_id = curr_update['message']['chat']['id']

            send_message(chat_id, text)

            last_update_id = curr_update['update_id'] 

        time.sleep(1)

main()
