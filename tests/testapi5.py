import coinmarketcapapi
import os

api_key = '92b817f3-e5e2-4bbd-85ba-622c7cc3c40a'
cmc_client = coinmarketcapapi.CoinMarketCapAPI(api_key)

response = cmc_client.cryptocurrency_info(symbol = 'BTC')
print(response.data['BTC'])
