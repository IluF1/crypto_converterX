import requests as req
from config import API_KEY

def cryptocurrencies_request():
    url = f'https://api.cryptorank.io/v1/currencies?api_key={API_KEY}'
    response = req.get(url)

    if response.status_code == 200:
        data = response.json()
        cryptocurrencies = [currency['name'] for currency in data['data']]
        return cryptocurrencies
    else:
        return f"Failed to fetch data. Status code: {response.status_code}"
