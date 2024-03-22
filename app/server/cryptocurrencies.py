import requests as req
from config import API_KEY


URL = 'https://min-api.cryptocompare.com/data/'

def cryptocurrencies_request():
    url_list = f'{URL}blockchain/list'

    response = req.get(url_list, params={'api_key': API_KEY})
    if response.status_code == 200:
        data = response.json()
        cryptocurrencies = data.get('Data', [])
        
        return cryptocurrencies
    else:
        raise Exception(response.status_code)

def crypto_price(cryptocurrency):
    url_price = f'{URL}price?fsym={cryptocurrency}&tsyms=USD,JPY,EUR&api_key={API_KEY}'
    response = req.get(url_price)
    if response.status_code == 200:
        response.raise_for_status()
        data = response.json()
    else:
        return f"No data available for {cryptocurrency}"
