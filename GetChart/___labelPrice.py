








import numpy as np




# linesToDraw = df[['EMA','SMA']]
# ema = mpf.make_addplot(linesToDraw)

# pipMax = df['High'].max()
# pipMin = df['Low'].min()
# my_yticks = np.arange(round(pipMin, 3),round(pipMax, 3),0.001)

# fig, axlist = mpf.plot(df, type='candle', style='charles', addplot=ema,
# returnfig=True)
# axlist[0].set_yticks( my_yticks )
# mpf.show()







# Help Link :-  https://github.com/matplotlib/mplfinance/issues/604


# pipMax = 500
# pipMin = 450
# my_yticks = np.arange(round(pipMin, 3),round(pipMax, 3),0.5)

# print(my_yticks)

# g='''
# # # "price increment"
#     # pInc = 00.0001      #   max < 1
#     # pInc = 00.01        #   Dlt = 0.40
#     # pInc = 00.05        #   Dlt = 2
#     # pInc = 00.10        #   Dlt = 4
#     # # pInc = 00.20        #   Dlt = 
#     # pInc = 00.25        #   Dlt = 10
#     # pInc = 00.50        #   Dlt = 20
#     # pInc = 01.00        #   Dlt = 40
#     # pInc = 02.50        #   Dlt = 100
#     # pInc = 05.00        #   Dlt = 200
#     # pInc = 10.00        #   Dlt = 400
#     # # pInc = 20.00        #   Dlt = 
#     # # pInc = 25.00        #   Dlt = 
#     # # pInc = 50.00        #   Dlt = 
#     # # pInc = 100.00       #   Dlt = 
#     # # pInc = 500.00       #   Dlt = 
#     # # pInc = 
# '''







#_____________________________________________________________________________________

def LabelPrice  (    pMax = 6
                    ,pMin = 2
                ):
    print("Calculate Price Label")
    outLable =  {   
                    'ticks':[],
                    'tlabs':[],
                    'mitks':[],
                    'milab':[]
                }
    pDlt = pMax - pMin
    pInc = 0.05
    pDec = "2"    # "Decimal point"
            
    if (pMax < 1):
        pInc = 00.0001      #   max < 1
        pDec = "4"
    elif((pDlt < 0.40) and (max > 1)):
        pInc = 00.01        #   Dlt = 0.40
    elif(pDlt <= 2 and pDlt > 0.40):
        pInc = 00.05        #   Dlt = 0.40
    elif(pDlt <= 4 and pDlt > 2):
        pInc = 00.10        #   Dlt = 0.40
    elif(pDlt <= 10 and pDlt > 4):
        pInc = 00.25        #   Dlt = 0.40
    elif(pDlt <= 20 and pDlt > 10):
        pInc = 00.50        #   Dlt = 0.40
    elif(pDlt <= 40 and pDlt > 20):
        pInc = 01.00        #   Dlt = 0.40
    elif(pDlt <= 100 and pDlt > 40):
        pInc = 02.50        #   Dlt = 0.40
    elif(pDlt <= 200 and pDlt > 100):
        pInc = 05.00        #   Dlt = 0.40
    elif(pDlt <= 400 and pDlt > 200):
        pInc = 10.00        #   Dlt = 0.40

    outLable["ticks"] = np.arange(round(pMin, 1),round(pMax, 1),pInc)

    outLable["ticks"] = outLable["ticks"][::-1]
    
    pDec = "%." + pDec + "f"             #   "%.2f" % a
    outLable["tlabs"] =  [(pDec % x) for x in outLable["ticks"]]
    
    print(outLable["ticks"])
    print(outLable["tlabs"])

    return outLable

#_____________________________________________________________________________________
    
