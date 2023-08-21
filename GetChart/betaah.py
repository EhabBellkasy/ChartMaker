import alpaah
from alpaah import betra
import TimeStamp as TS


# print (alpaah.betra)
# print (betra)
# EZA=[1,5,7,4,6]
# BZA=[42,79,31,54]
# print(EZA)
# EZA.append(2)
# print(EZA)
# EZA.extend(BZA)
# print(EZA)


# print("###################################################################")

# index = 0
# index1 =TS.fun(scope="5s",indexType =1)
# index2 =TS.fun(scope="5s",indexType =2)
# index3 =TS.fun(scope="5s",indexType =3)

# print (len(index1))

# for index in range(len(index1)):
#     print(index1[index] ,index2[index] ,index3[index])



# ###########################################################

# import pandas as pd
# filePathWL = r"D:\Python Tools\ChartMaker\SourceDocuments\InPut_Excel\Watch_List.xlsx"

k =9

if (k in [1,6,7,12]):
    print ("yes")
elif(k in [9,2,3,5]):
    print ("ok")
else:
    print ("NO")

import ImportData
import pandas as pd

filePath = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\gv mmm.xlsx'
bookScope = "Yahoo Dayes"  # "Yahoo 5m"  "Yahoo Dayes"

index1_5s_A = ["09:18:00","09:28:00","09:38:00","09:48:00","09:58:00","10:08:00","10:18:00","10:28:00","10:38:00","10:48:00","10:58:00","11:08:00","11:18:00","11:28:00","11:38:00","11:48:00"]
index2_5s_A = ["09:34:00","09:44:00","09:54:00","10:04:00","10:14:00","10:24:00","10:34:00","10:44:00","10:54:00","11:04:00","11:14:00","11:24:00","11:34:00","11:44:00","11:54:00","12:04:00"]
index3_5s_A = ["091800_to_093400","092800_to_094400","093800_to_095400"	,"094800_to_100400"	,"095800_to_101400"	,"100800_to_102400"	,"101800_to_103400"	,"102800_to_104400"	,"103800_to_105400"	,"104800_to_110400"	,"105800_to_111400"	,"110800_to_112400"	,"111800_to_113400"	,"112800_to_114400"	,"113800_to_115400"	,"114800_to_120400"	]

taro = pd.DataFrame({
                        'index1': index1_5s_A,
                        'index2': index2_5s_A,
                        'index3': index3_5s_A
                    })

# taro.index1 = pd.to_datetime(taro.index1.astype('datetime64[ns]'))
print(taro)




df = ImportData.fun (filePath_fun = filePath , bookName = bookScope)

print (df)
print (df.dtypes)
deltaro = "09:18:00"
Sday = str( df.index[-5] )
Eday = str( df.index[-1] )


print("###############################")
# print(ENDdaystr[:11] + deltaro)

taro["index4"] = Eday[:10].replace('-', '') +'_'+ (taro.index1.str.replace(':', ''))
taro["index5"] = Eday[:10].replace('-', '') +'_'+ (taro.index2.str.replace(':', ''))
taro.index1 = Sday[:11] + taro.index1 
taro.index2 = Eday[:11] + taro.index2 

print(taro)

print("###############################")
print( len(taro.index1) )


#index1_5s_A.astype('datetime64[ns]')
#print (ENDday)
#print (deltaro)

# ENDday += 09:18:00








