import requests
import time
from os import system

symbol = 'BTCUSDT'
base_url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
intervalo = '1m'

total_requests = 20

delay_ms = 1000//total_requests

for request in range(total_requests):
        response = requests.get(base_url)
        price = response.json()

        print(f"price: {price['price']}")
        time.sleep(1)

        system('clear')