def testo():

    # LabelPrice()

    # print(boor)

    boor = 3.84775
    print(boor)

    boor = round(boor, 2)
    print(boor)

    boor = 2.338888
    n_decimals = 2
    boor = ((boor*10**n_decimals)//1)/(10**n_decimals)
    print("_____________")
    print(boor)

    # sboor = str(float(boor)).split('.')

    Sboor = str(boor).split('.')

    print(Sboor)

    Dboor = int(Sboor[1][1])

    print(24 and 7)

    print(Dboor*10**-2)

    Tboor = int (str( ((boor*10**n_decimals)//1)/(10**n_decimals) ).split('.')[1][1]) *10**(-n_decimals)

    print(Tboor)

    print("_____________")
    print(float(4))

#_____________________________________________________________________________________

def LabelPrice  (    pMax = 6
                    ,pMin = 2
                ):
    print("Calculate Price Label")
    outLable =  {   
                    'ticks':[],
                    'tlabs':[],
                    'mitks':[],
                    'milab':[]
                }
    pMax = float(pMax)
    pMin = float(pMin)
    pDlt = round(pMax - pMin)
    pInc = 0.05
    pDec = "2"    # "Decimal point"
    pStr = ((pMin*10**2)//1)/(10**2)       # math.floor(pMin) 
    pEnd = ((pMax*10**2)//1)/(10**2)       #  math.ceil(pMax)
            
    if (pMax < 1):  # pInc = 00.0001 
        pInc = 00.0001      #   max < 1
        pDec = "4"
        pStr = round(pMin, 2)
        pEnd = round(pMax, 2)
        round(pMax, 1)

    #__________________________________________________________________________________________________________________

    elif((pDlt < 0.40) and (pMax > 1)):     # pInc = 00.01
        pInc = 00.01        #   Dlt = 0.40

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 2 and pDlt > 0.40):        # pInc = 00.05 
        pInc = 00.05        #   Dlt = 0.40
        # pStr = ((pMin*10**2)//1)/(10**2)       # math.floor(pMin) 
        # pEnd = ((pMax*10**2)//1)/(10**2)       #  math.ceil(pMax)

        n_decimals = 2
        # pDN = int (str( ((pMin*10**n_decimals)//1)/(10**n_decimals) ).split('.')[1][1]) *10**(-n_decimals)
        # pUP = int (str( ((pMax*10**n_decimals)//1)/(10**n_decimals) ).split('.')[1][1]) *10**(-n_decimals)

        #   "%.2f" % a
        pDN = int(("%.2f" % pMin).split('.')[1][1]) *10**(-n_decimals)
        pUP = int(("%.2f" % pMax).split('.')[1][1]) *10**(-n_decimals)

        pStr = pMin + (pInc - pDN)
        pEnd = pMax + (pInc - pUP)

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 4 and pDlt > 2):           # pInc = 00.10 
        pInc = 00.10        #   Dlt = 0.40
        n_decimals = 2

        # pStr = ((pMin*10**n_decimals)//1)/(10**n_decimals)       # math.floor(pMin) 
        # pEnd = ((pMax*10**n_decimals)//1)/(10**n_decimals)       #  math.ceil(pMax)
        
        # pDN = int (str( ((pMin*10**n_decimals)//1)/(10**n_decimals) ).split('.')[1]) *10**(-n_decimals)
        # pUP = int (str( ((pMax*10**n_decimals)//1)/(10**n_decimals) ).split('.')[1]) *10**(-n_decimals)

        pDN = int(("%.2f" % pMin).split('.')[1][1]) *10**(-n_decimals)
        pUP = int(("%.2f" % pMax).split('.')[1][1]) *10**(-n_decimals)

        print("____________")
        print(pDN)
        print(pUP)
        print("____________")

        pStr = pMin + (pInc - pDN)
        pEnd = pMax + (pInc - pUP)

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 10 and pDlt > 4):          # pInc = 00.25 
        pInc = 00.25        #   Dlt = 0.40
        n_decimals = 2

        # pDN = int (str( ((pMin*10**n_decimals)//1)/(10**n_decimals) ).split('.')[1]) *10**(-n_decimals)
        # pUP = int (str( ((pMax*10**n_decimals)//1)/(10**n_decimals) ).split('.')[1]) *10**(-n_decimals)

        # pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        # pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        # pStr = pMin + (pInc - pDN)
        # pEnd = pMax + (pInc - pUP)

        # pStr = pMin + (pInc - ((0.20 - pDN0)+(0.05 - pDN1)))
        # pEnd = pMax + (pInc - ((0.20 - pUP0)+(0.05 - pUP1)))

        # pDN = ((0.20 - pDN00)+(0.05 - pDN10))
        # pUP = ((0.20 - pUP00)+(0.05 - pUP10))

        # pStr = pMin + (pInc - pDN)
        # pEnd = pMax + (pInc - pUP)

        # pDN00 = int(("%.2f" % pMin).split('.')[1][0]) *10**(-1)
        # pUP00 = int(("%.2f" % pMax).split('.')[1][0]) *10**(-1)

        # pDN10 = int(("%.2f" % pMin).split('.')[1][1]) *10**(-2)
        # pUP10 = int(("%.2f" % pMax).split('.')[1][1]) *10**(-2)

        # pDN01 = int(("%.2f" % (0.20 - pDN00)).split('.')[1][0]) *10**(-1)
        # pUP01 = int(("%.2f" % (0.20 - pUP00)).split('.')[1][0]) *10**(-1)

        # pDN11 = int(("%.2f" % (0.05 - pDN10)).split('.')[1][1]) *10**(-2)
        # pUP11 = int(("%.2f" % (0.05 - pUP10)).split('.')[1][1]) *10**(-2)
                                
        # pDN = pDN01 + pDN11
        # pUP = pUP01 + pUP11

        # pStr = pMin + ( pDN)
        # pEnd = pMax + ( pUP)




        pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        pStr = pMin + (pInc - (pDN%pInc))
        pEnd = pMax + (pInc - (pUP%pInc))


        # print("____________")
        # print("pDN00=",pDN00,"|pDN01=",pDN01)
        # print("pUP00=",pUP00,"|pUP01=",pUP01)
        # print("pDN10=",pDN10,"|pDN11=",pDN11)
        # print("pUP10=",pUP10,"|pUP11=",pUP11)
        # print("____________")

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 20 and pDlt > 10):         # pInc = 00.50
        pInc = 00.50        #   Dlt = 0.40
        n_decimals = 2

        # pDN = int (str( ((pMin*10**n_decimals)//1)/(10**n_decimals) ).split('.')[1]) *10**(-n_decimals)
        # pUP = int (str( ((pMax*10**n_decimals)//1)/(10**n_decimals) ).split('.')[1]) *10**(-n_decimals)

        pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        pStr = pMin + (pInc - (pDN%pInc))
        pEnd = pMax + (pInc - (pUP%pInc))

        pStr = round(pStr,2)
        pEnd = round(pEnd,2)

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 40 and pDlt > 20):         # pInc = 01.00         
        pInc = 01.00        #   Dlt = 0.40
        n_decimals = 2

        # pStr = int(pMin)
        # pEnd = int(pMax)

        pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)
        
        pStr = int(pMin + (pInc - (pDN%pInc)))
        pEnd = int(pMax + (pInc - (pUP%pInc)))
        # print("++++++#################++++++")

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 100 and pDlt > 40):        # pInc = 02.50 
        pInc = 02.50        #   Dlt = 0.40
        n_decimals = 2
        
        # pDN = round(pMin%10,n_decimals)
        # pUP = round(pMax%10,n_decimals)
        # pStr = pMin + (pInc - pDN)
        # pEnd = pMax + (pInc - pUP)

        # pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        # pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        pDN = round(pMin%10,2) 
        pUP = round(pMax%10,2) 
        
        pStr = pMin + (pInc - (pDN%pInc))
        pEnd = pMax + (pInc - (pUP%pInc))

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 200 and pDlt > 100):       # pInc = 05.00 
        pInc = 05.00        #   Dlt = 0.40
        n_decimals = 2
        
        # pDN = int(pMin%10)
        # pUP = int(pMax%10)
        # pStr = pMin + (pInc - pDN)
        # pEnd = pMax + (pInc - pUP)

        pDN = round(pMin%10,2) 
        pUP = round(pMax%10,2) 
        
        pStr = pMin + (pInc - (pDN%pInc))
        pEnd = pMax + (pInc - (pUP%pInc))

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 400 and pDlt > 200):       # pInc = 10.00
        pInc = 10.00        #   Dlt = 0.40
        n_decimals = 2

        # pDN = int(pMin%100)
        # pUP = int(pMax%100)
        # pStr = pMin + (pInc - pDN)
        # pEnd = pMax + (pInc - pUP)
        
        pDN = round(pMin%100,2) 
        pUP = round(pMax%100,2) 
        
        pStr = pMin + (pInc - (pDN%pInc))
        pEnd = pMax + (pInc - (pUP%pInc))

    #__________________________________________________________________________________________________________________

    elif( pDlt > 400):                      # pInc = 25.00 
        pInc = 25.00        #   Dlt = 0.40
        n_decimals = 2

        # pDN = int(pMin%100)
        # pUP = int(pMax%100)
        # pStr = pMin + (pInc - pDN)
        # pEnd = pMax + (pInc - pUP)

        pDN = round(pMin%100,2) 
        pUP = round(pMax%100,2) 
        
        pStr = pMin + (pInc - (pDN%pInc))
        pEnd = pMax + (pInc - (pUP%pInc))

    #__________________________________________________________________________________________________________________
    
    # print(pMax)
    # print(pMin)
    # print(pDlt)
    # print(pInc)
    # print(pDec)
    
    # print("____________")
    # print("pDN=",pDN)
    # print("pUP=",pUP)
    # print("pStr=",pStr)
    # print("pEnd=",pEnd)
        
    print("____________")
    print("|Min:",pMin,"Max:",pMax,"|Dlt:",pDlt,"|Inc:",pInc,"|Dec:",pDec)
    print("pStr=",pStr,"pDN=",pDN,"     |pEnd=",pEnd,"|pUP=",pUP)
    print("++++++++++++")
    # print()
    
    
    outLable["ticks"] = np.arange(pStr,pEnd,pInc)

    # outLable["ticks"] = outLable["ticks"][::-1]
    
    pDec = "%." + pDec + "f"             #   "%.2f" % a
    outLable["tlabs"] =  [(pDec % x) for x in outLable["ticks"]]
    
    print(outLable["ticks"])
    print(outLable["tlabs"])



    # print(outLable["ticks"])
    # print(outLable["tlabs"])

    return outLable

