

import pandas as pd
import yfinance as yf
import openpyxl
import os


#------------------------------------------------

def fun(        ticker = 'goog',
                filePath = r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\def ", 
                sheetName = 'Yahoo News'
):
    # Set Varibles
    #------------------------------------------------     
        filePathTicker = filePath + ticker + ".xlsx"
        filePathTemp = filePath + " Temp " + ".xlsx"
        book  = openpyxl.load_workbook(filePathTicker)

    # Download NEWS from Yahoo Finance
    #------------------------------------------------
        try:
            funda = yf.Ticker(ticker).news
            df = []
            for index2 in range (len(funda)) :
                df.append(funda[index2])

        except Exception:
            print(f' Error on NEWS from Yahoo Finance : No data!')
            df = pd.DataFrame(columns=['index','uuid','title','publisher','link','providerPublishTime','type','thumbnail','relatedTickers'              
                                    ]) # 'index','uuid','title','publisher','link','providerPublishTime','type','thumbnail','relatedTickers'

    # Start Extend Data to exel
    #------------------------------------------------
        df= pd.DataFrame(df)					
        df.to_excel( filePathTemp , sheetName)
        book2 = openpyxl.load_workbook(filePathTemp).active
    
    #Load existing sheet as it is : -Help Link https://stackoverflow.com/questions/42344041/how-to-copy-worksheet-from-one-workbook-to-another-one-using-openpyxl  
    #------------------------------------------------   
        book2._parent = book
        book._add_sheet(book2)
        book.save(filePathTicker)
        os.remove(filePathTemp)




