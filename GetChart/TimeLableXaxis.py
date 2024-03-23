import mplfinance as mpf
import yfinance as yf
import datetime


def fTest():

    # df = yf.download('DIA',start='2024-01-07',end='2024-01-15',interval='15m')
    # print(df)

    # ticks = []
    # tlabs = []
    # dates = sorted(list(set([d.date() for d in df.index])))
    # for d1 in dates:
    #     d2 = d1 + datetime.timedelta(days=1)
    #     ts = df.loc[d1:d2].index[0]  # first timestamp of each day
    #     ticks.append(df.index.get_loc(ts))
    #     tlabs.append(d1.strftime('%b %d'))

    #     print("d1=",d1)
    #     print("d2=",d2)
    #     print("ts=",ts)
    #     print("______")

    # fig, axlist = mpf.plot(df,type='candle',xrotation=0,style='yahoo',tight_layout=True,returnfig=True)
    # axlist[-2].set_xticks(ticks,labels=tlabs,ha='left')

    # mpf.show()
    # print(ticks)
    # print(tlabs)
    # print(dates)
    # print()

    # ticks = []
    # tlabs = []
    # mitks = []
    # milab = []
    # dates = sorted(list(set([d.date() for d in df.index])))

    # for d1 in dates:

    #     # Major Ticks:
    #     d2 = d1 + datetime.timedelta(days=1)
    #     ts = df.loc[d1:d2].index[0]
    #     ticks.append(df.index.get_loc(ts))
    #     # line feed at beginning of label so it appears a lower below the x-axis:
    #     tlabs.append('\n'+d1.strftime('%b %d'))

    #     # Minor Ticks:
    #     mitks.append(ticks[-1]+0.1)
    #     milab.append('09:30')
    #     ts = df.loc[str(d1)+' 13:00':d2].index[0]
    #     mitks.append(df.index.get_loc(ts))
    #     milab.append('13:00')

    # fig, axlist = mpf.plot(df,type='candle',xrotation=0,style='yahoo',tight_layout=True,returnfig=True,figratio=(2,1))

    # axlist[-2].set_xticks(ticks)
    # axlist[-2].set_xticklabels(tlabs, ha='left')
    # axlist[-2].set_xticks(mitks,minor=True)
    # axlist[-2].set_xticklabels(milab, ha='center', minor=True, rotation=0)

    # mpf.show()

    print("*******************")
    print(15%2)
    print("*******************")

    df = yf.download('DIA',start='2024-02-28',end='2024-02-29',interval='1m')
    print(df)

    ticks = []
    tlabs = []
    dates = sorted(list(set([d.date() for d in df.index])))


    print("*******************")
    print(dates)
    print("*******************")



    print("*********@@@**********")
    grogro = []
    # grogro = list(df.index.values)
    grogro = list (df.index.map(str))
    print(grogro[5][11:16]) # lable
    print(int(grogro[5][14:16]))
    print("*********@@@**********")

    for i in range (len(grogro)) : 
        if( ((int(grogro[i][14:16])) % 5 ) == 0):
            print(i)
            print(grogro[i][11:16]) # lable
            print("---")
            ticks.append(i)
            tlabs.append(grogro[i][11:16])

    print(ticks)
    print(tlabs)

    fig, axlist = mpf.plot(df,type='candle',xrotation=0,style='yahoo',tight_layout=True,returnfig=True)
    axlist[-2].set_xticks(ticks,labels=tlabs,ha='center',kl=0)

    mpf.show()
    print("**________***")
    print(type( axlist[-2]))




#--------------------------------------------------------------------------------------------------------------------------





