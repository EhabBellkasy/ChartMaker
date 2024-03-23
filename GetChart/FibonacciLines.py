
import yfinance as yf
import mplfinance as mpf
import ImportData
import ta



class FiboClass():
    
    def __init__(self):
        self.fibolines=dict( hlines=(0, 0, 0, 0, 0, 0, 0),
                        colors=['#4ACE14','#E21919','#27DFDD', '#E6F226', '#27DFDD', '#E21919','#4ACE14'],
                        linestyle='solid',
                        linewidths=3,
                        alpha= 0.8 
                    )
        self.HighLow =   {
                        "Last5Year"	    :{	"High":	0.00	,	"Low":	0.00	},
                        "Last1Year"	    :{	"High":	0.00	,	"Low":	0.00	},
                        "Last1Month"	:{	"High":	0.00	,	"Low":	0.00	},
                        "Last1Week" 	:{	"High":	0.00	,	"Low":	0.00	},
                        "Yesterday"	    :{	"High":	0.00	,	"Low":	0.00	},
                        "PreMarketI"	:{	"High":	0.00	,	"Low":	0.00	},
                        "PreMarketII"	:{	"High":	0.00	,	"Low":	0.00	},
                        "MarketOpen"	:{	"High":	0.00	,	"Low":	0.00	},
                        "Midday"	    :{	"High":	0.00	,	"Low":	0.00	},
                        "PowerHour"	    :{	"High":	0.00	,	"Low":	0.00	},
                        "AfterMarketI"	:{	"High":	0.00	,	"Low":	0.00	},
                        "AfterMarketII"	:{	"High":	0.00	,	"Low":	0.00	},
                        "Final"	        :{	"High":	0.00	,	"Low":	0.00	},
                        "Random1"	    :{	"High":	0.00	,	"Low":	0.00	},
                        "Random2"	    :{	"High":	0.00	,	"Low":	0.00	},
                        "Random3"	    :{	"High":	0.00	,	"Low":	0.00	},
                        "Random4"	    :{	"High":	0.00	,	"Low":	0.00	},
                        "Random5"	    :{	"High":	0.00	,	"Low":	0.00	}
                    }



def fun (filePath_fun) :
                
        #Make a fibonacci lines
        # Link: https://github.com/matplotlib/mplfinance/blob/master/examples/using_lines.ipynb
        #------------------------------------------------
        # NOT FINSH
        
        fibolines=dict( hlines=(2.75, 2.65, 2.55, 2.45, 2.35, 2.25, 2.15),
                        colors=['#4ACE14','#E21919','#27DFDD', '#E6F226', '#27DFDD', '#E21919','#4ACE14'],
                        linestyle='solid',
                        linewidths=3,
                        alpha= 0.8 
                    )






        return fibolines





