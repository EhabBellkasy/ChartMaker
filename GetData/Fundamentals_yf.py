# import the libraries

import pandas as pd
import yfinance as yf
import openpyxl
import os


def fun (   ticker = 'goog',
            filePath = r"C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Split ",
            sheetName = 'Yahoo Fundamentals'

):

    # Set Varibles
    filePathTicker = filePath + ticker + ".xlsx"
    filePathTemp = filePath + " Temp " + ".xlsx"
    book  = openpyxl.load_workbook(filePathTicker)

    # Download Fundamentals from Yahoo Finance
    try:
        funda = yf.Ticker(ticker).info
        df= pd.DataFrame([funda])
        df = df.set_index('symbol')
        print(df)

    except Exception:
        print(f' Error on Fundamentals : No data!')
        df = pd.DataFrame(columns=['symbol','address1','city','state','zip','country','phone','website','industry','industryDisp','sector',	
                                'longBusinessSummary','fullTimeEmployees','companyOfficers','auditRisk','boardRisk','compensationRisk',
                                'shareHolderRightsRisk','overallRisk','governanceEpochDate','compensationAsOfEpochDate','maxAge','priceHint',
                                'previousClose','open','dayLow','dayHigh','regularMarketPreviousClose','regularMarketOpen','regularMarketDayLow',
                                'regularMarketDayHigh','payoutRatio','beta','trailingPE','forwardPE','volume','regularMarketVolume','averageVolume',
                                'averageVolume10days','averageDailyVolume10Day','bid','ask','bidSize','askSize','marketCap','fiftyTwoWeekLow','fiftyTwoWeekHigh',
                                'priceToSalesTrailing12Months','fiftyDayAverage','twoHundredDayAverage','trailingAnnualDividendRate','trailingAnnualDividendYield',
                                'currency','enterpriseValue','profitMargins','floatShares','sharesOutstanding','sharesShort','sharesShortPriorMonth',
                                'sharesShortPreviousMonthDate','dateShortInterest','sharesPercentSharesOut','heldPercentInsiders','heldPercentInstitutions',
                                'shortRatio','shortPercentOfFloat','impliedSharesOutstanding','bookValue','priceToBook','lastFiscalYearEnd','nextFiscalYearEnd',
                                'mostRecentQuarter','earningsQuarterlyGrowth','netIncomeToCommon','trailingEps','forwardEps','pegRatio','enterpriseToRevenue',
                                'enterpriseToEbitda','52WeekChange','SandP52WeekChange','exchange','quoteType','underlyingSymbol','shortName','longName',
                                'firstTradeDateEpochUtc','timeZoneFullName','timeZoneShortName','uuid','messageBoardId','gmtOffSetMilliseconds','currentPrice',
                                'targetHighPrice','targetLowPrice','targetMeanPrice','targetMedianPrice','recommendationMean','recommendationKey','numberOfAnalystOpinions',
                                'totalCash','totalCashPerShare','ebitda','totalDebt','quickRatio','currentRatio','totalRevenue','debtToEquity','revenuePerShare',
                                'returnOnAssets','returnOnEquity','grossProfits','freeCashflow','operatingCashflow','earningsGrowth','revenueGrowth','grossMargins',
                                'ebitdaMargins','operatingMargins','financialCurrency','trailingPegRatio','lastSplitFactor','lastSplitDate','dividendRate',
                                'dividendYield','exDividendDate','fiveYearAvgDividendYield','lastDividendValue','lastDividendDate'
                                    ]) # need to change this
        

    df.to_excel( filePathTemp , sheetName)
    book2 = openpyxl.load_workbook(filePathTemp).active
    book2._parent = book
    book._add_sheet(book2)
    book.save(filePathTicker)
    os.remove(filePathTemp)







