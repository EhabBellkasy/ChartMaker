



import pandas as pd
import yfinance as yf
import openpyxl
import os


ticker = 'AAPL'

funda = yf.Ticker(ticker).get_info()
df= pd.DataFrame([funda])
# Swap Rows and Columns                 Help Link :- https://note.nkmk.me/en/python-pandas-t-transpose/
df= df.transpose()
# Rename column in dataframe :-         Help Link :- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html
df= df.rename(columns={0:"Data"})
# Add an empty column to a dataframe    Help Link :- https://stackoverflow.com/questions/16327055/how-to-add-an-empty-column-to-a-dataframe
df["Premarket_High"]    = ""
df["High"]              = ""
df["Low"]               = ""
df["Open"]              = ""
df["Close"]             = ""
df["Previos_Close"]     = ""
df["Volume"]            = ""
df["H_Vol"]             = ""
df["L_Vol"]             = ""

print(df)

# print(df.dtypes)
# print(df.transpose())

# for key, value in funda.info.items():
#     print(key, ":", value)

# df = df.set_index('symbol')
# print(df)


print(f' Error on Fundamentals : No data!')
index = [
 'address1','address2','city','state','zip','country','phone','website','industry'
,'industryKey','industryDisp','sector','sectorKey','sectorDisp','longBusinessSummary','companyOfficers','compensationAsOfEpochDate','maxAge','priceHint'
,'previousClose','open','dayLow','dayHigh','regularMarketPreviousClose','regularMarketOpen','regularMarketDayLow','regularMarketDayHigh','forwardPE','volume'
,'regularMarketVolume','averageVolume','averageVolume10days','averageDailyVolume10Day','bid','ask','bidSize','askSize','marketCap','fiftyTwoWeekLow','fiftyTwoWeekHigh'
,'priceToSalesTrailing12Months','fiftyDayAverage','twoHundredDayAverage','currency','enterpriseValue','profitMargins','floatShares','sharesOutstanding','sharesShort'
,'sharesShortPriorMonth','sharesShortPreviousMonthDate','dateShortInterest','sharesPercentSharesOut','heldPercentInsiders','heldPercentInstitutions','shortRatio'
,'shortPercentOfFloat','impliedSharesOutstanding','bookValue','priceToBook','lastFiscalYearEnd','nextFiscalYearEnd','mostRecentQuarter','netIncomeToCommon'
,'trailingEps','forwardEps','lastSplitFactor','lastSplitDate','enterpriseToRevenue','enterpriseToEbitda','52WeekChange','SandP52WeekChange','exchange'
,'quoteType','symbol','underlyingSymbol','shortName','longName','firstTradeDateEpochUtc','timeZoneFullName','timeZoneShortName','uuid','messageBoardId'
,'gmtOffSetMilliseconds','currentPrice','targetHighPrice','targetLowPrice','targetMeanPrice','targetMedianPrice','recommendationKey','numberOfAnalystOpinions'
,'totalCash','totalCashPerShare','ebitda','totalDebt','quickRatio','currentRatio','totalRevenue','debtToEquity','revenuePerShare','returnOnAssets'
,'returnOnEquity','freeCashflow','operatingCashflow','revenueGrowth','grossMargins','ebitdaMargins','operatingMargins','financialCurrency','trailingPegRatio'
]

df = pd.DataFrame(columns=['INDEX','Data','PremarketHigh','High','Low','Open','Close','Previos_Close','Volume','H_Vol','L_Vol' ])
df.INDEX = index





print(df)





















index = [
 'address1'
,'address2'
,'city'
,'state'
,'zip'
,'country'
,'phone'
,'website'
,'industry'
,'industryKey'
,'industryDisp'
,'sector'
,'sectorKey'
,'sectorDisp'
,'longBusinessSummary'
,'companyOfficers'
,'compensationAsOfEpochDate'
,'maxAge'
,'priceHint'
,'previousClose'
,'open'
,'dayLow'
,'dayHigh'
,'regularMarketPreviousClose'
,'regularMarketOpen'
,'regularMarketDayLow'
,'regularMarketDayHigh'
,'forwardPE'
,'volume'
,'regularMarketVolume'
,'averageVolume'
,'averageVolume10days'
,'averageDailyVolume10Day'
,'bid'
,'ask'
,'bidSize'
,'askSize'
,'marketCap'
,'fiftyTwoWeekLow'
,'fiftyTwoWeekHigh'
,'priceToSalesTrailing12Months'
,'fiftyDayAverage'
,'twoHundredDayAverage'
,'currency'
,'enterpriseValue'
,'profitMargins'
,'floatShares'
,'sharesOutstanding'
,'sharesShort'
,'sharesShortPriorMonth'
,'sharesShortPreviousMonthDate'
,'dateShortInterest'
,'sharesPercentSharesOut'
,'heldPercentInsiders'
,'heldPercentInstitutions'
,'shortRatio'
,'shortPercentOfFloat'
,'impliedSharesOutstanding'
,'bookValue'
,'priceToBook'
,'lastFiscalYearEnd'
,'nextFiscalYearEnd'
,'mostRecentQuarter'
,'netIncomeToCommon'
,'trailingEps'
,'forwardEps'
,'lastSplitFactor'
,'lastSplitDate'
,'enterpriseToRevenue'
,'enterpriseToEbitda'
,'52WeekChange'
,'SandP52WeekChange'
,'exchange'
,'quoteType'
,'symbol'
,'underlyingSymbol'
,'shortName'
,'longName'
,'firstTradeDateEpochUtc'
,'timeZoneFullName'
,'timeZoneShortName'
,'uuid'
,'messageBoardId'
,'gmtOffSetMilliseconds'
,'currentPrice'
,'targetHighPrice'
,'targetLowPrice'
,'targetMeanPrice'
,'targetMedianPrice'
,'recommendationKey'
,'numberOfAnalystOpinions'
,'totalCash'
,'totalCashPerShare'
,'ebitda'
,'totalDebt'
,'quickRatio'
,'currentRatio'
,'totalRevenue'
,'debtToEquity'
,'revenuePerShare'
,'returnOnAssets'
,'returnOnEquity'
,'freeCashflow'
,'operatingCashflow'
,'revenueGrowth'
,'grossMargins'
,'ebitdaMargins'
,'operatingMargins'
,'financialCurrency'
,'trailingPegRatio'
]















