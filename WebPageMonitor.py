import requests
import threading
import hashlib
from urllib.request import urlopen
from twilio.rest import Client
from decouple import config



URL = 'https://www.bbc.co.uk/sport/live/football/55864099'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
current_hash = hashlib.sha224(urlopen(URL).read()).hexdigest()

def monitor():
    threading.Timer(3, monitor).start() #The number in the Timer() bracket represents the scheduling interval in seconds
    response = urlopen(URL).read()
    new_hash = hashlib.sha224(response).hexdigest()
    global current_hash
    if(current_hash != new_hash):
        send_notification()
        current_hash = new_hash

def send_notification():
    account_sid = config("TWILIO_ACCOUNT_SID")
    auth_token = config("TWILIO_AUTH_TOKEN")

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to = config('TO_NUMBER'),
        from_ = config('FROM_NUMBER'),
        body = 'Page has changed'
    )

monitor()
