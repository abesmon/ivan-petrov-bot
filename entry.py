# -*- coding: utf-8 -*- 

import random

import requests

def point(event, context):
    print(event)
    if event["message"]["text"][0] == "/":
        words = event["message"]["text"].split()
        command = words[0][1:]
        if command == "echo":
            send_message(event["message"]["from"]["id"], event["message"]["text"])
        elif command == "help":
            help_text = "Это вспомогательный текст. Здесь будет написано что и как со мной можно сделать"
            send_message(event["message"]["from"]["id"], help_text)
        elif command == "joke":
            JOKES_DICT = [
                "Шутка1",
                "Шутка2",
                "Шутка3"
            ]
            send_message(event["message"]["from"]["id"], random.choice(JOKES_DICT))
        else:
            send_message(event["message"]["from"]["id"], "Я не знаю эту команду")
    else:
        send_message(event["message"]["from"]["id"], "Введите команду")
    

def send_message(chat_id, text):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token="token",
        method="sendMessage"
    )
    data = {
        "chat_id": chat_id,
        "text": text
    }
    r = requests.post(url, data = data)
    print(r.json())

"""
def start_request():
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token="token",
        method="setWebhook"
    )
    data = {
        "url": "https://hs5s3yt90k.execute-api.us-west-2.amazonaws.com/v0/bot_handler"
    }
    r = requests.post(url, data = data)
    print(r.json())

if __name__ == "__main__":
    start_request()
"""