def fTimeLable  (   source="IBKR",
                    interval='1 min',
                    inList=[]
                ):
    print("###-TimeLable-###")
    
    # Set Varibles
    #------------------------------------------------

    tickFlag=True

    monthName=  [
                 "\nworng"
                ,"\nJan"
                ,"\nFeb"
                ,"\nMar"
                ,"\nApr"
                ,"\nMay"
                ,"\nJun"
                ,"\nJul"
                ,"\nAug"
                ,"\nSep"
                ,"\nOct"
                ,"\nNov"
                ,"\nDec"
                ,"" 
                ]

    srcIndex =  {
                    'IBKR'  :{'Y1': 0, 'Y2':4, 'M1': 5, 'M2':7, 'D1':8, 'D2':10,  'H1':11,  'H2':13, 'm1':14, 'm2':16, 's1':17, 's2':19 },
                    'Yahoo' :{'Y1': 0, 'Y2':4, 'M1': 5, 'M2':7, 'D1':8, 'D2':10, 'H1':11, 'H2':13, 'm1':13, 'm2':15, 's1':17, 's2':19 }
                }
        
    ntrvlHub =  {
                    '1 secs'	:{	'SheetName':'IBKR 1s'	    ,'IntervalSize':'1 min'	    ,'Scope':'intraday'	    ,'hourConstant':1	    ,'minConstant':1	    ,'secConstant':0.3      ,'leftSide':0	},		#	XX:XX:OO	Every 1  min
                    '5 secs'	:{	'SheetName':'IBKR 5s'   	,'IntervalSize':'1 min'	    ,'Scope':'intraday'	    ,'hourConstant':1	    ,'minConstant':1	    ,'secConstant':0.3	    ,'leftSide':-0.41  },		#	XX:XX:OO	Every 1  min
                    '10 secs'	:{	'SheetName':'IBKR 10s'  	,'IntervalSize':'1 min'	    ,'Scope':'intraday'	    ,'hourConstant':1	    ,'minConstant':1	    ,'secConstant':0.3	    ,'leftSide':0   },		#	XX:XX:OO	Every 1  min
                    '15 secs'	:{	'SheetName':'IBKR 15s'  	,'IntervalSize':'1 min'	    ,'Scope':'intraday'	    ,'hourConstant':1	    ,'minConstant':1	    ,'secConstant':0.3	    ,'leftSide':0   },		#	XX:XX:OO	Every 1  min
                    '30 secs'	:{	'SheetName':'IBKR 30s'  	,'IntervalSize':'5 min'	    ,'Scope':'intraday'	    ,'hourConstant':1	    ,'minConstant':5	    ,'secConstant':0.3	    ,'leftSide':0   },		#	XX:O5:OO	Every 5  min
                    '1 min' 	:{	'SheetName':"IBKR 1m"   	,'IntervalSize':'5 min'	    ,'Scope':'intraday'	    ,'hourConstant':1	    ,'minConstant':5	    ,'secConstant':0.3	    ,'leftSide':-0.35   },		#	XX:O5:OO	Every 5  min
                    '2 mins' 	:{	'SheetName':'IBKR 2m'   	,'IntervalSize':'10 min'	,'Scope':'intraday'	    ,'hourConstant':1	    ,'minConstant':10	    ,'secConstant':0.3	    ,'leftSide':0   },		#	XX:10:OO	Every 10 min
                    '3 mins' 	:{	'SheetName':'IBKR 3m'   	,'IntervalSize':'15 min'	,'Scope':'intraday'	    ,'hourConstant':1	    ,'minConstant':15	    ,'secConstant':0.3	    ,'leftSide':0   },		#	XX:15:OO	Every 15 min
                    '5 mins' 	:{	'SheetName':'IBKR 5m'   	,'IntervalSize':'15 min'	,'Scope':'intraday'	    ,'hourConstant':1	    ,'minConstant':15	    ,'secConstant':0.3	    ,'leftSide':-0.36   },		#	XX:15:OO	Every 15 min
                    '10 mins'	:{	'SheetName':'IBKR 10m'  	,'IntervalSize':'30 mins'	,'Scope':'intraday'	    ,'hourConstant':1	    ,'minConstant':30	    ,'secConstant':0.3	    ,'leftSide':0   },		#	XX:30:OO	Every 30 min
                    '15 mins'	:{	'SheetName':'IBKR 15m'  	,'IntervalSize':'1 hour'	,'Scope':'intraday'	    ,'hourConstant':1	    ,'minConstant':0.3	    ,'secConstant':0.3	    ,'leftSide':0   },		#	XX:OO:OO	Every 1  hour
                    '20 mins'	:{	'SheetName':'IBKR 20m'  	,'IntervalSize':'1 hour'	,'Scope':'intraday'	    ,'hourConstant':1	    ,'minConstant':0.3	    ,'secConstant':0.3	    ,'leftSide':0   },		#	XX:OO:OO	Every 1  hour
                    '30 mins'	:{	'SheetName':'IBKR 30m'	    ,'IntervalSize':'2 hours'	,'Scope':'intraday'	    ,'hourConstant':2	    ,'minConstant':0.3	    ,'secConstant':0.3	    ,'leftSide':-0.38   },		#	O2:OO:OO	Every 2  hour
                    '1 hour' 	:{	'SheetName':'IBKR 1H'	    ,'IntervalSize':'2 hours'	,'Scope':'intraday'	    ,'hourConstant':8	    ,'minConstant':0.3	    ,'secConstant':0.3	    ,'leftSide':-0.51   },		#	O2:OO:OO	Every 2  hour
                    '2 hours'	:{	'SheetName':'IBKR 2H'   	,'IntervalSize':'1 day'	    ,'Scope':'daily'	    ,'hourConstant':3	    ,'minConstant':0.3	    ,'secConstant':0.3	    ,'leftSide':0   },		#	O4:OO:OO	Every 1  day
                    '3 hours'	:{	'SheetName':'IBKR 3H'	    ,'IntervalSize':'1 day'	    ,'Scope':'daily'	    ,'hourConstant':13	    ,'minConstant':0.3	    ,'secConstant':0.3	    ,'leftSide':0   },		#	O4:OO:OO	Every 1  day
                    '4 hours'	:{	'SheetName':'IBKR 4H'   	,'IntervalSize':'1 day'	    ,'Scope':'daily'	    ,'hourConstant':11	    ,'minConstant':0.3	    ,'secConstant':0.3	    ,'leftSide':0   },		#	O4:OO:OO	Every 1  day
                    '8 hours'	:{	'SheetName':'IBKR 8H'	    ,'IntervalSize':'1 day'	    ,'Scope':'daily'	    ,'hourConstant':0.3	    ,'minConstant':0.3	    ,'secConstant':0.3	    ,'leftSide':0   },		#	O4:OO:OO	Every 1  day
                    '1 day' 	:{	'SheetName':'IBKR 1Day'	    ,'IntervalSize':'1 week'	,'Scope':'weekly'	    ,'hourConstant':1	    ,'minConstant':0.3	    ,'secConstant':0.3	    ,'leftSide':-0.41   },		#	O4:OO:OO	Every 1  week
                    '1W'    	:{	'SheetName':'IBKR 1week'	,'IntervalSize':'1 month'	,'Scope':'monthly'	    ,'hourConstant':1	    ,'minConstant':0.3	    ,'secConstant':0.3	    ,'leftSide':0   },		#	O4:OO:OO	Every 1  month
                    '1M'     	:{	'SheetName':'IBKR 1Month'   ,'IntervalSize':'1 year'	,'Scope':'yearly'	    ,'hourConstant':1	    ,'minConstant':0.3	    ,'secConstant':0.3	    ,'leftSide':0   },		#	O4:OO:OO	Every 1  year
                                                                                                            
                    '1m'     	:{	'SheetName':'Yahoo 1m'	    ,'IntervalSize':'5 min'	    ,'Scope':'intraday'	    ,'hourConstant':1	    ,'minConstant':5	    ,'secConstant':0.3	    ,'leftSide':0   },		#	XX:O5:OO	Every 5  min
                    '2m'     	:{	'SheetName':'Yahoo 2m'	    ,'IntervalSize':'10 min'	,'Scope':'intraday'	    ,'hourConstant':1	    ,'minConstant':10	    ,'secConstant':0.3	    ,'leftSide':0   },		#	XX:10:OO	Every 10 min
                    '5m'     	:{	'SheetName':'Yahoo 5m'	    ,'IntervalSize':'15 min'	,'Scope':'intraday'	    ,'hourConstant':1	    ,'minConstant':15	    ,'secConstant':0.3	    ,'leftSide':0   },		#	XX:15:OO	Every 15 min
                    '15m'   	:{	'SheetName':'Yahoo 15m'	    ,'IntervalSize':'1 hour'	,'Scope':'intraday'	    ,'hourConstant':1	    ,'minConstant':0.3	    ,'secConstant':0.3	    ,'leftSide':-0.21   },		#	XX:OO:OO	Every 1  hour
                    '30m'   	:{	'SheetName':'Yahoo 30m'	    ,'IntervalSize':'2 hours'	,'Scope':'intraday'	    ,'hourConstant':1	    ,'minConstant':0.3	    ,'secConstant':0.3	    ,'leftSide':0   },		#	O2:OO:OO	Every 2  hour
                    '1h'     	:{	'SheetName':'Yahoo Hours'	,'IntervalSize':'2 hours'	,'Scope':'daily'	    ,'hourConstant':1	    ,'minConstant':0.3	    ,'secConstant':0.3	    ,'leftSide':0   },		#	O2:OO:OO	Every 2  hour
                    '1d'     	:{	'SheetName':'Yahoo Dayes'	,'IntervalSize':'1 week'	,'Scope':'monthly'	    ,'hourConstant':1	    ,'minConstant':0.3	    ,'secConstant':0.3	    ,'leftSide':0   }		#	O4:OO:OO	Every 1  week
                }

    outLable =  {   
                    'ticks':[],
                    'tlabs':[],
                    'mitks':[],
                    'milab':[]
                }


    if(source in srcIndex) :
        print("source is ",source)
        if(interval in ntrvlHub) :
            print("interval is ",interval)
            print("Scope is ",ntrvlHub[interval]["Scope"])

            for i in range (len(inList)) : 
                # Set Varibles
                #------------------------------------------------
                if(interval in ['1 secs','5 secs','10 secs','15 secs','30 secs','1 min','2 mins','3 mins','5 mins','10 mins','15 mins','20 mins','30 mins','1 hour',
                                '2 hours','3 hours','4 hours','8 hours','1m','2m','5m','15m','30m','1h']
                    ):
                        # print(inList[i])
                        currentSecond   = (int(inList[i][(srcIndex[source]['s1']):(srcIndex[source]["s2"])]))   
                        # print("current Second = ","%02d"%currentSecond)
                        currentMinute   = (int(inList[i][(srcIndex[source]["m1"]):(srcIndex[source]["m2"])]))
                        # print("current Minute = ","%02d"%currentMinute)
                        currentHour     = (int(inList[i][(srcIndex[source]["H1"]):(srcIndex[source]["H2"])]))
                        # print("current Hour = ","%02d"%currentHour)
                        currentLable    =  str("%02d"%currentHour) + ':' + str("%02d"%currentMinute)      # lable HH:MM
                
                
                currentDay      = (int(inList[i][(srcIndex[source]["D1"]):(srcIndex[source]["D2"])])) 
                # print("current Day) = ","%02d"%currentDay)
                currentMonth    = (int(inList[i][(srcIndex[source]["M1"]):(srcIndex[source]["M2"])])) 
                # print("current Month = ","%02d"%currentMonth)
                currentYear     = (int(inList[i][(srcIndex[source]["Y1"]):(srcIndex[source]["Y2"])]))  
                # print("current Year = ","%02d"%currentYear)
                #------------------------------------------------
                if(i==0):
                        lastDay      = currentDay 
                        lastMonth    = currentMonth
                        lastYear     = currentYear
                elif(i>0):
                        lastDay      = (int(inList[i-1][(srcIndex[source]["D1"]):(srcIndex[source]["D2"])])) 
                        lastMonth    = (int(inList[i-1][(srcIndex[source]["M1"]):(srcIndex[source]["M2"])])) 
                        lastYear     = (int(inList[i-1][(srcIndex[source]["Y1"]):(srcIndex[source]["Y2"])])) 
                #------------------------------------------------
                
                dayLable        =  monthName[currentMonth] + '.' + str("%02d"%currentDay)        # lable MM.DD
                yearLable       = str(currentYear) + '.' + dayLable                    # lable YYYY.MM.DD
                #------------------------------------------------


                if(ntrvlHub[interval]["Scope"] == 'intraday'):
                    # print("Scope is ",ntrvlHub[interval]["Scope"])
                    #__________________________________________
                    #   Day lable:
                    # print("____")
                    # print(currentYear,currentMonth,currentDay)
                    # print(lastYear,lastMonth,lastDay)
                    
                    if(     currentYear  >  lastYear        #   Year   Change:
                        or   currentMonth >  lastMonth       #   Month  Change:
                        or   currentDay   >  lastDay         #   Day    Change:
                       ):
                                # print("@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@")
                                if(     currentYear  >  lastYear    #   Year   Change:
                                    ):
                                        condLable = yearLable
                                else:
                                        condLable = dayLable
                                outLable["ticks"].append(i+ntrvlHub[interval]['leftSide'])
                                outLable["tlabs"].append("\n \n " +currentLable)
                                outLable["mitks"].append(i-0.1)   
                                outLable["milab"].append("\n \n " +condLable)                                                 
                    #__________________________________________
                    #   clock lable:
                    elif(       (( currentSecond % ntrvlHub[interval]["secConstant"]  ) == 0)     # Seconds   Condition
                            &   (( currentMinute % ntrvlHub[interval]["minConstant"]  ) == 0)     # Minutes   Condition
                            &   (( currentHour   % ntrvlHub[interval]["hourConstant"] ) == 0)     # Hours     Condition
                        ):
                                if(     tickFlag  == True                        #   First  Candel:
                                    # or   currentYear  >  lastYear    #   Year   Change:
                                    ):
                                        tickFlag  =  False
                                        condLable =  currentLable   #.replace('\n', '')
                                else:
                                        tickFlag  =  True
                                        condLable =  '\n' + currentLable 
                                
                                outLable["ticks"].append(i+ntrvlHub[interval]['leftSide'])
                                outLable["tlabs"].append(condLable)
                                # print(i)
                                # print(currentLable) 
                    #__________________________________________
                    
                            
            
                elif(ntrvlHub[interval]["Scope"] == 'daily'):
                    # print("Scope is ",ntrvlHub[interval]["Scope"])
                    #__________________________________________
                    #   Day lable:
                    if(     i==0                            #   First  Candel:
                        or   currentYear  >  lastYear        #   Year   Change:
                        or   currentMonth >  lastMonth       #   Month  Change:
                        or   currentDay   >  lastDay         #   Day    Change:
                       ):
                                
                                if(     i==0                        #   First  Candel:
                                    or   currentYear  >  lastYear    #   Year   Change:
                                    ):
                                        condLable = yearLable
                                else:
                                        condLable = dayLable
                                outLable["ticks"].append(i+ntrvlHub[interval]['leftSide'])
                                outLable["tlabs"].append("\n \n " + currentLable)
                                outLable["mitks"].append(i-0.1)   
                                outLable["milab"].append("\n " + condLable)                                                 
                    #__________________________________________
                    #   clock lable:
                    elif(       (( currentSecond % ntrvlHub[interval]["secConstant"]  ) == 0)     # Seconds   Condition
                            &   (( currentMinute % ntrvlHub[interval]["minConstant"]  ) == 0)     # Minutes   Condition
                            &   (( currentHour   % ntrvlHub[interval]["hourConstant"] ) == 0)     # Hours     Condition
                        ):
                                outLable["ticks"].append(i+ntrvlHub[interval]['leftSide'])
                                outLable["tlabs"].append(currentLable)
                                # print(i)
                                # print(currentLable) 
                    #__________________________________________


                elif(ntrvlHub[interval]["Scope"] == 'weekly'):
                    # print("Scope is ",ntrvlHub[interval]["Scope"])
                    #__________________________________________
                    #   Day lable:
                    if(         i==0                            #   First  Candel:
                        or       currentYear  >  lastYear        #   Year   Change:
                        or       currentMonth >  lastMonth       #   Month  Change: 
                       ):
                                
                                if(     i==0                        #   First  Candel:
                                    or   currentYear  >  lastYear    #   Year   Change:
                                    ):
                                        condLable = "\n \n " + yearLable.replace('\n', '')
                                else:                               #   Month  Change: 
                                        condLable = "\n \n " + dayLable.replace('\n', '')
                                        if(i % 5 == 0):
                                                # print("_____1_____")
                                                if( i%2==0):                        #   First  Candel:                                                
                                                    tCondLable = dayLable.replace('\n', '')
                                                    # print("_____2_____")
                                                else:
                                                    # print("_____3_____")
                                                    tCondLable = dayLable        
                                                outLable["ticks"].append(i+ntrvlHub[interval]['leftSide'])
                                                outLable["tlabs"].append(tCondLable)

                                outLable["mitks"].append(i+ntrvlHub[interval]['leftSide']-0.2)
                                outLable["milab"].append(condLable)
                                                                                
                    #__________________________________________
                    #   Week lable:
                    elif(       i % 5 == 0        #   Day    Change: currentDay
                        ):
                                if(     i%2==0                        #   First  Candel:
                                    # or   currentYear  >  lastYear    #   Year   Change:
                                    ):
                                        condLable = dayLable.replace('\n', '')
                                else:
                                        condLable = dayLable        
                                outLable["ticks"].append(i+ntrvlHub[interval]['leftSide'])
                                outLable["tlabs"].append(condLable)
                                # print(i)
                                # print(dayLable) 
                    #__________________________________________


                elif(ntrvlHub[interval]["Scope"] == 'monthly'):
                    # print("Scope is ",ntrvlHub[interval]["Scope"])
                    #__________________________________________
                    #   Day lable:
                    if(         i==0                            #   First  Candel:
                        |       currentYear  >  lastYear        #   Year   Change:
                        |       currentMonth >  lastMonth       #   Month  Change: 
                       ):
                                
                                if(     i==0                        #   First  Candel:
                                    |   currentYear  >  lastYear    #   Year   Change:
                                    ):
                                        condLable = yearLable
                                else:
                                        condLable = dayLable
                                outLable["ticks"].append(i+ntrvlHub[interval]['leftSide'])
                                outLable["tlabs"].append(condLable)                                                
                    #__________________________________________


                elif(ntrvlHub[interval]["Scope"] == 'yearly'):
                    # print("Scope is ",ntrvlHub[interval]["Scope"])
                    #__________________________________________
                    #   Day lable:
                    if(         i==0                            #   First  Candel:
                        |       currentYear  >  lastYear        #   Year   Change:
                       ):
                                outLable["ticks"].append(i+ntrvlHub[interval]['leftSide'])
                                outLable["tlabs"].append(yearLable)                                                
                    #__________________________________________

                elif(ntrvlHub[interval]["Scope"] == 'interday'):
                    print("Scope is ",ntrvlHub[interval]["Scope"])


                '''
                if(ntrvlHub[interval].Scope == 'intraday'):
                    print("Scope is ",ntrvlHub[interval].Scope)
                    if  (       (( currentSecond % ntrvlHub[interval].secConstant  ) == 0)     # Seconds   Condition
                            &   (( currentMinute % ntrvlHub[interval].minConstant  ) == 0)     # Minutes   Condition
                            &   (( currentHour   % ntrvlHub[interval].hourConstant ) == 0)     # Hours     Condition
                        ):
                                currentLable =  str(currentHour) + ':' + str(currentMinute) # lable HH:MM
                                outLable.ticks.append(i)
                                outLable.tlabs.append(currentLable)
                                print(i)
                                print(currentLable) 

                    if  (       (i+1)in range (len(inList)) ):
                                j=i+1 
                                nextDay      = (int(inList[j][(srcIndex[source].D1):(srcIndex[source].D2)])) 
                                nextMonth    = (int(inList[j][(srcIndex[source].M1):(srcIndex[source].M2)])) 
                                nextYear     = (int(inList[j][(srcIndex[source].Y1):(srcIndex[source].Y2)]))  
                                if(                 nextMonth>currentMonth      #   Month   changed
                                        |           nextDay>currentDay          #   day     changed     
                                    ): 
                                            dayLable =  monthName[nextMonth] + '.' + str(nextDay)
                                            if(     nextYear>currentYear):      #   year    changed 
                                                dayLable = str(nextYear) + '.' + dayLable
                                            outLable.mitks.append(j)
                                            outLable.milab.append(dayLable)
 
                '''




        else:
            print("interval is Wrong")
    else:
        print("source is Wrong")

    return outLable







