import inspect
import pandas as pd
import json
from pprint import pprint
from utils import *

from config import *

from kotak_api import KotakAPI

import neo_api_client

# print(n)

# print(current_time())
# print(is_market_open())
# print(is_entry_time())
# print(is_exit_time())
# print(is_expiry_day())
# print(round_to_strike(25123))

api = KotakAPI()
response = api.login()
# url = api.get_script_master(exchange_segment="nse_cm")
# df = pd.read_csv(url)
# print(df.head())
# print(df.columns)

index_detals =  api.get_spot_price()
spot_price = float(index_detals[0]["ltp"])


# print(index_detals)
# print(dir(api.client))
import inspect

print([m for m in dir(api.client) if "history" in m.lower()])
print([m for m in dir(api.client) if "candle" in m.lower()])
print([m for m in dir(api.client) if "ohlc" in m.lower()])

# stock = api.client.search_scrip(
#     exchange_segment="nse_cm",
#     symbol="RELIANCE"
# )

# instrument = [{
#     "exchange_segment": "nse_cm",
#     "instrument_token": "Nifty 50"
# }]

# print(api.client.quotes(
#     instrument_tokens=instrument,
#     # quote_type="ohlc"
#     quote_type="scrip_details"
# ))





# script_name = api.client.search_scrip(exchange_segment=config.EXCHANGE_SEGMENT, symbol=config.SYMBOL) # search app script 
# print(json.dumps(script_name, indent=4))# print(response)
# pprint.pprint(script_name)
# print(script_name)
print("bot started successfully")




