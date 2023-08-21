import pandas as pd
import ImportData








# 5sec 16min
index1_5s_A = ["09:18:00","09:28:00","09:38:00","09:48:00","09:58:00","10:08:00","10:18:00","10:28:00","10:38:00","10:48:00","10:58:00","11:08:00","11:18:00","11:28:00","11:38:00","11:48:00"]
index2_5s_A = ["09:34:00","09:44:00","09:54:00","10:04:00","10:14:00","10:24:00","10:34:00","10:44:00","10:54:00","11:04:00","11:14:00","11:24:00","11:34:00","11:44:00","11:54:00","12:04:00"]
index3_5s_A = ["091800_to_093400","092800_to_094400","093800_to_095400"	,"094800_to_100400"	,"095800_to_101400"	,"100800_to_102400"	,"101800_to_103400"	,"102800_to_104400"	,"103800_to_105400"	,"104800_to_110400"	,"105800_to_111400"	,"110800_to_112400"	,"111800_to_113400"	,"112800_to_114400"	,"113800_to_115400"	,"114800_to_120400"	]
index4_5s_A = ["091800","092800","093800","094800","095800","100800","101800","102800","103800","104800","105800","110800","111800","112800","113800","114800"]
index5_5s_A = ["093400","094400","095400","100400","101400","102400","103400","104400","105400","110400","111400","112400","113400","114400","115400","120400"]
tDelta_5s_A = -1 #day

# 5sec 30min
index1_5s_B = ["08:00:00","08:30:00","09:00:00","09:30:00","10:00:00","10:30:00","11:00:00","11:30:00"]#"00:30","00:00",
index2_5s_B = ["08:30:00","09:00:00","09:30:00","10:00:00","10:30:00","11:00:00","11:30:00","12:00:00"] 
index3_5s_B = ["080000_to_083000","083000_to_090000","090000_to_093000","093000_to_100000","100000_to_103000","103000_to_110000","110000_to_113000","113000_to_120000"]
index4_5s_B = ["080000","083000","090000","093000","100000","103000","110000","113000"]
index5_5s_B = ["083000","090000","093000","100000","103000","110000","113000","120000"]
tDelta_5s_B = -1 #day

# 1min 2h32min
index1_1m_A = ["09:19:00","11:20:00","13:20:00","15:20:00","17:28:00","04:00:00","05:55:00","07:55:00","08:55:00"]
index2_1m_A = ["11:51:00","13:52:00","15:52:00","17:52:00","20:00:00","06:33:00","08:28:00","10:28:00","11:28:00"]
index3_1m_A = ["091900_to_115100","112000_to_135200","132000_to_155200","152000_to_175200","172800_to_200000","040000_to_063300","055500_to_082800","075500_to_102800","085500_to_112800"]#,"_to_"
index4_1m_A = ["091900","112000","132000","152000","172800","040000","055500","075500","085500"]
index5_1m_A = ["115100","135200","155200","175200","200000","063300","082800","102800","112800"]
tDelta_1m_A = -1 #day

# 5min 8h5min 
index1_5m_A = ["04:00:00","08:45:00","12:05:00","15:20:00"]
index2_5m_A = ["11:55:00","16:40:00","20:00:00","17:52:00"]
index3_5m_A = ["040000_to_115500","084500_to_164000","120500_to_200000","152000_to_175200"]
index4_5m_A = ["040000","084500","120500","152000"]
index5_5m_A = ["115500","164000","200000","175200"]
tDelta_5m_A = -1 #day

# 30min 6days
index1_30m_A = ["04:00:00"]
index2_30m_A = ["20:00:00"]
index3_30m_A = ["040000_to_200000"]
index4_30m_A = ["040000"]
index5_30m_A = ["200000"]
tDelta_30m_A = -6 #days

# 1h 21days
index1_1h_A = ["04:00:00"]
index2_1h_A = ["20:00:00"]
index3_1h_A = ["040000_to_200000"]
index4_1h_A = ["040000"]
index5_1h_A = ["200000"]
tDelta_1h_A = -21 #days

# 1d 220days
index1_1d_A = ["04:00:00"]
index2_1d_A = ["20:00:00"]
index3_1d_A = ["040000_to_200000"]
index4_1d_A = ["040000"]
index5_1d_A = ["200000"]
tDelta_1d_A = -220 #days




