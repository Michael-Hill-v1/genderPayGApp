# pip install pandas
# pip install matplotlib
# pip install FPDF2
# pip install requests

import pandas as pd
import mdlChart
import mdlGUI
import mdlPDF

def fMain():
    # Read in the whole data file
    strFile = r'data\data.csv'
    df = pd.read_csv(filepath_or_buffer=strFile, converters = {'EmployerId': str})

    ##### Use GUI to get year, Employer, and file path for the output #####
    intYear, strEmployerId, strPathOut = mdlGUI.fGetSettings(df)

    # Create subset dataframes
    dfCo = df.loc[(df['Year'] == intYear) & (df['EmployerId'] == strEmployerId)]
    dfCo = dfCo.reset_index(drop=True, inplace=False)
    dfTs = df.loc[df['EmployerId'] == strEmployerId]
    dfTs = dfTs.reset_index(drop=True, inplace=False)    

    tupleBonus = (dfCo['MaleBonusPercent'][0] != 0, dfCo['FemaleBonusPercent'][0] != 0)
    mdlChart.fCreateCompanyCharts(df=dfCo, tupleBonus=tupleBonus)
    mdlChart.fCreateTimeSeriesCharts(df=dfTs)
    mdlPDF.fCreatePdf(dfCo=dfCo, dfTs=dfTs, strPathOut=strPathOut)
    
fMain()
