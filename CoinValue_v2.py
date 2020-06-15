# Coin Value Program
# Haoyuan Gao
# June 15, 2020

import requests
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

def get_info (symbol):
  web = f"https://api.binance.com/api/v3/klines?symbol={symbol}USDT&interval=1d"
  coin_info = requests.get(web)
  json_coin = coin_info.json() # create a list of information from the source
  opening_price = []
  max_price = []
  min_price = []
  closing_price = []
  closing_time = []
  for i in range (len(json_coin)):
    opening_price.append(float(json_coin[i][1])) # get opening price                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ning price
    max_price.append(float(json_coin[i][2])) # get maxium price
    min_price.append(float(json_coin[i][3])) # get minium price
    closing_price.append(float(json_coin[i][4])) # get closing price
    time_converted = pd.to_datetime(json_coin[i][6],unit='ms') # convert to timestamp format
    closing_time.append(time_converted) # get closing time
  df = {"Opening Price":opening_price,"Maxium Price":max_price,"Minium Price":min_price,"Closing Price":closing_price,"Closing Time":closing_time}
  output = pd.DataFrame(df)
  return output

def drawing (coin,symbol): # draw a graph for one coin with closing price
  plt.plot(coin["Closing Time"],coin["Closing Price"],label=symbol)

def integrate (symbols,results): # integrate multiple graphs
  for i in range (len(symbols)):
      drawing(results[i],symbols[i])
  plt.xlabel("Time")
  plt.ylabel("Closing Price (USD)")
  plt.legend()
  plt.show()

def drawing_multi (coin,symbol): # draw a graph for one coin containing multiple information
  plt.plot(coin["Closing Time"],coin["Opening Price"],label="Opening Price")
  plt.plot(coin["Closing Time"],coin["Closing Price"],label="Closing Price")
  plt.plot(coin["Closing Time"],coin["Maxium Price"],label="Maxium Price")
  plt.plot(coin["Closing Time"],coin["Minium Price"],label="Minium Price")
  plt.xlabel("Time")
  plt.ylabel(f"{symbol} Price (USD)")
  plt.legend()
  plt.show()

symbols = ["ETH","BNB","TRX","BCH","EOS","XRP","LTC"] # create a list for all the coins needed
results = [get_info(symbol) for symbol in symbols]

# example
integrate(symbols,results)
drawing_multi(results[0],"ETH")
