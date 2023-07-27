

# import the libraries

import yfinance as yf
import mplfinance as mpf
import ta

import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime as dt
import pandas as pd
import numpy as np

from datetime import datetime


# https://sparkbyexamples.com/pandas/pandas-convert-datetime-to-string-format/


print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")


df = yf.Ticker('^GSPC').history(start='2023-06-01', interval='1h')
print(df.dtypes)
print(df.tail())

print("**********0000000000000000000000000000000*******************")

df.index = df.index.tz_localize(None)
#df.reset_index(inplace = True)
print(df.dtypes)
print(df.tail())


# df.style.format({'Datetime': lambda t: t.strftime("%d/%m/%Y")})

print("**********-111111111111111111111111111*******************")

#df.Datetime = df.Datetime.strftime("%m/%d/%Y, %H:%M:%S")
df.index=df.index.astype(str) # Help link # https://sparkbyexamples.com/pandas/pandas-convert-datetime-to-string-format/
df.reset_index(inplace = True)

print(df.dtypes)
print(df.tail())

print("**********2222222222222222222222222222******************")







df = df.set_index('Datetime')


df.index = pd.to_datetime(df.index.astype('datetime64[ns]'))
#df["Datetime"] = pd.to_datetime(df["Datetime"])
print(df.dtypes)
print(df.tail())



print("**********3333333333333333333333333333******************")



df.reset_index(inplace = True)

print(df.dtypes)
print(df.tail())










