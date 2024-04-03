
import pandas as pd
import numpy as np
import math
import ImportData
import openpyxl








# 5sec 16min
'''
index1_5s_A = ["09:18:00","09:28:00","09:38:00","09:48:00","09:58:00","10:08:00","10:18:00","10:28:00","10:38:00","10:48:00","10:58:00","11:08:00","11:18:00","11:28:00","11:38:00","11:48:00"]
index2_5s_A = ["09:34:00","09:44:00","09:54:00","10:04:00","10:14:00","10:24:00","10:34:00","10:44:00","10:54:00","11:04:00","11:14:00","11:24:00","11:34:00","11:44:00","11:54:00","12:04:00"]
index3_5s_A = ["091800_to_093400","092800_to_094400","093800_to_095400"	,"094800_to_100400"	,"095800_to_101400"	,"100800_to_102400"	,"101800_to_103400"	,"102800_to_104400"	,"103800_to_105400"	,"104800_to_110400"	,"105800_to_111400"	,"110800_to_112400"	,"111800_to_113400"	,"112800_to_114400"	,"113800_to_115400"	,"114800_to_120400"	]
index4_5s_A = ["091800","092800","093800","094800","095800","100800","101800","102800","103800","104800","105800","110800","111800","112800","113800","114800"]
index5_5s_A = ["093400","094400","095400","100400","101400","102400","103400","104400","105400","110400","111400","112400","113400","114400","115400","120400"]
tDelta_5s_A = -1 #day
'''
index1_5s_A = ["09:28:00","09:18:00","09:28:00","09:38:00","09:48:00","09:58:00","10:08:00","10:18:00","10:28:00","10:38:00","10:48:00","10:58:00","11:08:00","11:18:00","11:28:00","11:38:00","11:48:00","11:58:00"]
index2_5s_A = ["10:01:00","09:34:00","09:44:00","09:54:00","10:04:00","10:14:00","10:24:00","10:34:00","10:44:00","10:54:00","11:04:00","11:14:00","11:24:00","11:34:00","11:44:00","11:54:00","12:04:00","12:14:00"]
index3_5s_A = ["093000_to_100000","091800_to_093400","092800_to_094400","093800_to_095400","094800_to_100400","095800_to_101400","100800_to_102400","101800_to_103400","102800_to_104400","103800_to_105400","104800_to_110400","105800_to_111400","110800_to_112400","111800_to_113400","112800_to_114400","113800_to_115400","114800_to_120400","115800_to_121400"]
index4_5s_A = ["093000","091800","092800","093800","094800","095800","100800","101800","102800","103800","104800","105800","110800","111800","112800","113800","114800","115800"]
index5_5s_A = ["100000","093400","094400","095400","100400","101400","102400","103400","104400","105400","110400","111400","112400","113400","114400","115400","120400","121400"]
tDelta_5s_A = -1 #day

# 5sec 30min
'''
index1_5s_B = ["08:00:00","08:30:00","09:00:00","09:30:00","10:00:00","10:30:00","11:00:00","11:30:00"]#"00:30","00:00",
index2_5s_B = ["08:30:00","09:00:00","09:30:00","10:00:00","10:30:00","11:00:00","11:30:00","12:00:00"] 
index3_5s_B = ["080000_to_083000","083000_to_090000","090000_to_093000","093000_to_100000","100000_to_103000","103000_to_110000","110000_to_113000","113000_to_120000"]
index4_5s_B = ["080000","083000","090000","093000","100000","103000","110000","113000"]
index5_5s_B = ["083000","090000","093000","100000","103000","110000","113000","120000"]
tDelta_5s_B = -1 #day
'''
index1_5s_B = ["07:59:00","08:29:00","08:59:00","09:29:00","09:59:00","10:29:00","10:59:00","11:29:00"]#"00:30","00:00",
index2_5s_B = ["08:31:00","09:01:00","09:31:00","10:01:00","10:31:00","11:01:00","11:31:00","12:01:00"] 
index3_5s_B = ["075900_to_083100","082900_to_090100","085900_to_093100","092900_to_100100","095900_to_103100","102900_to_110100","105900_to_113100","112900_to_120100"]
index4_5s_B = ["075900","082900","085900","092900","095900","102900","105900","112900"]
index5_5s_B = ["083100","090100","093100","100100","103100","110100","113100","120100"]
tDelta_5s_B = -1 #day