def fTest2():


    df = yf.download('DIA',start='2024-02-28',end='2024-03-15',interval='15m')
    print(df)

    ticks = []
    tlabs = []
    dates = sorted(list(set([d.date() for d in df.index])))



    print("*********@@@**********")
    grogro = []

    grogro = list (df.index.map(str))

    outLable = fTimeLable  (   source="Yahoo",
                                interval='15m',
                                inList=grogro
                            )

    

    # fig, axlist = mpf.plot(df,type='candle',xrotation=0,style='yahoo',tight_layout=True,returnfig=True)
    fig, axlist = mpf.plot(df,type='candle',xrotation=0,style='yahoo',tight_layout=True,returnfig=True,figratio=(2,1))
    # axlist[-2].set_xticks(outLable["ticks"],labels=outLable["tlabs"],ha='center',kl=0)

    axlist[-2].set_xticks(outLable["ticks"])
    axlist[-2].set_xticklabels(outLable["tlabs"], ha='center')
    axlist[-2].set_xticks(outLable["mitks"],minor=True)
    axlist[-2].set_xticklabels(outLable["milab"], ha='center', minor=True, rotation=0)    

    mpf.show()
    print("**________***")
    print(type( axlist[-2]))
    print(outLable["tlabs"])
    print(outLable["milab"])

        