def fun(scope       = "1m", # ["5s","1m","5m","30m","1h","1d"]
        indexType   = 1     # [1,2,3]
        ):
    
    if(scope == "5s"):
        if(indexType==1):
            index = index1_5s_A
            index.extend(index1_5s_B)
        elif(indexType==2):
            index = index2_5s_A
            index.extend(index2_5s_B)
        elif(indexType==3):
            index = index3_5s_A
            index.extend(index3_5s_B)
        else:
            print ("wrong index number only accept [1,2,3]")

    elif(scope == "1m"):
        if(indexType==1):
            index = index1_1m_A
        elif(indexType==2):
            index = index2_1m_A
        elif(indexType==3):
            index = index3_1m_A
        else:
            print ("wrong index number only accept [1,2,3]")

    elif(scope == "5m"):
        if(indexType==1):
            index = index1_5m_A
        elif(indexType==2):
            index = index2_5m_A
        elif(indexType==3):
            index = index3_5m_A
        else:
            print ("wrong index number only accept [1,2,3]")

    elif(scope == "30m"):
        if(indexType==1):
            index = index1_30m_A
        elif(indexType==2):
            index = index2_30m_A
        elif(indexType==3):
            index = index3_30m_A
        else:
            print ("wrong index number only accept [1,2,3]")

    elif(scope == "1h"):
        if(indexType==1):
            index = index1_1h_A
        elif(indexType==2):
            index = index2_1h_A
        elif(indexType==3):
            index = index3_1h_A
        else:
            print ("wrong index number only accept [1,2,3]")

    elif(scope == "1d"):
        if(indexType==1):
            index = index1_1d_A
        elif(indexType==2):
            index = index2_1d_A
        elif(indexType==3):
            index = index3_1d_A
        else:
            print ("wrong index number only accept [1,2,3]")

    else:
        print ("wrong Scope type only accept ['5s','1m','5m','30m','1h','1d']")

    return index


def fun2(   filePath ,
            bookScope = "Yahoo Dayes" ,
            scope       = "1m" # ["5s","1m","5m","30m","1h","1d"]         
        ): 
    df = ImportData.fun (filePath_fun = filePath , bookName = bookScope)
    Eday = str( df.index[-1] )

    if      (scope=="5s"):
        taro = pd.DataFrame({
                                'index1': index1_5s_A + index1_5s_B,
                                'index2': index2_5s_A + index2_5s_B,
                                'index3': index3_5s_A + index3_5s_B
                                # 'index4': index2_5s_A + index4_5s_B,
                                # 'index5': index2_5s_A + index5_5s_B
                            })
        Sday = str( df.index[tDelta_5s_A] )

    elif    (scope=="1m"):
        taro = pd.DataFrame({
                                'index1': index1_1m_A,
                                'index2': index2_1m_A,
                                'index3': index3_1m_A
                                # 'index4': index4_1m_A,
                                # 'index5': index5_1m_A
                            })
        Sday = str( df.index[tDelta_1m_A] )

    elif    (scope=="5m"):
        taro = pd.DataFrame({
                                'index1': index1_5m_A,
                                'index2': index2_5m_A,
                                'index3': index3_5m_A
                                # 'index4': index4_5m_A,
                                # 'index5': index5_5m_A
                            })
        Sday = str( df.index[tDelta_5m_A] )

    elif    (scope=="30m"):
        taro = pd.DataFrame({
                                'index1': index1_30m_A,
                                'index2': index2_30m_A,
                                'index3': index3_30m_A
                                # 'index4': index4_30m_A,
                                # 'index5': index5_30m_A
                            })
        Sday = str( df.index[tDelta_30m_A] )

    elif    (scope=="1h"):
        taro = pd.DataFrame({
                                'index1': index1_1h_A,
                                'index2': index2_1h_A,
                                'index3': index3_1h_A
                                # 'index4': index4_1h_A,
                                # 'index5': index5_1h_A
                            })
        Sday = str( df.index[tDelta_1h_A] )

    elif    (scope=="1d"):
        taro = pd.DataFrame({
                                'index1': index1_1d_A,
                                'index2': index2_1d_A,
                                'index3': index3_1d_A
                                # 'index4': index4_1d_A,
                                # 'index5': index5_1d_A
                            })
        Sday = str( df.index[tDelta_1d_A] )

    else:
        print ("wrong Scope type only accept ['5s','1m','5m','30m','1h','1d']")
    

    taro["index4"] = Eday[:10].replace('-', '') +'_'+ (taro.index1.str.replace(':', '')) # link:- https://www.statology.org/pandas-remove-characters-from-string/
    taro["index5"] = Eday[:10].replace('-', '') +'_'+ (taro.index2.str.replace(':', ''))
    taro.index1 = Sday[:11] + taro.index1 
    taro.index2 = Eday[:11] + taro.index2 

    taro.index1 = pd.to_datetime(taro.index1.astype('datetime64[ns]'))
    taro.index2 = pd.to_datetime(taro.index2.astype('datetime64[ns]'))

    return taro













