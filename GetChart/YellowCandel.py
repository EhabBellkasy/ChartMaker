import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots



def fun (dataFrame) :

        

        #Make Yellow Color Candel 
        dataFrame['MCOverrides'] = [None]*len(dataFrame)
        # print(dataFrame.head(3))
        for ts in dataFrame.index:
            if    ( (dataFrame.loc[ts,'Open']    ==  dataFrame.loc[ts,'Close']) and 
                    (dataFrame.loc[ts,'Volume']  >   0)):
                                                    dataFrame.loc[ts,'MCOverrides'] = '#FCFC00'
            elif  ( (dataFrame.loc[ts,'Open']    == dataFrame.loc[ts,'Close']) and 
                    (dataFrame.loc[ts,'Open']    == dataFrame.loc[ts,'High']) and 
                    (dataFrame.loc[ts,'High']    == dataFrame.loc[ts,'Low']) and 
                    (dataFrame.loc[ts,'Volume']  == 0)):
                                                    dataFrame.loc[ts,'MCOverrides'] = '#8A8A8A'
        # print(dataFrame.head(3))

        # print("/*-/*-/*-/*-")
        mco = dataFrame['MCOverrides'].values
        # print(len(mco))
        # print((mco))


        # for ei in range (len(mco)):
        #         if    (mco[ei] == '#FCFC00'):
        #                mco[ei] = mc_Y
        #         elif  (mco[ei] == '#8A8A8A'):
        #                mco[ei] = mc_G
        # mco[0] = mc_Y
        # mco[1] = mc_Y
        # mco[2] = mc_Y
        # mco[3] = mc_Y
        # mco[4] = mc_Y
        # mco[5] = mc_Y
        # mco[6] = mc_Y
        # mco[7] = mc_Y
        # mco[8] = mc_Y
        # mco[9] = mc_Y

        # print("/*-/*-/*-/*-")
        # print((mco))
        '''




        #marketcolors
        mc = mpf.make_marketcolors(up='g',
                                down='r',
                                edge='inherit',
                                wick={'up':'w','down':'w'},
                                volume='in',
                                ohlc='i'
                                
                                
                                )

        #make mpf style
        styleEhab  = mpf.make_mpf_style(marketcolors=mc,
                                        gridaxis= 'both',
                                        gridstyle= 'dashdot',
                                        gridcolor= '#ffff00', #'yellow'
                                        figcolor = 'gray',
                                        facecolor= 'Black',
                                        edgecolor= 'r',
                                        
                                        y_on_right= False

                                        
                                        )

        '''


        # #Make Yallow Color Candel 
        # dataFrame['MCOverrides'] = [None]*len(dataFrame)
        # print(dataFrame.head(3))
        # for ts in dataFrame.index:
        #     if    ( (dataFrame.loc[ts,'Open']    ==  dataFrame.loc[ts,'Close']) and 
        #             (dataFrame.loc[ts,'Volume']  >   0)):
        #                                             dataFrame.loc[ts,'MCOverrides'] = '#FCFC00' # Yellow
        #     elif  ( (dataFrame.loc[ts,'Open']    == dataFrame.loc[ts,'Close']) and 
        #             (dataFrame.loc[ts,'Open']    == dataFrame.loc[ts,'High']) and 
        #             (dataFrame.loc[ts,'High']    == dataFrame.loc[ts,'Low']) and 
        #             (dataFrame.loc[ts,'Volume']  == 0)):
        #                                             dataFrame.loc[ts,'MCOverrides'] = '#8A8A8A' # Grey
        # print(dataFrame.head(3))
        # mco = dataFrame['MCOverrides'].values





        return mco


