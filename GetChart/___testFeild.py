import ChartPackage

index=0
tickerlist = ['TSLA','INTC','GOOGL']
exelsheets = [
                    r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\gv TSLA.xlsx",
                    r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\gv INTC.xlsx",
                    r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\gv GOOGL.xlsx"
             ]


for index in range(len(tickerlist)):
        
    ChartPackage.fun(   tickerName = tickerlist[index],     
                        filePathExcel = exelsheets[index],
                        filePathChart = r'D:\Python Tools\ChartMaker\SourceDocuments\OutPut_jpg',            #C:\Users\lenovo\Desktop\Python Project\Ehab\Results\Chart test.jpg
                        daySheet = "Yahoo Dayes",
                        imageType= '.png'

                    )