from bs4 import BeautifulSoup
from pycoingecko import CoinGeckoAPI
from datetime import datetime
import json

cg = CoinGeckoAPI()
time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Get all info for top 50 coins
coins = cg.get_coins()

# Update decoder file with coin symbols/names
with open('decoder.txt', 'r+') as file:
    old_codes = json.load(file)        
    new_codes = {coin['symbol']: coin['id'] for coin in coins}   
    json.dump({**old_codes, **new_codes}, file)

# Get current prices for top 50 coins in USD
current_prices_usd = {coin['symbol']: coin['market_data']['current_price']['usd'] for coin in coins}

# Dump current price data
with open('prices.txt', 'a') as file:
    file.write('\n')
    json.dump({time: current_prices_usd}, file)