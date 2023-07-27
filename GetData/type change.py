

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



timestamp =  45110.29167
date_time = datetime.fromtimestamp(timestamp)
print(date_time)
# date_time = datetime.fromordinal(timestamp)
# print(date_time)
# date_time = datetime.fromisocalendar(timestamp)
# print(date_time)
# date_time = datetime.fromisoformat(timestamp)
# print(date_time)


# from datetime import datetime

# now = datetime.now() # current date and time

# year = now.strftime("%Y")
# print("year:", year)

# month = now.strftime("%m")
# print("month:", month)

# day = now.strftime("%d")
# print("day:", day)

# time = now.strftime("%H:%M:%S")
# print("time:", time)

# date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
# print("date and time:",date_time)




# from datetime import datetime

# timestamp = 1528797322
# date_time = datetime.fromtimestamp(timestamp)

# print("Date time object:", date_time)

# d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
# print("Output 2:", d)	

# d = date_time.strftime("%d %b, %Y")
# print("Output 3:", d)

# d = date_time.strftime("%d %B, %Y")
# print("Output 4:", d)

# d = date_time.strftime("%I%p")
# print("Output 5:", d)












# # Below are quick example
# # Convert datetype to string
# df['ConvertedDate']=df['DateTypeCol'].astype(str)

# # Using to_datetime() & astype()
# df['ConvertedDate']=pd.to_datetime(df['DateTypeCol'].astype(str), format='%Y/%m/%d')

# # Conver DataTime to Different Format
# df['ConvertedDate'] = df['DateTypeCol'].dt.strftime('%m/%d/%Y')

# # Using DataFrame.style.format() and lambda function
# df.style.format({"DateTypeCol": lambda t: t.strftime("%d/%m/%Y")})

# # Convert multiple date columns to string type
# date_columns = ["date_col1","date_col2","date_col3"]
# df[date_columns] = df[date_columns].astype(str)

# # Convert all date columns to string type
# for col in  df.select_dtypes(include=['datetime64']).columns.tolist():
#     df[col] = df[col].astype(str)

# # Convert all date columns to string type
# date_columns = df.select_dtypes(include=['datetime64']).columns.tolist()
# df[date_columns] = df[date_columns].astype(str)











# # Create a DataFrame.

# import pandas as pd
# technologies = ({
#     'Courses':["Spark","PySpark","Hadoop"],
#     'Fee' :[22000,25000,23000],
#     'InsertedDate':["2021/11/24","2021/11/25","2021/11/26"]
#                })
# df = pd.DataFrame(technologies)
# # Use pandas.to_datetime() to change datetime format
# df['DateTypeCol'] = pd.to_datetime(df.InsertedDate)
# print(df)

# # Convert datetype to string
# df['ConvertedDate']=df['DateTypeCol'].astype(str)
# print(df)

# # Using to_datetime()  & astype()
# df['ConvertedDate']=pd.to_datetime(df['DateTypeCol'].astype(str), format='%Y/%m/%d')
# print(df)

# # change in date time format
# df['ConvertedDate'] = df['DateTypeCol'].dt.strftime('%m/%d/%Y')
# print(df)

# # Using DataFrame.style.format() and lambda function
# df.style.format({"DateTypeCol": lambda t: t.strftime("%d/%m/%Y")})
# print(df)

# # Convert all date columns to string type
# date_columns = df.select_dtypes(include=['datetime64']).columns.tolist()
# df[date_columns] = df[date_columns].astype(str)






print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")


df = yf.Ticker('^GSPC').history(start='2023-06-01', interval='1h')
print(df.dtypes)
print(df.tail())

print("**********0000000000000000000000000000000*******************")

df.index = df.index.tz_localize(None)
df.reset_index(inplace = True)
print(df.dtypes)
print(df.tail())


# df.style.format({'Datetime': lambda t: t.strftime("%d/%m/%Y")})

print("**********-111111111111111111111111111*******************")

#df.Datetime = df.Datetime.strftime("%m/%d/%Y, %H:%M:%S")
df['Datetime']=df['Datetime'].astype(str)


print(df.dtypes)
print(df.tail())

print("**********2222222222222222222222222222******************")


df["Datetime"] = pd.to_datetime(df["Datetime"].astype('datetime64[ns]'))
#df["Datetime"] = pd.to_datetime(df["Datetime"])
print(df.dtypes)
print(df.tail())


















