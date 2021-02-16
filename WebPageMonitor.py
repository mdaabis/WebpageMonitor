import requests
import threading
import hashlib
from urllib.request import urlopen
from twilio.rest import Client
from decouple import config
import smtplib



URL = 'https://www.bbc.co.uk/sport/live/football/54074356'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
current_hash = hashlib.sha224(urlopen(URL).read()).hexdigest()
sender = 'SENDER EMAIL'
password = 'SENDER_PASSWORD'
recipient = 'RECIPIENT EMAIL'
message = 'Page changed'

def monitor():
    threading.Timer(5, monitor).start() #The number in the Timer() bracket represents the scheduling interval in seconds. Keep to 1 second and above to prevent memory errors
    response = urlopen(URL).read()
    new_hash = hashlib.sha224(response).hexdigest()
    global current_hash
    if(current_hash != new_hash):
        print(current_hash)
        print(new_hash)
        send_notification()
        current_hash = new_hash

def send_notification():
    server = smtplib.SMTP('64.233.184.108')
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, message)
    print('Email Sent')

monitor()
