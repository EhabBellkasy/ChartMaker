








# 5sec 16min
index1_5s_A = ["09:18:00","09:28:00","09:38:00","09:48:00","09:58:00","10:08:00","10:18:00","10:28:00","10:38:00","10:48:00","10:58:00","11:08:00","11:18:00","11:28:00","11:38:00","11:48:00"]
index2_5s_A = ["09:34:00","09:44:00","09:54:00","10:04:00","10:14:00","10:24:00","10:34:00","10:44:00","10:54:00","11:04:00","11:14:00","11:24:00","11:34:00","11:44:00","11:54:00","12:04:00"]
index3_5s_A = ["091800_to_093400","092800_to_094400","093800_to_095400"	,"094800_to_100400"	,"095800_to_101400"	,"100800_to_102400"	,"101800_to_103400"	,"102800_to_104400"	,"103800_to_105400"	,"104800_to_110400"	,"105800_to_111400"	,"110800_to_112400"	,"111800_to_113400"	,"112800_to_114400"	,"113800_to_115400"	,"114800_to_120400"	]
tDelta_5s_A = 16 #min

# 5sec 30min
index1_5s_B =["08:00:00","08:30:00","09:00:00","09:30:00","10:00:00","10:30:00","11:00:00","11:30:00"]#"00:30","00:00",
index2_5s_B =["08:30:00","09:00:00","09:30:00","10:00:00","10:30:00","11:00:00","11:30:00","12:00:00"] 
index3_5s_B =["080000_to_083000","083000_to_090000","090000_to_093000","093000_to_100000","100000_to_103000","103000_to_110000","110000_to_113000","113000_to_120000"]
tDelta_5s_B = 30 #min

# 1min 2h32min
index1_1m_A = ["09:19:00","11:20:00","13:20:00","15:20:00","17:28:00","04:00:00","05:55:00","07:55:00","08:55:00"]
index2_1m_A = ["11:51:00","13:52:00","15:52:00","17:52:00","20:00:00","06:33:00","08:28:00","10:28:00","11:28:00"]
index3_1m_A = ["091900_to_115100","112000_to_135200","132000_to_155200","152000_to_175200","172800_to_200000","040000_to_063300","055500_to_082800","075500_to_102800","085500_to_112800"]#,"_to_"
tDelta_1m_A = 152 #min

# 5min 8h5min 
index1_5m_A = ["04:00:00","08:45:00","12:05:00","15:20:00"]
index2_5m_A = ["11:55:00","16:40:00","20:00:00","17:52:00"]
index3_5m_A = ["040000_to_115500","084500_to_164000","120500_to_200000","152000_to_175200"]
tDelta_5m_A = 485 #min

# 30min 6days
index1_30m_A = ["04:00:00"]
index2_30m_A = ["20:00:00"]
index3_30m_A = ["040000_to_200000"]
tDelta_30m_A = 6 #days

# 1h 21days
index1_1h_A = ["04:00:00"]
index2_1h_A = ["20:00:00"]
index3_1h_A = ["040000_to_200000"]
tDelta_1h_A = 21 #days

# 1d 220days
index1_1d_A = ["04:00:00"]
index2_1d_A = ["20:00:00"]
index3_1d_A = ["040000_to_200000"]
tDelta_1d_A = 220 #days




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
















