from coinmarketcapapi import CoinMarketCapAPI

cmc = CoinMarketCapAPI(debug=True)

rep = cmc.cryptocurrency_info(symbol='BTC')

print(rep.data["BTC"]["logo"])