def fun2(   filePath_fun 
            ,Fobi_Input
            ,DaySheetName = "IBKR 1Day" 
            ,fibonacciIndex = "MarketOpen"
            ,fibonacciBook ={
                                "Last5Year"	    :{	'SheetName':	'IBKR 1Month'	,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-61	,	"EndDelta":	-1			},
                                "Last1Year"	    :{	'SheetName':	'IBKR 1Month'	,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-13	,	"EndDelta":	-1			},
                                "Last1Month"	:{	'SheetName':	'IBKR 1Day'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-31	,	"EndDelta":	-2			},
                                "Last1Week"	    :{	'SheetName':	'IBKR 1Day'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-6	,	"EndDelta":	-2			},
                                "Yesterday"	    :{	'SheetName':	'IBKR 4H'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-2	,	"EndDelta":	-1			},
                                "PreMarketI"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"04:00:00"	,	"PeriodEnd":	"06:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-2	,	"EndDelta":	-1			},
                                "PreMarketII"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"06:00:00"	,	"PeriodEnd":	"08:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"06:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                "MarketOpen"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"09:00:00"	,	"PeriodEnd":	"10:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"09:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                "Midday"	    :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"10:00:00"	,	"PeriodEnd":	"14:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"10:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                "PowerHour"	    :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"14:00:00"	,	"PeriodEnd":	"16:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"14:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                "AfterMarketI"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"16:00:00"	,	"PeriodEnd":	"18:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"16:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                "AfterMarketII"	:{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"18:00:00"	,	"PeriodEnd":	"20:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"18:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                "Final"	        :{	'SheetName':	'IBKR 30m'	    ,	"PeriodStart":	"20:00:00"	,	"PeriodEnd":	"00:00:00"	,	"TimeStart":	"04:00:00"	,	"TimeEnd":	"20:00:00"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                "Random1"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                "Random2"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                "Random3"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                "Random4"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			},
                                "Random5"	    :{	'SheetName':	'IBKR 8H'	    ,	"PeriodStart":	"XX:XX:XX"	,	"PeriodEnd":	"XX:XX:XX"	,	"TimeStart":	"XX:XX:XX"	,	"TimeEnd":	"XX:XX:XX"	,	"StartDelta":	-1	,	"EndDelta":	-1			}
                            }
        ) :
        '''
            last 5 year     04:00-20:00
            last 1 year     04:00-20:00
            last 1 month    04:00-20:00
            last 1 week     04:00-20:00
            yesterday       04:00-20:00
            Pre-MarketI     04:00-06:00
            Pre-MarketII    06:00-08:00	
            Market Open     09:00-10:00
            Midday          10:00-14:00
            Power Hour      14:00-16:00
            After MarketI   16:00-18:00
            After MarketII  18:00-20:00
            Final           20:00-00:00
            Random1         XX:XX-XX:XX
            Random2         XX:XX-XX:XX
            Random3         XX:XX-XX:XX
            Random4         XX:XX-XX:XX
            Random5         XX:XX-XX:XX    

        '''
                
        #Make a fibonacci lines
        # Link: https://github.com/matplotlib/mplfinance/blob/master/examples/using_lines.ipynb
        #------------------------------------------------
        # NOT FINSH
        #------------------------------------------------
        # 0- Ist need fibonacci lines?
        if(fibonacciIndex in fibonacciBook):
            print("it need fibonacci lines")
        # 1- Ist the first time? Import  data or Recall Data?        
            # Import  data
            if(        (Fobi_Input.HighLow[fibonacciIndex]["High"] == 0)
                   and (Fobi_Input.HighLow[fibonacciIndex]["Low"]  == 0) ):
                    print("Import Data")
                
                    dfD = ImportData.fun2 (filePath_fun = filePath_fun , bookName = DaySheetName) # "IBKR 1Day"
                    if(len(dfD.index)==0):
                        if(DaySheetName == "IBKR 1Day"):
                            DaySheetName = "Yahoo Dayes"
                            dfD = ImportData.fun (filePath_fun = filePath_fun , bookName = DaySheetName )   # "Yahoo Dayes"
                        elif(DaySheetName == "Yahoo Dayes"):
                            DaySheetName = "IBKR 1Day"
                            dfD = ImportData.fun2 (filePath_fun = filePath_fun , bookName = DaySheetName )   # "Yahoo Dayes"
                        else:
                            print("Wrong Day Sheet Name")
                        # dfD = ImportData.fun2 (filePath_fun = filePath_fun , bookName = DaySheetName )   # "Yahoo Dayes"
                    EDay = str( dfD.index[fibonacciBook[fibonacciIndex]["EndDelta"]] )
                    SDay = str( dfD.index[fibonacciBook[fibonacciIndex]["StartDelta"]] )
                    
                    # print(">>>>>>","@@@","<<<<<<")
                    # print(dfD)
                    # print(SDay)

                    ETime=EDay[0:11] + fibonacciBook[fibonacciIndex]["TimeEnd"]  
                    STime=SDay[0:11] + fibonacciBook[fibonacciIndex]["TimeStart"]
                    

                    dfT = ImportData.fun2 (filePath_fun = filePath_fun , bookName = fibonacciBook[fibonacciIndex]['SheetName'])    #   'YAHOO'      'IBKR 30m'  IBKR 1H
                    df = dfT[STime:ETime] #XXXXXXXX
                    
                    High = Fobi_Input.HighLow[fibonacciIndex]["High"] = df['High'].max()
                    Low  = Fobi_Input.HighLow[fibonacciIndex]["Low"]  = df['Low'].min()

                    # print(">>>>>>","@@@","<<<<<<")
                    # print(df)
                    # print(High)
                    # print(Low)
                    # print(Low22)
                    # print(">>>>>>","@@@","<<<<<<")

            # Recall Data
            else:
                    print("Import Data")
                    High = Fobi_Input.HighLow[fibonacciIndex]["High"]
                    Low  = Fobi_Input.HighLow[fibonacciIndex]["Low"]
        else:
            print("it dont need fibonacci lines")
            High = 0
            Low  = 0

        # High=437.05
        # Low=429.05

        # 2- Culclate fibonacci lines   Help Link :-  https://eodhd.com/financial-academy/technical-analysis-examples/fibonacci-sequence-in-trading-with-python/
        #------------------------------------------------
        '''
            # Help Link :-  https://eodhd.com/financial-academy/technical-analysis-examples/fibonacci-sequence-in-trading-with-python/
            Fib100 = Low + ((High - Low) * 1.000 )
            Fib764 = Low + ((High - Low) * 0.764 )
            Fib618 = Low + ((High - Low) * 0.618 )
            Fib500 = Low + ((High - Low) * 0.500 )
            Fib382 = Low + ((High - Low) * 0.382 )
            Fib236 = Low + ((High - Low) * 0.236 )
            Fib000 = Low + ((High - Low) * 0.000 )

            Fib100 = Low + ((High - Low) * 1.000 )
            Fib764 = Low + ((High - Low) * 0.764 )
            Fib618 = Low + ((High - Low) * 0.618 )
            Fib500 = Low + ((High - Low) * 0.500 )
            Fib382 = Low + ((High - Low) * 0.382 )
            Fib236 = Low + ((High - Low) * 0.236 )
            Fib000 = Low + ((High - Low) * 0.000 )
            

        '''
        
        Fib100 = {'Value':(Low + ((High - Low) * 1.000 ))  ,'linestyle':'solid'  ,'linewidth':3   ,'alpha':0.8   ,'color':'#4ACE14'}
        Fib764 = {'Value':(Low + ((High - Low) * 0.764 ))  ,'linestyle':'solid'  ,'linewidth':3   ,'alpha':0.8   ,'color':'#E21919'}
        Fib618 = {'Value':(Low + ((High - Low) * 0.618 ))  ,'linestyle':'solid'  ,'linewidth':3   ,'alpha':0.8   ,'color':'#27DFDD'}
        Fib500 = {'Value':(Low + ((High - Low) * 0.500 ))  ,'linestyle':'solid'  ,'linewidth':3   ,'alpha':0.8   ,'color':'#E6F226'}
        Fib382 = {'Value':(Low + ((High - Low) * 0.382 ))  ,'linestyle':'-.'     ,'linewidth':3   ,'alpha':0.8   ,'color':'#27DFDD'}
        Fib236 = {'Value':(Low + ((High - Low) * 0.236 ))  ,'linestyle':'-.'     ,'linewidth':3   ,'alpha':0.8   ,'color':'#E21919'}
        Fib000 = {'Value':(Low + ((High - Low) * 0.000 ))  ,'linestyle':'-.'     ,'linewidth':3   ,'alpha':0.8   ,'color':'#4ACE14'}
        # print(">>>>>>","@@@","<<<<<<")
        # print(High)
        # print(Low)
        # print(Fib100)
        # print(Fib764)
        # print(Fib618)
        # print(Fib500)
        # print(Fib382)
        # print(Fib236)
        # print(Fib000)
        # print(">>>>>>","@@@","<<<<<<")
        
        
        # 3- Make  fibonacci lines
        #------------------------------------------------
        '''
        fibolines=dict( hlines=(Fib100, Fib764, Fib618, Fib500, Fib382, Fib236, Fib000),
                        colors=['#4ACE14','#E21919','#27DFDD', '#E6F226', '#27DFDD', '#E21919','#4ACE14'],
                        linestyle='solid',
                        linewidths=3,
                        alpha= 0.8 
                    )
        
        
        fibolines=dict( hlines      =(438        ,436        ,434        ,432        ,430        ,425       ,420),
                        colors      =['#4ACE14'  ,'#E21919'  ,'#27DFDD'  ,'#E6F226'  ,'#27DFDD'  ,'#E21919' ,'#4ACE14'],
                        linestyle   =['solid'    ,'solid'    ,'solid'    ,'solid'    ,'-.'       ,'-.'      ,'-.'],
                        linewidths  =[3          ,3          ,3          ,3          ,3          ,3         ,3],
                        alpha       =[0.8        ,0.8        ,0.8        ,0.8        ,0.8        ,0.8       ,0.8]
                    )
        
        
        '''
        
        Fobi_Input.fibolines=dict   (    hlines      =(Fib100['Value']       ,Fib764['Value']        ,Fib618['Value']        ,Fib500['Value']        ,Fib382['Value']        ,Fib236['Value']        ,Fib000['Value'])
                                        ,colors      =[Fib100['color']       ,Fib764['color']        ,Fib618['color']        ,Fib500['color']        ,Fib382['color']        ,Fib236['color']        ,Fib000['color']]
                                        ,linestyle   =[Fib100['linestyle']   ,Fib764['linestyle']    ,Fib618['linestyle']    ,Fib500['linestyle']    ,Fib382['linestyle']    ,Fib236['linestyle']    ,Fib000['linestyle']]
                                        ,linewidths  =[Fib100['linewidth']   ,Fib764['linewidth']    ,Fib618['linewidth']    ,Fib500['linewidth']    ,Fib382['linewidth']    ,Fib236['linewidth']    ,Fib000['linewidth']]
                                        ,alpha       =[Fib100['alpha']       ,Fib764['alpha']        ,Fib618['alpha']        ,Fib500['alpha']        ,Fib382['alpha']        ,Fib236['alpha']        ,Fib000['alpha']]
                                    )

        return Fobi_Input



