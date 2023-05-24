import requests

# URL base da API do CoinMarketCap
base_url = "https://api.coinmarketcap.com/data/v1/"

# Exemplo de solicitação para obter os dados de uma criptomoeda específica
cryptocurrency_id = "bitcoin"
url = f"{base_url}cryptocurrency/{cryptocurrency_id}"

# Fazendo a solicitação GET à API
response = requests.get(url)

# Verificando se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    data = response.json()  # Obtendo os dados da resposta em formato JSON
    # Aqui você pode processar e utilizar os dados recebidos como desejar
else:
    print("Falha na solicitação. Código de status:", response.status_code)