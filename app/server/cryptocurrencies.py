import requests as req
from config import API_KEY


def cryptocurrencies_request():
    url_list = 'https://min-api.cryptocompare.com/data/blockchain/list'

    response = req.get(url_list, params={'api_key': API_KEY})
    data = response.json()
    cryptocurrencies = data.get('Data', [])
    if cryptocurrencies:
        return cryptocurrencies
    else:
        return f'error'


def crypto_price(cryptocurrency):
    url_price = f'https://min-api.cryptocompare.com/data/price?fsym={cryptocurrency}&tsyms=USD,JPY,EUR&api_key={API_KEY}'
    response = req.get(url_price)
    response.raise_for_status()
    data = response.json()
    if data:
        price_usd = data.get('USD')
        return price_usd
    else:
        return f"No data available for {cryptocurrency}"
