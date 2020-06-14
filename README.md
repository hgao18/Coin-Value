# Coin-Value
Get coin value information online and draw graphs.

Python code list below；

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
    opening_price.append(float(json_coin[i][1])) # get opening price                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    max_price.append(float(json_coin[i][2])) # get maxium price
    min_price.append(float(json_coin[i][3])) # get minium price
    closing_price.append(float(json_coin[i][4])) # get closing price
    time_converted = pd.to_datetime(json_coin[i][6],unit='ms') # convert to timestamp format
    closing_time.append(time_converted) # get closing time
  return opening_price,max_price,min_price,closing_price,closing_time

def output (symbol,results):
  for i in range (len(symbols)):
    if symbol == symbols[i]:
      index = i
      break
  df = {"Opening Price":results[index][0],"Maxium Price":results[index][1],"Minium Price":results[index][2],"Closing Price":results[index][3],"Closing Time":results[index][4]}
  output = pd.DataFrame(df)
  return output

def drawing (coin,symbol): # draw graph with closing price
  plt.plot(coin["Closing Time"],coin["Closing Price"],label=symbol)

def integrate (coins,symbols): # integrate multiple graphs
  if len(coins) == len(symbols):
    for i in range (len(coins)):
      drawing(coins[i],symbols[i])
  plt.xlabel("Time")
  plt.ylabel("Closing Price (USD)")
  plt.legend()
  plt.show()

def drawing_only (coin,symbol):
  plt.plot(coin["Closing Time"],coin["Opening Price"],label="Opening Price")
  plt.plot(coin["Closing Time"],coin["Closing Price"],label="Closing Price")
  plt.plot(coin["Closing Time"],coin["Maxium Price"],label="Maxium Price")
  plt.plot(coin["Closing Time"],coin["Minium Price"],label="Minium Price")
  plt.xlabel("Time")
  plt.ylabel(f"{symbol} Price (USD)")
  plt.legend()
  plt.show()

symbols = ["ETH","BNB","TRX","BCH","EOS","XRP","LTC"]
results = [get_info(symbol) for symbol in symbols]
ETH = output("ETH",results)
BNB = output("BNB",results)
TRX = output("TRX",results)
BCH = output("BCH",results)
EOS = output("EOS",results)
XRP = output("XRP",results)
LTC = output("LTC",results)
coins = [ETH,BNB,TRX,BCH,EOS,XRP,LTC]

# example
integrate(coins,symbols)
drawing_only(BTC,"BTC")