def tTest3():

    df = yf.download('DIA',start='2024-02-28',end='2024-03-15',interval='15m')
    print(df)

    ticks = []
    tlabs = []
    mitks = []
    milab = []
    dates = sorted(list(set([d.date() for d in df.index])))

    for d1 in dates:

        # Major Ticks:
        d2 = d1 + datetime.timedelta(days=1)
        ts = df.loc[d1:d2].index[0]
        ticks.append(df.index.get_loc(ts))
        # line feed at beginning of label so it appears a lower below the x-axis:
        tlabs.append('\n'+d1.strftime('%b %d'))

        # Minor Ticks:
        mitks.append(ticks[-1]+0.1)
        milab.append('09:30')
        ts = df.loc[str(d1)+' 13:00':d2].index[0]
        mitks.append(df.index.get_loc(ts))
        milab.append('13:00')

    fig, axlist = mpf.plot(df,type='candle',xrotation=0,style='yahoo',tight_layout=True,returnfig=True,figratio=(2,1))

    axlist[-2].set_xticks(ticks)
    axlist[-2].set_xticklabels(tlabs, ha='left')
    axlist[-2].set_xticks(mitks,minor=True)
    axlist[-2].set_xticklabels(milab, ha='center', minor=True, rotation=0)

    print("***________***")
    print(ticks)
    print(tlabs)
    print("***________***")
    print(mitks)
    print(milab)

    mpf.show()


# fTest2()
# tTest3()
    
    