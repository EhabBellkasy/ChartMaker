

import pandas as pd

def fun(    ticker = 'goog',
            filePath = r"C\Users\lenovo\Desktop\Python Project\Ehab\Results\Split ",
            sheetName = 'Samary'
        ):
    
    filePathTicker = filePath + ticker + ".xlsx"
    df = pd.DataFrame(columns=['Symbol', 'Premarket_High','High','Low','Open','Close','Volume',
                               'Open_Volume','Relative_Volume','Average_Volume','Shortable_Shares',
                               'gap','PH_pst','PH_O','Max_Gain','intra_Range','Market_Cap','Float',
                               'Sector','Industry','Country','Watch_List','Zamzam_Effect','My_Interaction',
                               'File','Daily','Min_5','Min_1',
                               'Sec0920_0930','Sec0930_0940' ,'Sec0940_0950','Sec0950_1000','Sec1000_1010',
                               'Sec1010_1020','Sec1020_1030','Sec1030_1040','Sec1040_1050','Sec1050_1100','Sec1100_1110' 
                                
                               ]) # need to change this
    df.to_excel( filePathTicker , sheetName)








