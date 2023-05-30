import requests, time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from os import system
from time import sleep

symbol = 'BTCUSDT'
base_url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
interval = '1s'
total_requests = 20

graph_prices = []

for request in range(total_requests):
	response = requests.get(base_url)
	price = response.json()
	
	graph_prices.append(price)
	
	plt.plot(graph_prices)
	plt.xlabel('BTC to USDT lapse of time since open')
	
	sleep(1)
