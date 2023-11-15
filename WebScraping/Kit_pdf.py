










import pdfkit

# Help Link :- https://www.youtube.com/watch?v=ri4flu1Jn4Y
# Help Link :- https://stackoverflow.com/questions/23359083/how-to-convert-webpage-into-pdf-by-using-python
# Help Link :- https://wkhtmltopdf.org/downloads.html

def fun(pdfTiker='MMM', pdfDisPath=r"D:\Python Tools\ChartMaker\SourceDocuments\OutPut_Excel\finviz "):
    try:
        path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf = path_wkhtmltopdf)
        rxpath = pdfDisPath + " finviz " + pdfTiker + ".pdf"
        pdfkit.from_url(f'https://finviz.com/quote.ashx?t={pdfTiker}&ty=c&ta=1&p=d', rxpath , configuration=config)

    except Exception:    
        print("#######################################################")
        print("Error found")
        print(f'https://finviz.com/quote.ashx?t={pdfTiker}&ty=c&ta=1&p=d')
        print("#######################################################")
    



















