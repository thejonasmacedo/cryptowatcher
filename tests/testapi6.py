import requests

url = "http://pro-api.coinmarketcap.com/v1/"

api_key = "92b817f3-e5e2-4bbd-85ba-622c7cc3c40a"

headers = {
	'Accepts': 'application/json',
	'X-CMC_PRO_API_KEY': '92b817f3-e5e2-4bbd-85ba-622c7cc3c40a'
}

parameters = {
	'symbol': 'BTC',	# cryptocurrency symbol
	'interval': 'monthly',	# monthy interval
	'count': '12'		# periods (months)
}

response = requests.get(f'{url}cryptocurrency/quotes/historical', headers=headers, params=parameters)

print(f'Status da resposta: {response.status_code}')

content = response.text

print(content)
