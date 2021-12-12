import random
import time
import requests
from fake_useragent import UserAgent
import threading


ua = UserAgent()
headers = dict()
proxies = dict()
i=0
with open('available_proxies.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    while True:
        headers['User-Agent'] = ua.random
        rand = random.randint(0,45)
        proxies = {'http': lines[rand]}
        time_start = time.time()
        try:
            requests.get('http://20.212.155.150/', proxies=proxies, headers=headers, timeout=0.6)
        except:
            pass
