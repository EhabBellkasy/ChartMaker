import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots



def fun (dataFrame) :

        #Make Yellow Color Candel 
        dataFrame['MCOverrides'] = [None]*len(dataFrame)

        for ts in dataFrame.index:
            if    ( (dataFrame.loc[ts,'Open']    ==  dataFrame.loc[ts,'Close']) and 
                    (dataFrame.loc[ts,'Volume']  >   0)):
                                                    dataFrame.loc[ts,'MCOverrides'] = '#FCFC00'
            elif  ( (dataFrame.loc[ts,'Open']    == dataFrame.loc[ts,'Close']) and 
                    (dataFrame.loc[ts,'Open']    == dataFrame.loc[ts,'High']) and 
                    (dataFrame.loc[ts,'High']    == dataFrame.loc[ts,'Low']) and 
                    (dataFrame.loc[ts,'Volume']  == 0)):
                                                    dataFrame.loc[ts,'MCOverrides'] = '#8A8A8A'
        
        mco = dataFrame['MCOverrides'].values
        return mco


