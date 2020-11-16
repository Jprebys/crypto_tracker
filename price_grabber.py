from bs4 import BeautifulSoup
from pycoingecko import CoinGeckoAPI
from datetime import datetime
import json

cg = CoinGeckoAPI()
time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

current_prices_usd = {coin['id']: coin['market_data']['current_price']['usd'] for coin in cg.get_coins()}

with open('./prices.txt', 'a') as file:
    file.write('\n')
    json.dump({time: current_prices_usd}, file)