#_____________________________________________________________________________________

def LabelPrice3  (    pMax = 6
                    ,pMin = 2
                ):
    print("Calculate Price Label")
    #__________________________________________________________________________________________________________________
    # Set Varibles
    outLable =  {   
                    'ticks':[],
                    'tlabs':[],
                    'mitks':[],
                    'milab':[]
                }
    pMax = float(pMax)
    pMin = float(pMin)
    pDlt = round(pMax - pMin)
    pInc = 0.05
    pDec = "2"    # "Decimal point"
    pStr = ((pMin*10**2)//1)/(10**2)       # math.floor(pMin) 
    pEnd = ((pMax*10**2)//1)/(10**2)       #  math.ceil(pMax)

    #__________________________________________________________________________________________________________________

    if (pMax < 1):  # pInc = 00.0001 
        pInc = 00.0001      #   max < 1
        pDec = "4"
        pStr = round(pMin, 2)
        pEnd = round(pMax, 2)
        round(pMax, 1)

    #__________________________________________________________________________________________________________________

    elif((pDlt < 0.40) and (pMax > 1)):     # pInc = 00.01
        pInc = 00.01        #   Dlt = 0.40

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 2 and pDlt > 0.40):        # pInc = 00.05 
        pInc = 00.05        #   Dlt = 0.40        
        n_decimals = 2
        
        # pDN = int(("%.2f" % pMin).split('.')[1][1]) *10**(-n_decimals)
        # pUP = int(("%.2f" % pMax).split('.')[1][1]) *10**(-n_decimals)

        # pStr = pMin + (pInc - pDN)
        # pEnd = pMax + (pInc - pUP)

        pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        pStr = round( pMin + (pInc - (pDN%pInc)) ,n_decimals)
        pEnd = round( pMax + (pInc - (pUP%pInc)) ,n_decimals)

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 4 and pDlt > 2):           # pInc = 00.10 
        pInc = 00.10        #   Dlt = 0.40
        n_decimals = 2

        # pDN = int(("%.2f" % pMin).split('.')[1][1]) *10**(-n_decimals)
        # pUP = int(("%.2f" % pMax).split('.')[1][1]) *10**(-n_decimals)
        
        # pStr = pMin + (pInc - pDN)
        # pEnd = pMax + (pInc - pUP)

        pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        pStr = round( pMin + (pInc - (pDN%pInc)) ,n_decimals)
        pEnd = round( pMax + (pInc - (pUP%pInc)) ,n_decimals)

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 10 and pDlt > 4):          # pInc = 00.25 
        pInc = 00.25        #   Dlt = 0.40
        n_decimals = 2

        # pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        # pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        # pStr = pMin + (pInc - (pDN%pInc))
        # pEnd = pMax + (pInc - (pUP%pInc))

        pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        pStr = round( pMin + (pInc - (pDN%pInc)) ,n_decimals)
        pEnd = round( pMax + (pInc - (pUP%pInc)) ,n_decimals)

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 20 and pDlt > 10):         # pInc = 00.50
        pInc = 00.50        #   Dlt = 0.40
        n_decimals = 2

        # pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        # pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        # pStr = pMin + (pInc - (pDN%pInc))
        # pEnd = pMax + (pInc - (pUP%pInc))

        # pStr = round(pStr,2)
        # pEnd = round(pEnd,2)

        pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        pStr = round( pMin + (pInc - (pDN%pInc)) ,n_decimals)
        pEnd = round( pMax + (pInc - (pUP%pInc)) ,n_decimals)

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 40 and pDlt > 20):         # pInc = 01.00         
        pInc = 01.00        #   Dlt = 0.40
        n_decimals = 2

        # pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        # pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)
        
        # pStr = int(pMin + (pInc - (pDN%pInc)))
        # pEnd = int(pMax + (pInc - (pUP%pInc)))

        pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        pStr = round( pMin + (pInc - (pDN%pInc)) ,n_decimals)
        pEnd = round( pMax + (pInc - (pUP%pInc)) ,n_decimals)

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 100 and pDlt > 40):        # pInc = 02.50 
        pInc = 02.50        #   Dlt = 0.40
        n_decimals = 2

        pDN = round(pMin%10,2) 
        pUP = round(pMax%10,2) 
        
        pStr = pMin + (pInc - (pDN%pInc))
        pEnd = pMax + (pInc - (pUP%pInc))

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 200 and pDlt > 100):       # pInc = 05.00 
        pInc = 05.00        #   Dlt = 0.40
        n_decimals = 2

        pDN = round(pMin%10,2) 
        pUP = round(pMax%10,2) 
        
        pStr = pMin + (pInc - (pDN%pInc))
        pEnd = pMax + (pInc - (pUP%pInc))

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 400 and pDlt > 200):       # pInc = 10.00
        pInc = 10.00        #   Dlt = 0.40
        n_decimals = 2
        
        pDN = round(pMin%100,2) 
        pUP = round(pMax%100,2) 
        
        pStr = pMin + (pInc - (pDN%pInc))
        pEnd = pMax + (pInc - (pUP%pInc))

    #__________________________________________________________________________________________________________________

    elif( pDlt > 400):                      # pInc = 25.00 
        pInc = 25.00        #   Dlt = 0.40
        n_decimals = 2

        pDN = round(pMin%100,2) 
        pUP = round(pMax%100,2) 
        
        pStr = pMin + (pInc - (pDN%pInc))
        pEnd = pMax + (pInc - (pUP%pInc))

    #__________________________________________________________________________________________________________________
        
    print("____________")
    print("|Min:",pMin,"Max:",pMax,"|Dlt:",pDlt,"|Inc:",pInc,"|Dec:",pDec)
    print("pStr=",pStr,"pDN=",pDN,"     |pEnd=",pEnd,"|pUP=",pUP)
    print("++++++++++++")
    # print()
    
    
    outLable["ticks"] = np.arange(pStr,pEnd,pInc)
    
    pDec = "%." + pDec + "f"             #   "%.2f" % a
    outLable["tlabs"] =  [(pDec % x) for x in outLable["ticks"]]
    
    print(outLable["ticks"])
    print(outLable["tlabs"])

    return outLable
    #__________________________________________________________________________________________________________________