# 1min 2h32min
'''
index1_1m_A = ["09:19:00","11:20:00","13:20:00","15:20:00","17:28:00","04:00:00","05:55:00","07:55:00","08:55:00"]
index2_1m_A = ["11:51:00","13:52:00","15:52:00","17:52:00","20:00:00","06:33:00","08:28:00","10:28:00","11:28:00"]
index3_1m_A = ["091900_to_115100","112000_to_135200","132000_to_155200","152000_to_175200","172800_to_200000","040000_to_063300","055500_to_082800","075500_to_102800","085500_to_112800"]#,"_to_"
index4_1m_A = ["091900","112000","132000","152000","172800","040000","055500","075500","085500"]
index5_1m_A = ["115100","135200","155200","175200","200000","063300","082800","102800","112800"]
tDelta_1m_A = -1 #day
'''
index1_1m_A = ["09:19:00","04:00:00","05:55:00","07:55:00","09:55:00","11:55:00","13:55:00","15:55:00","17:28:00"]
index2_1m_A = ["11:51:00","06:33:00","08:28:00","10:28:00","12:28:00","14:28:00","16:28:00","18:28:00","20:00:00"]
index3_1m_A = ["091900_to_115100","040000_to_063300","055500_to_082800","075500_to_102800","095500_to_122800","115500_to_142800","135500_to_162800","155500_to_182800","172800_to_200000"]#,"_to_"
index4_1m_A = ["091900","040000","055500","075500","095500","115500","135500","155500","172800"]
index5_1m_A = ["115100","063300","082800","102800","122800","142800","162800","182800","200000"]
tDelta_1m_A = -1 #day



def fibCul(High,Low):

    Fib100 = {'Value':(Low + ((High - Low) * 1.000 ))  ,'linestyle':'solid'  ,'linewidth':3   ,'alpha':0.8   ,'color':'#4ACE14'}
    Fib764 = {'Value':(Low + ((High - Low) * 0.764 ))  ,'linestyle':'solid'  ,'linewidth':3   ,'alpha':0.8   ,'color':'#E21919'}
    Fib618 = {'Value':(Low + ((High - Low) * 0.618 ))  ,'linestyle':'solid'  ,'linewidth':3   ,'alpha':0.8   ,'color':'#27DFDD'}
    Fib500 = {'Value':(Low + ((High - Low) * 0.500 ))  ,'linestyle':'solid'  ,'linewidth':3   ,'alpha':0.8   ,'color':'#E6F226'}
    Fib382 = {'Value':(Low + ((High - Low) * 0.382 ))  ,'linestyle':'-.'     ,'linewidth':3   ,'alpha':0.8   ,'color':'#27DFDD'}
    Fib236 = {'Value':(Low + ((High - Low) * 0.236 ))  ,'linestyle':'-.'     ,'linewidth':3   ,'alpha':0.8   ,'color':'#E21919'}
    Fib000 = {'Value':(Low + ((High - Low) * 0.000 ))  ,'linestyle':'-.'     ,'linewidth':3   ,'alpha':0.8   ,'color':'#4ACE14'}

    fibolines=dict      (    hlines      =(Fib100['Value']       ,Fib764['Value']        ,Fib618['Value']        ,Fib500['Value']        ,Fib382['Value']        ,Fib236['Value']        ,Fib000['Value'])
                        ,colors      =[Fib100['color']       ,Fib764['color']        ,Fib618['color']        ,Fib500['color']        ,Fib382['color']        ,Fib236['color']        ,Fib000['color']]
                        ,linestyle   =[Fib100['linestyle']   ,Fib764['linestyle']    ,Fib618['linestyle']    ,Fib500['linestyle']    ,Fib382['linestyle']    ,Fib236['linestyle']    ,Fib000['linestyle']]
                        ,linewidths  =[Fib100['linewidth']   ,Fib764['linewidth']    ,Fib618['linewidth']    ,Fib500['linewidth']    ,Fib382['linewidth']    ,Fib236['linewidth']    ,Fib000['linewidth']]
                        ,alpha       =[Fib100['alpha']       ,Fib764['alpha']        ,Fib618['alpha']        ,Fib500['alpha']        ,Fib382['alpha']        ,Fib236['alpha']        ,Fib000['alpha']]
                    )



