import requests

crypto = 'BTC'
fiat = 'USD'

symbol = crypto + fiat

priceConvert = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
	
