
import yfinance as yf
import mplfinance as mpf
import ImportData
import ta
from datetime import datetime,date, timedelta



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



#________________________________________________________________________________________________________________________________________________________________________________________________

class FiboClass2():
    
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
                        "CurrentYear"   :{	"High":	0.00	,	"Low":	0.00	},
                        "Last1Month"	:{	"High":	0.00	,	"Low":	0.00	},
                        "CurrentMonth"	:{	"High":	0.00	,	"Low":	0.00	},
                        "Last1Week" 	:{	"High":	0.00	,	"Low":	0.00	},
                        "CurrentWeek" 	:{	"High":	0.00	,	"Low":	0.00	},
                        "Yesterday"	    :{	"High":	0.00	,	"Low":	0.00	},
                        "PreMarketI"	:{	"High":	0.00	,	"Low":	0.00	},
                        "PreMarketII"	:{	"High":	0.00	,	"Low":	0.00	},
                        "MarketOpen"	:{	"High":	0.00	,	"Low":	0.00	},
                        "Midday"	    :{	"High":	0.00	,	"Low":	0.00	},
                        "PowerHour"	    :{	"High":	0.00	,	"Low":	0.00	},
                        "AfterMarketI"	:{	"High":	0.00	,	"Low":	0.00	},
                        "AfterMarketII"	:{	"High":	0.00	,	"Low":	0.00	},
                        "Final"	        :{	"High":	0.00	,	"Low":	0.00	},
                        "EMA200"	    :{	"High":	0.00	,	"Low":	0.00	},
                        "Random1"	    :{	"High":	0.00	,	"Low":	0.00	},
                        "Random2"	    :{	"High":	0.00	,	"Low":	0.00	},
                        "Random3"	    :{	"High":	0.00	,	"Low":	0.00	},
                        "Random4"	    :{	"High":	0.00	,	"Low":	0.00	},
                        "Random5"	    :{	"High":	0.00	,	"Low":	0.00	}
                    }

    def HLday ( self 
                ,dfD
                ,dfT 
                # ,filepath_xl
                ,showOutPut = True
                ,dayIndex = "MarketOpen"
                ,dayList = ["Yesterday","PreMarketI","PreMarketII","MarketOpen","Midday","PowerHour","AfterMarketI","AfterMarketII","Final"]
                ,dayBook =  {
                                "Yesterday"	    :{"TimeStart":"04:00:00" ,"TimeEnd":"20:00:00" ,"StartDelta":-2	,"EndDelta":-2},
                                "PreMarketI"	:{"TimeStart":"04:00:00" ,"TimeEnd":"06:00:00" ,"StartDelta":-1	,"EndDelta":-1},
                                "PreMarketII"	:{"TimeStart":"04:00:00" ,"TimeEnd":"08:00:00" ,"StartDelta":-1	,"EndDelta":-1},
                                "MarketOpen"	:{"TimeStart":"04:00:00" ,"TimeEnd":"09:00:00" ,"StartDelta":-1	,"EndDelta":-1},
                                "Midday"	    :{"TimeStart":"04:00:00" ,"TimeEnd":"10:00:00" ,"StartDelta":-1	,"EndDelta":-1},
                                "PowerHour"	    :{"TimeStart":"04:00:00" ,"TimeEnd":"14:00:00" ,"StartDelta":-1	,"EndDelta":-1},
                                "AfterMarketI"	:{"TimeStart":"04:00:00" ,"TimeEnd":"16:00:00" ,"StartDelta":-1	,"EndDelta":-1},
                                "AfterMarketII" :{"TimeStart":"04:00:00" ,"TimeEnd":"18:00:00" ,"StartDelta":-1	,"EndDelta":-1},
                                "Final"	        :{"TimeStart":"04:00:00" ,"TimeEnd":"20:00:00" ,"StartDelta":-1	,"EndDelta":-1}
                            }
                ):

        for dayIndex in dayList :
            EDay = str( dfD.index[dayBook[dayIndex]["EndDelta"]] )
            SDay = str( dfD.index[dayBook[dayIndex]["StartDelta"]] )
            ETime=EDay + " " + dayBook[dayIndex]["TimeEnd"]  
            STime=SDay + " " + dayBook[dayIndex]["TimeStart"]
            if(showOutPut):print(STime)
            if(showOutPut):print(ETime)
            df = dfT[STime:ETime] #XXXXXXXX
            High = self.HighLow[dayIndex]["High"] = df['High'].max()
            Low  = self.HighLow[dayIndex]["Low"]  = df['Low'].min()
            if(showOutPut):print(dayIndex,"High",High)
            if(showOutPut):print(dayIndex,"Low",Low)

    def HLweek ( self 
                ,dfD
                ,dfT 
                # ,filepath_xl
                ,showOutPut = True
                ):
        # last_day= date(2024, 4, 8)
        last_day = dfD.index[-1]
        last_day = datetime.strptime(last_day, '%Y-%m-%d').date()
        if(showOutPut):print(last_day.year,last_day.month,last_day.day)

        temp_Monday = last_day + timedelta(days = 0 - last_day.weekday())
        temp_Sunday = last_day + timedelta(days = 6 - last_day.weekday())

        monday_list = []
        Sunday_list = []

        monday_list.append(str(temp_Monday))
        Sunday_list.append(str(temp_Sunday))

        for i in range( 2 ):
            temp_Monday -= timedelta(days = 7)
            temp_Sunday -= timedelta(days = 7)

            monday_list.append(str(temp_Monday))
            Sunday_list.append(str(temp_Sunday))

        if(showOutPut):print(monday_list)
        if(showOutPut):print(Sunday_list)

        # dfT = ImportData.fun2 (filePath_fun = filepath_xl , bookName = 'IBKR 30m')    #   'YAHOO'      'IBKR 30m'  IBKR 1H

        # CurrentWeek
        STime=monday_list[0] + ' ' + "04:00:00"
        ETime=Sunday_list[0] + ' ' + "20:00:00"        
        df = dfT[STime:ETime] #XXXXXXXX
        High = self.HighLow["CurrentWeek"]["High"] = df['High'].max()
        Low  = self.HighLow["CurrentWeek"]["Low"]  = df['Low'].min()
        if(showOutPut):print("CurrentWeek","High",High)
        if(showOutPut):print("CurrentWeek","Low",Low)

        # Last1Week
        STime=monday_list[1] + ' ' + "04:00:00"
        ETime=Sunday_list[1] + ' ' + "20:00:00"        
        df = dfT[STime:ETime] #XXXXXXXX
        High = self.HighLow["Last1Week"]["High"] = df['High'].max()
        Low  =self.HighLow["Last1Week"]["Low"]  = df['Low'].min()
        if(showOutPut):print("Last1Week","High",High)
        if(showOutPut):print("Last1Week","Low",Low)

    def HLmonth ( self 
                ,dfD
                ,dfT 
                # ,filepath_xl
                ,showOutPut = True
                ):

        last_day = dfD.index[-1]
        last_day = datetime.strptime(last_day, '%Y-%m-%d').date()
        if(showOutPut):print(last_day.year,last_day.month,last_day.day)

        # CurrentMonth
        first_day = last_day.replace(day=1)    #Help Link :-   https://stackoverflow.com/questions/12468823/python-datetime-setting-fixed-hour-and-minute-after-using-strptime-to-get-day
        STime = str(first_day) + ' ' + "04:00:00"
        ETime = str(last_day)  + ' ' + "20:00:00" 
        if(showOutPut):print(STime)
        if(showOutPut):print(ETime)
        df = dfT[STime:ETime] #XXXXXXXX
        High = self.HighLow["CurrentMonth"]["High"] = df['High'].max()
        Low  = self.HighLow["CurrentMonth"]["Low"]  = df['Low'].min()
        if(showOutPut):print("CurrentMonth","High",High)
        if(showOutPut):print("CurrentMonth","Low",Low) 

        # Last1Month
        from dateutil.relativedelta import relativedelta
        first_LMD = first_day - relativedelta(months=1)     #Help Link :- https://www.geeksforgeeks.org/add-months-to-datetime-object-in-python/
        last_LMD  = first_day - timedelta(days = 1)
        STime = str(first_LMD) + ' ' + "04:00:00"
        ETime = str(last_LMD)  + ' ' + "20:00:00" 
        if(showOutPut):print(STime)
        if(showOutPut):print(ETime)
        df = dfT[STime:ETime] #XXXXXXXX
        High = self.HighLow["Last1Month"]["High"] = df['High'].max()
        Low  = self.HighLow["Last1Month"]["Low"]  = df['Low'].min()
        if(showOutPut):print("Last1Month","High",High)
        if(showOutPut):print("Last1Month","Low",Low)

    def HLyear ( self 
                ,dfD
                ,dfT 
                # ,filepath_xl
                ,showOutPut = True
                ):

        last_day = dfD.index[-1]
        last_day = datetime.strptime(last_day, '%Y-%m-%d').date()
        if(showOutPut):print(last_day.year,last_day.month,last_day.day)

        # CurrentYear
        first_day = last_day.replace(day=1,month=1)    #Help Link :-   https://stackoverflow.com/questions/12468823/python-datetime-setting-fixed-hour-and-minute-after-using-strptime-to-get-day
        STime = str(first_day) + ' ' + "04:00:00"
        ETime = str(last_day)  + ' ' + "20:00:00" 
        if(showOutPut):print(STime)
        if(showOutPut):print(ETime)
        df = dfD[STime:ETime] #XXXXXXXX
        High = self.HighLow["CurrentYear"]["High"] = df['High'].max()
        Low  = self.HighLow["CurrentYear"]["Low"]  = df['Low'].min()
        if(showOutPut):print("CurrentYear","High",High)
        if(showOutPut):print("CurrentYear","Low",Low) 

        # Last1Year
        from dateutil.relativedelta import relativedelta
        first_LMD = first_day - relativedelta(years=1)     #Help Link :- https://www.geeksforgeeks.org/add-months-to-datetime-object-in-python/
        last_LMD  = first_day - timedelta(days = 1)
        STime = str(first_LMD) + ' ' + "04:00:00"
        ETime = str(last_LMD)  + ' ' + "20:00:00" 
        if(showOutPut):print(STime)
        if(showOutPut):print(ETime)
        df = dfD[STime:ETime] #XXXXXXXX
        High = self.HighLow["Last1Year"]["High"] = df['High'].max()
        Low  = self.HighLow["Last1Year"]["Low"]  = df['Low'].min()
        if(showOutPut):print("Last1Year","High",High)
        if(showOutPut):print("Last1Year","Low",Low)

    def HL_EMA200 ( self 
                    ,dfD
                    ,dfT 
                    # ,filepath_xl
                    ,showOutPut = True
                ):

        self.HighLow["EMA200"]["High"] = dfD.EMA200[-1]

    def GetHighLow(  self 
                    ,dfD
                    ,dfT 
                    # ,filepath_xl
                    ,showOutPut = True
                    ):
        self.HLday      (dfD,dfT,showOutPut)
        self.HLweek     (dfD,dfT,showOutPut)
        self.HLmonth    (dfD,dfT,showOutPut)
        self.HLyear     (dfD,dfT,showOutPut)
        self.HL_EMA200  (dfD,dfT,showOutPut)

    def MakeHorizontalLine  (    self
                                ,style = "Sheet2"
                                ,fibonacciIndex = "MarketOpen"
                                ,showOutPut = True
                            ):
        # 1- Check Style
        if(style in ["Ehab","Ehab1","Sheet2"]):
            # 2- Ist need fibonacci lines?
            if(fibonacciIndex in self.HighLow):
                if(showOutPut):print("it need fibonacci lines")
                if(showOutPut):print("Import Data")
                High = self.HighLow[fibonacciIndex]["High"]
                Low  = self.HighLow[fibonacciIndex]["Low"]
            else:
                if(showOutPut):print("it dont need fibonacci lines")
                High = -100
                Low  = -100
            # 3- Culclate fibonacci lines   Help Link :-  https://eodhd.com/financial-academy/technical-analysis-examples/fibonacci-sequence-in-trading-with-python/
            Fib100 = {'Value':(Low + ((High - Low) * 1.000 ))  ,'linestyle':'solid'  ,'linewidth':3   ,'alpha':0.8   ,'color':'#4ACE14'}
            Fib764 = {'Value':(Low + ((High - Low) * 0.764 ))  ,'linestyle':'solid'  ,'linewidth':3   ,'alpha':0.8   ,'color':'#E21919'}
            Fib618 = {'Value':(Low + ((High - Low) * 0.618 ))  ,'linestyle':'solid'  ,'linewidth':3   ,'alpha':0.8   ,'color':'#27DFDD'}
            Fib500 = {'Value':(Low + ((High - Low) * 0.500 ))  ,'linestyle':'solid'  ,'linewidth':3   ,'alpha':0.8   ,'color':'#E6F226'}
            Fib382 = {'Value':(Low + ((High - Low) * 0.382 ))  ,'linestyle':'-.'     ,'linewidth':3   ,'alpha':0.8   ,'color':'#27DFDD'}
            Fib236 = {'Value':(Low + ((High - Low) * 0.236 ))  ,'linestyle':'-.'     ,'linewidth':3   ,'alpha':0.8   ,'color':'#E21919'}
            Fib000 = {'Value':(Low + ((High - Low) * 0.000 ))  ,'linestyle':'-.'     ,'linewidth':3   ,'alpha':0.8   ,'color':'#4ACE14'}
            
            # 3- Make  fibonacci lines
            self.fibolines=dict   (      hlines      =(Fib100['Value']       ,Fib764['Value']        ,Fib618['Value']        ,Fib500['Value']        ,Fib382['Value']        ,Fib236['Value']        ,Fib000['Value'])
                                        ,colors      =[Fib100['color']       ,Fib764['color']        ,Fib618['color']        ,Fib500['color']        ,Fib382['color']        ,Fib236['color']        ,Fib000['color']]
                                        ,linestyle   =[Fib100['linestyle']   ,Fib764['linestyle']    ,Fib618['linestyle']    ,Fib500['linestyle']    ,Fib382['linestyle']    ,Fib236['linestyle']    ,Fib000['linestyle']]
                                        ,linewidths  =[Fib100['linewidth']   ,Fib764['linewidth']    ,Fib618['linewidth']    ,Fib500['linewidth']    ,Fib382['linewidth']    ,Fib236['linewidth']    ,Fib000['linewidth']]
                                        ,alpha       =[Fib100['alpha']       ,Fib764['alpha']        ,Fib618['alpha']        ,Fib500['alpha']        ,Fib382['alpha']        ,Fib236['alpha']        ,Fib000['alpha']]
                                    )

        elif(style in ["Zamzam"]):
            if(fibonacciIndex in ["All"]):
                z_LineIndex = "Last1Year"
                z_LineList = ["Last1Year","CurrentYear","Last1Month","CurrentMonth","Last1Week","CurrentWeek","Yesterday","MarketOpen","EMA200"]
                z_LineBook =    {
                                "Last1Year"	    :{'Value':self.HighLow["Last1Year"]["High"]	    ,'linestyle':'solid'  ,'linewidth':1  ,'alpha':0.8	,'color':'#09F6BD'},
                                "CurrentYear"	:{'Value':self.HighLow["CurrentYear"]["High"]	,'linestyle':'solid'  ,'linewidth':1  ,'alpha':0.8	,'color':'#13E1EC'},
                                "Last1Month"	:{'Value':self.HighLow["Last1Month"]["High"]	,'linestyle':'solid'  ,'linewidth':1  ,'alpha':0.8	,'color':'#E01F7D'},
                                "CurrentMonth"	:{'Value':self.HighLow["CurrentMonth"]["High"]	,'linestyle':'solid'  ,'linewidth':1  ,'alpha':0.8	,'color':'#BC38C7'},
                                "Last1Week"	    :{'Value':self.HighLow["Last1Week"]["High"]	    ,'linestyle':'solid'  ,'linewidth':1  ,'alpha':0.8	,'color':'#C3893C'},
                                "CurrentWeek"	:{'Value':self.HighLow["CurrentWeek"]["High"]	,'linestyle':'solid'  ,'linewidth':1  ,'alpha':0.8	,'color':'#AAB847'},
                                "Yesterday"	    :{'Value':self.HighLow["Yesterday"]["High"]	    ,'linestyle':'solid'  ,'linewidth':1  ,'alpha':0.8	,'color':'#4D15EA'},
                                "MarketOpen"    :{'Value':self.HighLow["MarketOpen"]["High"]	,'linestyle':'solid'  ,'linewidth':1  ,'alpha':0.8	,'color':'#0FF045'},
                                "EMA200"	    :{'Value':self.HighLow["EMA200"]["High"]	    ,'linestyle':'solid'  ,'linewidth':1  ,'alpha':0.8	,'color':'#F20D2E'}
                                }
                Z_hlines        = []
                Z_colors        = []
                Z_linestyle     = []
                Z_linewidths    = []
                Z_alpha         = []
                for z_LineIndex in z_LineList :  Z_hlines.append     (z_LineBook[z_LineIndex]['Value'])
                for z_LineIndex in z_LineList :  Z_colors.append     (z_LineBook[z_LineIndex]['color'])
                for z_LineIndex in z_LineList :  Z_linestyle.append  (z_LineBook[z_LineIndex]['linestyle'])
                for z_LineIndex in z_LineList :  Z_linewidths.append (z_LineBook[z_LineIndex]['linewidth'])
                for z_LineIndex in z_LineList :  Z_alpha.append      (z_LineBook[z_LineIndex]['alpha'])
                self.fibolines=dict(     hlines      =  Z_hlines
                                        ,colors      =  Z_colors
                                        ,linestyle   =  Z_linestyle
                                        ,linewidths  =  Z_linewidths
                                        ,alpha       =  Z_alpha
                                    )

#________________________________________________________________________________________________________________________________________________________________________________________________





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
            High = -100
            Low  = -100

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










def fun3(   filePath_fun 
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
            High = -100
            Low  = -100

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