['#4ACE14'  ,'#E21919'  ,'#27DFDD'  , '#E6F226' , '#27DFDD' , '#E21919' ,'#4ACE14']
['solid'    ,'solid'    ,'solid'    ,'solid'    ,'solid'    ,'solid'    ,'solid']
[3          ,3          ,3          ,3          ,3          ,3          ,3]
[0.8        ,0.8        ,0.8        ,0.8        ,0.8        ,0.8        ,0.8]















scopeBook = {
                 "5s":"5s"
                ,'5 secs':"5s"
                ,"1m":"1m"
                ,'1 min':"1m"
                ,"5m":"5m"
                ,'5 mins':"5m"
                ,"30m":"30m"
                ,'30 mins':"30m"
                ,"1h":"1h"
                ,'1 hour':"1h"
                ,"1d":"1d" 
                ,'1 day':"1d" 
            } 








["5s","1m","5m","30m","1h","1d"]  



















def fun6(    filePath           = r"C:\Users\lenovo\Desktop\TGL\BCG\OK BCG.xlsx"
            ,timeStampPath      = r"D:\Python Tools\ChartMaker\SourceDocuments\InPut_Excel\Time_Stamp.xlsx"
            ,timeStampSheet     = "Ver1"
            ,DaySheetName       = "IBKR 1Day" 
            ,scope              =  "5m" # ["5s","1m","5m","30m","1h","1d"]  
            ,scopeBook          = {
                                     "5s"       :"5s"
                                    ,'5 secs'   :"5s"
                                    ,"1m"       :"1m"
                                    ,'1 min'    :"1m"
                                    ,"5m"       :"5m"
                                    ,'5 mins'   :"5m"
                                    ,"30m"      :"30m"
                                    ,'30 mins'  :"30m"
                                    ,"1h"       :"1h"
                                    ,'1 hour'   :"1h"
                                    ,"1d"       :"1d" 
                                    ,'1 day'    :"1d" 
                                } 
      
        ):
            #----------------------------------------------------------------------------------------------------------------------------------------------     
            # Date sheet:- Import data and change index to string     Help Link :-    https://stackoverflow.com/questions/44741587/pandas-timestamp-series-to-string
            #   1-Import data
            dfD = ImportData.fun2 (filePath_fun = filePath , bookName = DaySheetName) # "IBKR 1Day"
            
            if(len(dfD.index)==0):
                if(DaySheetName == "IBKR 1Day"):
                    DaySheetName = "Yahoo Dayes"
                    dfD = ImportData.fun (filePath_fun = filePath , bookName = DaySheetName )   # "Yahoo Dayes"
                elif(DaySheetName == "Yahoo Dayes"):
                    DaySheetName = "IBKR 1Day"
                    dfD = ImportData.fun2 (filePath_fun = filePath , bookName = DaySheetName )   # "Yahoo Dayes"
                else:
                    print("Wrong Day Sheet Name")
                # dfD = ImportData.fun2 (filePath_fun = filePath , bookName = DaySheetName )   # "Yahoo Dayes"
            #   2-Change index Type to string
            dfD.index = dfD.index.astype(str)
            #----------------------------------------------------------------------------------------------------------------------------------------------     



            #----------------------------------------------------------------------------------------------------------------------------------------------     
            # Time Stamp sheet:- Import  data and Set column header 
            #   1-Import  data
            book = openpyxl.load_workbook(timeStampPath)
            sheet = book[timeStampSheet]
            dfS= pd.DataFrame(sheet.values)
            #   2-Set column header :- Convert row to column header for Pandas DataFrame : Link https://stackoverflow.com/questions/26147180/convert-row-to-column-header-for-pandas-dataframe
            dfS.columns = dfS.iloc[0]
            dfS = dfS.drop(0)
            #----------------------------------------------------------------------------------------------------------------------------------------------     


            
            #----------------------------------------------------------------------------------------------------------------------------------------------     
            # OutPut Dataframe "taro":-     #   01- Create dataframe :-
            #-------------------------------#   02- Rename column in dataframe :- 
            #-------------------------------#   03- Clean None Rows :-
            #-------------------------------#   04- Change object to float :-
            #-------------------------------#   05- Add date to index colum :-
            #-------------------------------#   06- Change type of index colum to Time stamp :-
            #-------------------------------#   07- Return OutPut Dataframe "taro" :-
            #   01- Create dataframe :- from "dfS" another dataframe    Help Link :- https://www.statology.org/pandas-create-dataframe-from-existing-dataframe/
            taro = dfS[[    
                                         ("Index1_"         + scopeBook[scope])
                                        ,("Index2_"         + scopeBook[scope])
                                        ,("Name_"           + scopeBook[scope])
                                        ,("StartDelta_"     + scopeBook[scope])
                                        ,("EndDelta_"       + scopeBook[scope])
                                        ,("Fibonacci_"      + scopeBook[scope])
                                        ,("Scope_"          + scopeBook[scope])
                                        ,("HourConstant_"   + scopeBook[scope])
                                        ,("MinConstant_"    + scopeBook[scope])
                                        ,("SecConstant_"    + scopeBook[scope])
                                        ,("leftSide_"       + scopeBook[scope])
                                        ,("Blank_"          + scopeBook[scope])
                                        ]].copy()                        
            #   02- Rename column in dataframe :-      Help Link :- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html
            taro = taro.rename(columns={                                                                  
                                         "Index1_"         + scopeBook[scope]    :"Index1"
                                        ,"Index2_"         + scopeBook[scope]    :"Index2"
                                        ,"Name_"           + scopeBook[scope]    :"Name"
                                        ,"StartDelta_"     + scopeBook[scope]    :"StartDelta"
                                        ,"EndDelta_"       + scopeBook[scope]    :"EndDelta"
                                        ,"Fibonacci_"      + scopeBook[scope]    :"Fibonacci"
                                        ,"Scope_"          + scopeBook[scope]    :"Scope"
                                        ,"HourConstant_"   + scopeBook[scope]    :"HourConstant"
                                        ,"MinConstant_"    + scopeBook[scope]    :"MinConstant"
                                        ,"SecConstant_"    + scopeBook[scope]    :"SecConstant"
                                        ,"leftSide_"       + scopeBook[scope]    :"leftSide"
                                        ,"Blank_"          + scopeBook[scope]    :"Date"
                                        })
            #   03- Clean None Rows :- Help Link :- https://www.digitalocean.com/community/tutorials/pandas-dropna-drop-null-na-values-from-dataframe    ,   https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html
            taro = taro.dropna(how='all')
            taro.reset_index(inplace=True, drop=True)
            #   04- Change object to float :-   Help Link https://stackoverflow.com/questions/36814100/pandas-to-numeric-for-multiple-columns
            cols = taro.columns.drop(["Index1","Index2","Name","Fibonacci","Scope","Date"])   # set colums you dont want to change         
            taro[cols] = taro[cols].apply(pd.to_numeric, errors='coerce')            
            #   05- Add date to index colum :-            
            taro["Date"] = dfD.index[taro.EndDelta]
            taro.Index2 = taro.Date + " " + taro.Index2                        
            for x in range (len(taro)): 
                # IF taro.StartDelta out of bounds for dfD.index set the firist Day is the start of dfD.index    
                if(len(dfD.index) >= abs(taro.loc[x].StartDelta)): 
                    # print(">>>>_______________________________<<<<")
                    # print(dfD.index[taro.loc[x].StartDelta])    
                    taro.Date[x] = dfD.index[taro.loc[x].StartDelta]      
                else:                       
                    taro.Date[x] =    dfD.index[0]                                    
            taro.Index1 = taro.Date + " " + taro.Index1
            #   06- Change type of index colum to Time stamp :-            
            print(">>>>$$$$$$$$$$$$$$<<<<")
            print(dfD)
            print(taro)
            print(">>>>$$$$$$$$$$$$$$<<<<")
            taro.Index1 = pd.to_datetime(taro.Index1.astype('datetime64[ns]'))
            taro.Index2 = pd.to_datetime(taro.Index2.astype('datetime64[ns]'))            
            #   07- Return OutPut Dataframe "taro" :-
            return taro
            #----------------------------------------------------------------------------------------------------------------------------------------------     










print("Start test for new Time Stamp")

fun6()
