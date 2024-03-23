import datetime as dt
import pandas as pd
import numpy as np
import openpyxl



def fun (filePath_fun, bookName = "Yahoo 1m") :

    # Set Variable    
    intraDayList = ['Yahoo Hours','Yahoo 30m','Yahoo 15m','Yahoo 5m','Yahoo 2m','Yahoo 1m']
    swingDayList = ['Yahoo Dayes']
    
    # Import  data
    #------------------------------------------------  
    book = openpyxl.load_workbook(filePath_fun)
    sheet = book[bookName]
    df= pd.DataFrame(sheet.values)


    # format  data
    #------------------------------------------------  
    #Convert row to column header for Pandas DataFrame : Link https://stackoverflow.com/questions/26147180/convert-row-to-column-header-for-pandas-dataframe
    df.columns = df.iloc[0]
    df = df.drop(0)

    #change object to datetime64[ns]
    if (bookName in intraDayList):
        df.Datetime = pd.to_datetime(df.Datetime.astype('datetime64[ns]'))
        df = df.set_index('Datetime')
    elif (bookName in swingDayList):
        df.Date = pd.to_datetime(df.Date.astype('datetime64[ns]'))
        df = df.set_index('Date')

    #change object to float
    # Link https://stackoverflow.com/questions/36814100/pandas-to-numeric-for-multiple-columns
    cols = df.columns
    df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')


    return df





def fun2 (filePath_fun, bookName = 'IBKR 1m') :

    # Set Variable    
    intraDayList = ['IBKR 1s','IBKR 5s','IBKR 10s','IBKR 15s','IBKR 30s',
                    'IBKR 1m','IBKR 2m','IBKR 3m','IBKR 5m','IBKR 10m','IBKR 15m','IBKR 20m','IBKR 30m',
                    'IBKR 1H','IBKR 2H','IBKR 3H','IBKR 4H','IBKR 8H' ]
    swingDayList = ['IBKR 1Day','IBKR 1week','IBKR 1Month']
    
    # Import  data
    #------------------------------------------------  
    book = openpyxl.load_workbook(filePath_fun)
    sheet = book[bookName]
    df= pd.DataFrame(sheet.values)


    # format  data
    #------------------------------------------------  
    #Convert row to column header for Pandas DataFrame : Link https://stackoverflow.com/questions/26147180/convert-row-to-column-header-for-pandas-dataframe
    df.columns = df.iloc[0]
    df = df.drop(0)

    #change object to datetime64[ns]
    if (bookName in intraDayList):
        df.Datetime = df.Datetime.str.replace("US/Eastern", "")
        df.Datetime = pd.to_datetime(df.Datetime.astype('datetime64[ns]'))
        df = df.set_index('Datetime')
    elif (bookName in swingDayList):
        df.Datetime = pd.to_datetime(df.Datetime.astype('datetime64[ns]'))
        df = df.set_index('Datetime')

    #change object to float
    # Link https://stackoverflow.com/questions/36814100/pandas-to-numeric-for-multiple-columns
    cols = df.columns
    df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')


    return df







