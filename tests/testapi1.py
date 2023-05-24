from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

#parameters = {
#	'start':'1',
#	'limit':'5000',
#	'convert':'USD',
#}

parameters = {

    "data": [
        {
            "id": 1,
            "name": "Bitcoin",
            "symbol": "BTC",
            # "slug": "bitcoin",
            # "cmc_rank": 5,
            # "num_market_pairs": 500,
            # "circulating_supply": 16950100,
            # "total_supply": 16950100,
            # "max_supply": 21000000,
            "infinite_supply": False,
            # "last_updated": "2018-06-02T22:51:28.209Z",
            # "date_added": "2013-04-28T00:00:00.000Z",
		}]
	}

headers = {
	'Accepts': 'application/json',
	'X-CMC_PRO_API_KEY': '92b817f3-e5e2-4bbd-85ba-622c7cc3c40a',
		}


session = Session()
session.headers.update(headers)

try:
	response = session.get(url, params=parameters)
	data = json.loads(response.text)
	print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
	print(e)