#_____________________________________________________________________________________

def LabelPrice4  (    pMax = 6
                    ,pMin = 2
                ):
    print("Calculate Price Label")
    #__________________________________________________________________________________________________________________
    # Set Varibles
    pDlt = round(pMax - pMin,4)
    ntrvIndex = 'Inc00_05'
    outLable =  {   
                    'ticks':[],
                    'tlabs':[],
                    'mitks':[],
                    'milab':[]
                }
    ntrvlHub =  {
                     'Inc00_0001'	:{	'p_Incerement':00.0001	    ,'p_Decimals':'4'	    ,'n_Decimals':4	    ,'n_Integers':0	    	}		#	pInc = 00.0001 
                    ,'Inc00_01'	    :{	'p_Incerement':00.01	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':0	    	}		#	pInc = 00.01
                    ,'Inc00_05'	    :{	'p_Incerement':00.05	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':0	    	}		#	pInc = 00.05
                    ,'Inc00_10'	    :{	'p_Incerement':00.10	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':0	    	}		#	pInc = 00.10
                    ,'Inc00_25'	    :{	'p_Incerement':00.25	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':0	    	}		#	pInc = 00.25
                    ,'Inc00_50'	    :{	'p_Incerement':00.50	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':0	    	}		#	pInc = 00.50
                    ,'Inc01_00'	    :{	'p_Incerement':01.00	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':0	    	}		#	pInc = 01.00
                    ,'Inc02_50'	    :{	'p_Incerement':02.50	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':1	    	}		#	pInc = 02.50
                    ,'Inc05_00'	    :{	'p_Incerement':05.00	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':1	    	}		#	pInc = 05.00
                    ,'Inc10_00'	    :{	'p_Incerement':10.00	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':2	    	}		#	pInc = 10.00
                    ,'Inc25_00'	    :{	'p_Incerement':25.00	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':2	    	}		#	pInc = 25.00
                    ,'Inc50_00'	    :{	'p_Incerement':50.00	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':2	    	}		#	pInc = 50.00 
                   

                }


    

    #__________________________________________________________________________________________________________________

    if (pMax < 1):  # pInc = 00.0001 
        ntrvIndex = 'Inc00_0001'	

        # pInc = 00.0001      #   max < 1
        # pDec = "4"
        # pStr = round(pMin, 2)
        # pEnd = round(pMax, 2)
        # round(pMax, 1)

    #__________________________________________________________________________________________________________________

    elif((pDlt < 0.40) and (pMax > 1)):     # pInc = 00.01
        ntrvIndex = 'Inc00_01'	
        
        
        # pInc = 00.01        #   Dlt = 0.40

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 2 and pDlt > 0.40):        # pInc = 00.05 
        ntrvIndex = 'Inc00_05'	
           
        
        # pInc = 00.05        #   Dlt = 0.40        
        # n_decimals = 2
        
        # # pDN = int(("%.2f" % pMin).split('.')[1][1]) *10**(-n_decimals)
        # # pUP = int(("%.2f" % pMax).split('.')[1][1]) *10**(-n_decimals)

        # # pStr = pMin + (pInc - pDN)
        # # pEnd = pMax + (pInc - pUP)

        # pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        # pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        # pStr = round( pMin + (pInc - (pDN%pInc)) ,n_decimals)
        # pEnd = round( pMax + (pInc - (pUP%pInc)) ,n_decimals)

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 4 and pDlt > 2):           # pInc = 00.10 
        ntrvIndex = 'Inc00_10'	    
        
        # pInc = 00.10        #   Dlt = 0.40
        # n_decimals = 2

        # # pDN = int(("%.2f" % pMin).split('.')[1][1]) *10**(-n_decimals)
        # # pUP = int(("%.2f" % pMax).split('.')[1][1]) *10**(-n_decimals)
        
        # # pStr = pMin + (pInc - pDN)
        # # pEnd = pMax + (pInc - pUP)

        # pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        # pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        # pStr = round( pMin + (pInc - (pDN%pInc)) ,n_decimals)
        # pEnd = round( pMax + (pInc - (pUP%pInc)) ,n_decimals)

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 10 and pDlt > 4):          # pInc = 00.25 
        ntrvIndex = 'Inc00_25'	    
        
        # pInc = 00.25        #   Dlt = 0.40
        # n_decimals = 2

        # # pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        # # pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        # # pStr = pMin + (pInc - (pDN%pInc))
        # # pEnd = pMax + (pInc - (pUP%pInc))

        # pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        # pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        # pStr = round( pMin + (pInc - (pDN%pInc)) ,n_decimals)
        # pEnd = round( pMax + (pInc - (pUP%pInc)) ,n_decimals)

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 20 and pDlt > 10):         # pInc = 00.50
        ntrvIndex = 'Inc00_50'	    
        
        # pInc = 00.50        #   Dlt = 0.40
        # n_decimals = 2

        # # pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        # # pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        # # pStr = pMin + (pInc - (pDN%pInc))
        # # pEnd = pMax + (pInc - (pUP%pInc))

        # # pStr = round(pStr,2)
        # # pEnd = round(pEnd,2)

        # pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        # pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        # pStr = round( pMin + (pInc - (pDN%pInc)) ,n_decimals)
        # pEnd = round( pMax + (pInc - (pUP%pInc)) ,n_decimals)

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 40 and pDlt > 20):         # pInc = 01.00         
        ntrvIndex = 'Inc01_00'	    
        
        # pInc = 01.00        #   Dlt = 0.40
        # n_decimals = 2

        # # pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        # # pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)
        
        # # pStr = int(pMin + (pInc - (pDN%pInc)))
        # # pEnd = int(pMax + (pInc - (pUP%pInc)))

        # pDN = int(("%.2f" % pMin).split('.')[1]) *10**(-n_decimals)
        # pUP = int(("%.2f" % pMax).split('.')[1]) *10**(-n_decimals)

        # pStr = round( pMin + (pInc - (pDN%pInc)) ,n_decimals)
        # pEnd = round( pMax + (pInc - (pUP%pInc)) ,n_decimals)

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 100 and pDlt > 40):        # pInc = 02.50 
        ntrvIndex = 'Inc02_50'	    
        
        # pInc = 02.50        #   Dlt = 0.40
        # n_decimals = 2

        # pDN = round(pMin%10,2) 
        # pUP = round(pMax%10,2) 
        
        # pStr = pMin + (pInc - (pDN%pInc))
        # pEnd = pMax + (pInc - (pUP%pInc))

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 200 and pDlt > 100):       # pInc = 05.00 
        ntrvIndex = 'Inc05_00'	    
        
        # pInc = 05.00        #   Dlt = 0.40
        # n_decimals = 2

        # pDN = round(pMin%10,2) 
        # pUP = round(pMax%10,2) 
        
        # pStr = pMin + (pInc - (pDN%pInc))
        # pEnd = pMax + (pInc - (pUP%pInc))

    #__________________________________________________________________________________________________________________

    elif(pDlt <= 400 and pDlt > 200):       # pInc = 10.00
        ntrvIndex = 'Inc10_00'	    
        
        # pInc = 10.00        #   Dlt = 0.40
        # n_decimals = 2
        
        # pDN = round(pMin%100,2) 
        # pUP = round(pMax%100,2) 
        
        # pStr = pMin + (pInc - (pDN%pInc))
        # pEnd = pMax + (pInc - (pUP%pInc))

    #__________________________________________________________________________________________________________________

    elif( pDlt > 400):                      # pInc = 25.00 
        ntrvIndex = 'Inc25_00'	    
        
        # pInc = 25.00        #   Dlt = 0.40
        # n_decimals = 2

        # pDN = round(pMin%100,2) 
        # pUP = round(pMax%100,2) 
        
        # pStr = pMin + (pInc - (pDN%pInc))
        # pEnd = pMax + (pInc - (pUP%pInc))

    #__________________________________________________________________________________________________________________
        
    
    
    
    pMax = float(pMax)
    pMin = float(pMin)
    
    pInc = ntrvlHub[ntrvIndex]['p_Incerement']
    pDec = ntrvlHub[ntrvIndex]['p_Decimals']    # "Decimal point"

    n_decimals = ntrvlHub[ntrvIndex]['n_Decimals']
    n_Integers = ntrvlHub[ntrvIndex]['n_Integers']
    

    pDN = round((pMin%(10**n_Integers)),n_decimals) 
    pUP = round((pMax%(10**n_Integers)),n_decimals) 
        
    pStr = round( pMin + (pInc - (pDN%pInc)) ,n_decimals)
    pEnd = round( pMax + (pInc - (pUP%pInc)) ,n_decimals)
    
    outLable["ticks"] = np.arange(pStr,pEnd,pInc)
    
    pDec = "%." + pDec + "f"             #   "%.2f" % a
    outLable["tlabs"] =  [(pDec % x) for x in outLable["ticks"]]
    


    print(outLable["ticks"])
    print(outLable["tlabs"])

    print("____________")
    print("|Min:",pMin,"Max:",pMax,"|Dlt:",pDlt,"|Inc:",pInc,"|Dec:",pDec)
    print("pStr=",pStr,"pDN=",pDN,"     |pEnd=",pEnd,"|pUP=",pUP)
    print(ntrvIndex)
    print("++++++++++++")
    # print()

    return outLable
    #__________________________________________________________________________________________________________________

#_____________________________________________________________________________________

def LabelPrice5 (    pMax = 6
                    ,pMin = 2
                ):
    print("Calculate Price Label")
    #__________________________________________________________________________________________________________________
    # Set Varibles:-
    pDlt = round(pMax - pMin,4)
    ntrvIndex = 'Inc00_05'
    outLable =  {   
                    'ticks':[],
                    'tlabs':[],
                    'mitks':[],
                    'milab':[]
                }
    ntrvlHub =  {
                     'Inc00_0001'	:{	'p_Incerement':00.0001	    ,'p_Decimals':'4'	    ,'n_Decimals':4	    ,'n_Integers':0	    	}		#	pInc = 00.0001 
                    ,'Inc00_01'	    :{	'p_Incerement':00.01	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':0	    	}		#	pInc = 00.01
                    ,'Inc00_05'	    :{	'p_Incerement':00.05	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':0	    	}		#	pInc = 00.05
                    ,'Inc00_10'	    :{	'p_Incerement':00.10	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':0	    	}		#	pInc = 00.10
                    ,'Inc00_25'	    :{	'p_Incerement':00.25	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':0	    	}		#	pInc = 00.25
                    ,'Inc00_50'	    :{	'p_Incerement':00.50	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':0	    	}		#	pInc = 00.50
                    ,'Inc01_00'	    :{	'p_Incerement':01.00	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':0	    	}		#	pInc = 01.00
                    ,'Inc02_50'	    :{	'p_Incerement':02.50	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':1	    	}		#	pInc = 02.50
                    ,'Inc05_00'	    :{	'p_Incerement':05.00	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':1	    	}		#	pInc = 05.00
                    ,'Inc10_00'	    :{	'p_Incerement':10.00	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':2	    	}		#	pInc = 10.00
                    ,'Inc25_00'	    :{	'p_Incerement':25.00	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':2	    	}		#	pInc = 25.00
                    ,'Inc50_00'	    :{	'p_Incerement':50.00	    ,'p_Decimals':'2'	    ,'n_Decimals':2	    ,'n_Integers':2	    	}		#	pInc = 50.00 
                   

                }                
    if (pDlt > 0):
        #__________________________________________________________________________________________________________________
        # Choose Interval:- 
        if  (pMax < 1                   ) : ntrvIndex = 'Inc00_0001'  # pInc = 00.0001 
        elif(pDlt < 0.40 and pMax > 1   ) : ntrvIndex = 'Inc00_01'	  # pInc = 00.01
        elif(pDlt <= 2   and pDlt > 0.40) : ntrvIndex = 'Inc00_05'    # pInc = 00.05 
        elif(pDlt <= 4   and pDlt > 2   ) : ntrvIndex = 'Inc00_10'    # pInc = 00.10 
        elif(pDlt <= 10  and pDlt > 4   ) : ntrvIndex = 'Inc00_25'    # pInc = 00.25 
        elif(pDlt <= 20  and pDlt > 10  ) : ntrvIndex = 'Inc00_50'    # pInc = 00.50
        elif(pDlt <= 40  and pDlt > 20  ) : ntrvIndex = 'Inc01_00'    # pInc = 01.00         
        elif(pDlt <= 100 and pDlt > 40  ) : ntrvIndex = 'Inc02_50'    # pInc = 02.50 
        elif(pDlt <= 200 and pDlt > 100 ) : ntrvIndex = 'Inc05_00'    # pInc = 05.00 
        elif(pDlt <= 400 and pDlt > 200 ) : ntrvIndex = 'Inc10_00'    # pInc = 10.00
        elif(                pDlt > 400 ) : ntrvIndex = 'Inc25_00'    # pInc = 25.00 
        #__________________________________________________________________________________________________________________    
        # Extract parameters        
        pMax = float(pMax)
        pMin = float(pMin)

        pInc = ntrvlHub[ntrvIndex]['p_Incerement']
        pDec = ntrvlHub[ntrvIndex]['p_Decimals']    # "Decimal point"

        n_decimals = ntrvlHub[ntrvIndex]['n_Decimals']
        n_Integers = ntrvlHub[ntrvIndex]['n_Integers']
        #__________________________________________________________________________________________________________________    
        # Calculate Start and End range of Price Label
        pDN = round((pMin%(10**n_Integers)),n_decimals) 
        pUP = round((pMax%(10**n_Integers)),n_decimals) 
            
        pStr = round( pMin + (pInc - (pDN%pInc)) ,n_decimals)
        pEnd = round( pMax + (pInc - (pUP%pInc)) ,n_decimals)
        #__________________________________________________________________________________________________________________    
        # Calculate Price Label and Prepare Output
        outLable["ticks"] = np.arange(pStr,pEnd,pInc)
        
        pDec = "%." + pDec + "f"             #   "%.2f" % a
        outLable["tlabs"] =  [(pDec % x) for x in outLable["ticks"]]    
        #__________________________________________________________________________________________________________________
        # Print out Data
        print(outLable["ticks"])
        print(outLable["tlabs"])

        print("____________")
        print("Min:",pMin,"|Max:",pMax,"|Dlt:",pDlt,"|Inc:",pInc,"|Dec:",pDec)
        print("pStr=",pStr,"pDN=",pDN,"     |pEnd=",pEnd,"|pUP=",pUP)
        print(ntrvIndex)
        print("++++++++++++")
        # print()
    #__________________________________________________________________________________________________________________
    else:
        print ("Wrong InPut")
        print("Min:",pMin,"|Max:",pMax,"|Dlt:",pDlt)
    #__________________________________________________________________________________________________________________
    return outLable
    #__________________________________________________________________________________________________________________

#_____________________________________________________________________________________

def LabelPrice6 (    pMax = 6
                    ,pMin = 2
                ):
    print("Calculate Price Label")
    #__________________________________________________________________________________________________________________
    # Set Varibles:-
    pDlt = round(pMax - pMin,4)
    ntrvIndex = 'Inc00_05'
    outLable =  {   
                    'ticks':[],
                    'tlabs':[],
                    'mitks':[],
                    'milab':[]
                }
    ntrvlHub =  {
                     "Inc00_0001"	:{	"p_Incerement":	00.0001	    ,"p_Decimals": "4"	  ,"n_Decimals": 4    ,"n_Integers": 0	  ,"MAX": 0000.0036	  ,"MIN":	0000.0000	}		#	pInc = 	00.0001
                    ,"Inc00_0005"	:{	"p_Incerement":	00.0005	    ,"p_Decimals": "4"	  ,"n_Decimals": 4	  ,"n_Integers": 0	  ,"MAX": 0000.0190	  ,"MIN":	0000.0036	}		#	pInc = 	00.0005
                    ,"Inc00_0010"	:{	"p_Incerement":	00.0010	    ,"p_Decimals": "4"	  ,"n_Decimals": 4    ,"n_Integers": 0	  ,"MAX": 0000.0370	  ,"MIN":	0000.0190	}		#	pInc = 	00.0010
                    ,"Inc00_0025"	:{	"p_Incerement":	00.0025	    ,"p_Decimals": "4"	  ,"n_Decimals": 4	  ,"n_Integers": 0	  ,"MAX": 0000.0925	  ,"MIN":	0000.0370	}		#	pInc = 	00.0025
                    ,"Inc00_0050"	:{	"p_Incerement":	00.0050	    ,"p_Decimals": "4"	  ,"n_Decimals": 4	  ,"n_Integers": 0	  ,"MAX": 0000.1800	  ,"MIN":	0000.0925	}		#	pInc = 	00.0050
                    ,"Inc00_0100"	:{	"p_Incerement":	00.0100	    ,"p_Decimals": "4"	  ,"n_Decimals": 4	  ,"n_Integers": 0	  ,"MAX": 0000.3700	  ,"MIN":	0000.1800	}		#	pInc = 	00.0100
                    ,"Inc00_0250"	:{	"p_Incerement":	00.0250	    ,"p_Decimals": "4"	  ,"n_Decimals": 4	  ,"n_Integers": 0	  ,"MAX": 0000.9250	  ,"MIN":	0000.3700	}		#	pInc = 	00.0250
                    ,"Inc00_0500"	:{	"p_Incerement":	00.0500	    ,"p_Decimals": "4"	  ,"n_Decimals": 4	  ,"n_Integers": 0	  ,"MAX": 0001.8500	  ,"MIN":	0000.9250	}		#	pInc = 	00.0500
                    ,"Inc00_1000"	:{	"p_Incerement":	00.1000	    ,"p_Decimals": "4"	  ,"n_Decimals": 4	  ,"n_Integers": 0	  ,"MAX": 0003.7000	  ,"MIN":	0001.8500	}		#	pInc = 	00.1000
    
                    ,"Inc00_01"	    :{	"p_Incerement":	00.0100	    ,"p_Decimals": "2"	  ,"n_Decimals": 2	  ,"n_Integers": 0	  ,"MAX": 0000.4000	  ,"MIN":	0000.0000	}		#	pInc = 	00.0100
                    ,"Inc00_05"	    :{	"p_Incerement":	00.0500	    ,"p_Decimals": "2"	  ,"n_Decimals": 2	  ,"n_Integers": 0	  ,"MAX": 0002.0000	  ,"MIN":	0000.4000	}		#	pInc = 	00.0500
                    ,"Inc00_10"	    :{	"p_Incerement":	00.1000	    ,"p_Decimals": "2"	  ,"n_Decimals": 2	  ,"n_Integers": 0	  ,"MAX": 0004.0000	  ,"MIN":	0002.0000	}		#	pInc = 	00.1000
                    ,"Inc00_25"	    :{	"p_Incerement":	00.2500	    ,"p_Decimals": "2"	  ,"n_Decimals": 2	  ,"n_Integers": 0	  ,"MAX": 0010.0000	  ,"MIN":	0004.0000	}		#	pInc = 	00.2500
                    ,"Inc00_50"	    :{	"p_Incerement":	00.5000	    ,"p_Decimals": "2"	  ,"n_Decimals": 2	  ,"n_Integers": 0	  ,"MAX": 0020.0000	  ,"MIN":	0010.0000	}		#	pInc = 	00.5000
                    ,"Inc01_00"	    :{	"p_Incerement":	01.0000	    ,"p_Decimals": "2"	  ,"n_Decimals": 2	  ,"n_Integers": 0	  ,"MAX": 0040.0000	  ,"MIN":	0020.0000	}		#	pInc = 	01.0000
                    ,"Inc02_50"	    :{	"p_Incerement":	02.5000	    ,"p_Decimals": "2"	  ,"n_Decimals": 2	  ,"n_Integers": 1	  ,"MAX": 0100.0000	  ,"MIN":	0040.0000	}		#	pInc = 	02.5000
                    ,"Inc05_00"	    :{	"p_Incerement":	05.0000	    ,"p_Decimals": "2"	  ,"n_Decimals": 2	  ,"n_Integers": 1	  ,"MAX": 0200.0000	  ,"MIN":	0100.0000	}		#	pInc = 	05.0000
                    ,"Inc10_00"	    :{	"p_Incerement":	10.0000	    ,"p_Decimals": "2"	  ,"n_Decimals": 2	  ,"n_Integers": 2	  ,"MAX": 0400.0000	  ,"MIN":	0200.0000	}		#	pInc = 	10.0000
                    ,"Inc25_00"	    :{	"p_Incerement":	25.0000	    ,"p_Decimals": "2"	  ,"n_Decimals": 2	  ,"n_Integers": 2	  ,"MAX": 0925.0000	  ,"MIN":	0400.0000	}		#	pInc = 	25.0000
                    ,"Inc50_00"	    :{	"p_Incerement":	50.0000	    ,"p_Decimals": "2"	  ,"n_Decimals": 2	  ,"n_Integers": 2	  ,"MAX": 1800.0000	  ,"MIN":	0925.0000	}		#	pInc = 	50.0000                   
                }                
    if (pDlt > 0):
        #__________________________________________________________________________________________________________________
        # Choose Interval:- 
        if  (pMax < 1 ) : 
            if  (pDlt <= ntrvlHub["Inc00_0001"]["MAX"]  and  pDlt > ntrvlHub["Inc00_0001"]["MIN"]  ):ntrvIndex = 'Inc00_0001'   # pInc = 00.0001 
            elif(pDlt <= ntrvlHub["Inc00_0005"]["MAX"]  and  pDlt > ntrvlHub["Inc00_0005"]["MIN"]  ):ntrvIndex = 'Inc00_0005'   # pInc = 00.0005
            elif(pDlt <= ntrvlHub["Inc00_0010"]["MAX"]  and  pDlt > ntrvlHub["Inc00_0010"]["MIN"]  ):ntrvIndex = 'Inc00_0010'   # pInc = 00.0010
            elif(pDlt <= ntrvlHub["Inc00_0025"]["MAX"]  and  pDlt > ntrvlHub["Inc00_0025"]["MIN"]  ):ntrvIndex = 'Inc00_0025'   # pInc = 00.0025
            elif(pDlt <= ntrvlHub["Inc00_0050"]["MAX"]  and  pDlt > ntrvlHub["Inc00_0050"]["MIN"]  ):ntrvIndex = 'Inc00_0050'   # pInc = 00.0050
            elif(pDlt <= ntrvlHub["Inc00_0100"]["MAX"]  and  pDlt > ntrvlHub["Inc00_0100"]["MIN"]  ):ntrvIndex = 'Inc00_0100'   # pInc = 00.0100
            elif(pDlt <= ntrvlHub["Inc00_0250"]["MAX"]  and  pDlt > ntrvlHub["Inc00_0250"]["MIN"]  ):ntrvIndex = 'Inc00_0250'   # pInc = 00.0250
            elif(pDlt <= ntrvlHub["Inc00_0500"]["MAX"]  and  pDlt > ntrvlHub["Inc00_0500"]["MIN"]  ):ntrvIndex = 'Inc00_0500'   # pInc = 00.0500
            elif(pDlt <= ntrvlHub["Inc00_1000"]["MAX"]  and  pDlt > ntrvlHub["Inc00_1000"]["MIN"]  ):ntrvIndex = 'Inc00_1000'   # pInc = 0001000                        
        elif(pMax >= 1 ) :     
            if  (pDlt <= ntrvlHub["Inc00_01"]["MAX"]    and  pDlt > ntrvlHub["Inc00_01"]["MIN"]    ):ntrvIndex = 'Inc00_01'     # pInc = 00.01
            elif(pDlt <= ntrvlHub["Inc00_05"]["MAX"]    and  pDlt > ntrvlHub["Inc00_05"]["MIN"]    ):ntrvIndex = 'Inc00_05'     # pInc = 00.05
            elif(pDlt <= ntrvlHub["Inc00_10"]["MAX"]    and  pDlt > ntrvlHub["Inc00_10"]["MIN"]    ):ntrvIndex = 'Inc00_10'     # pInc = 00.10
            elif(pDlt <= ntrvlHub["Inc00_25"]["MAX"]    and  pDlt > ntrvlHub["Inc00_25"]["MIN"]    ):ntrvIndex = 'Inc00_25'     # pInc = 00.25
            elif(pDlt <= ntrvlHub["Inc00_50"]["MAX"]    and  pDlt > ntrvlHub["Inc00_50"]["MIN"]    ):ntrvIndex = 'Inc00_50'     # pInc = 00.50
            elif(pDlt <= ntrvlHub["Inc01_00"]["MAX"]    and  pDlt > ntrvlHub["Inc01_00"]["MIN"]    ):ntrvIndex = 'Inc01_00'     # pInc = 01.00
            elif(pDlt <= ntrvlHub["Inc02_50"]["MAX"]    and  pDlt > ntrvlHub["Inc02_50"]["MIN"]    ):ntrvIndex = 'Inc02_50'     # pInc = 02.50
            elif(pDlt <= ntrvlHub["Inc05_00"]["MAX"]    and  pDlt > ntrvlHub["Inc05_00"]["MIN"]    ):ntrvIndex = 'Inc05_00'     # pInc = 05.00
            elif(pDlt <= ntrvlHub["Inc10_00"]["MAX"]    and  pDlt > ntrvlHub["Inc10_00"]["MIN"]    ):ntrvIndex = 'Inc10_00'     # pInc = 10.00
            elif(pDlt <= ntrvlHub["Inc25_00"]["MAX"]    and  pDlt > ntrvlHub["Inc25_00"]["MIN"]    ):ntrvIndex = 'Inc25_00'     # pInc = 25.00
            elif(pDlt <= ntrvlHub["Inc50_00"]["MAX"]    and  pDlt > ntrvlHub["Inc50_00"]["MIN"]    ):ntrvIndex = 'Inc50_00'     # pInc = 50.00
        #__________________________________________________________________________________________________________________    
        # Extract parameters        
        pMax = float(pMax)
        pMin = float(pMin)

        pInc = ntrvlHub[ntrvIndex]['p_Incerement']
        pDec = ntrvlHub[ntrvIndex]['p_Decimals']    # "Decimal point"

        n_decimals = ntrvlHub[ntrvIndex]['n_Decimals']
        n_Integers = ntrvlHub[ntrvIndex]['n_Integers']
        #__________________________________________________________________________________________________________________    
        # Calculate Start and End range of Price Label      
        pDN = round((pMin%(10**n_Integers)),n_decimals)     # Help Link :-  https://stackoverflow.com/questions/63430691/last-two-digits-of-decimal-number-with-a-mask
        pUP = round((pMax%(10**n_Integers)),n_decimals)     # Help Link :-  https://stackoverflow.com/questions/58065055/floor-and-ceil-with-number-of-decimals 
            
        pStr = round( pMin + (pInc - (pDN%pInc)) ,n_decimals)
        pEnd = round( pMax + (pInc - (pUP%pInc)) ,n_decimals)
        #__________________________________________________________________________________________________________________    
        # Calculate Price Label and Prepare Output
        outLable["ticks"] = np.arange(pStr,pEnd,pInc)
        
        pDec = "%." + pDec + "f" #   "%.2f" % a             # Help Link :-  https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
        outLable["tlabs"] =  [(pDec % x) for x in outLable["ticks"]]    
        #__________________________________________________________________________________________________________________
        # Print out Data
        print(outLable["ticks"])
        print(outLable["tlabs"])

        print("____________")
        print("Min:",pMin,"|Max:",pMax,"|Dlt:",pDlt,"|Inc:",pInc,"|Dec:",pDec)
        print("pStr=",pStr,"pDN=",pDN,"     |pEnd=",pEnd,"|pUP=",pUP)
        print(ntrvIndex)
        print("++++++++++++")
        # print()
    #__________________________________________________________________________________________________________________
    else:
        print ("Wrong InPut")
        print("Min:",pMin,"|Max:",pMax,"|Dlt:",pDlt)
    #__________________________________________________________________________________________________________________
    return outLable
    #__________________________________________________________________________________________________________________

#_____________________________________________________________________________________







print("#####___START___#####")


# LabelPrice3  (    pMax = 8.53
#                 ,pMin = 3.42
#             )

print("||||||||||||||||||||||||||")

LabelPrice5  (    pMax = 6.53
                ,pMin = 9.45
            )


# print("||||||||||||||||||||||||||")
# print(round (55.65%1 , 2))


# logor = 7 - 8
# if ((logor )>0 ) : print(logor)


