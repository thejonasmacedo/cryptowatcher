
import requests
import time
from os import system

symbol = 'BTCUSD'
base_url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
intervalo = '1m'

total_requests = 20

delay_ms = 1000//total_requests

response = requests.get(base_url)
print(f'price: {response.content}')
time.sleep(delay_ms / 1000)

#system('clear')


