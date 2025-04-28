import pandas as pd
from fpdf import FPDF
from fpdf.fonts import FontFace

##### CREATE A PDF #####

def fCreatePdf(dfCo, dfTs, strPathOut):
    pdf = classPDF()
    strCo = dfCo.CurrentName[0]

    # Add introductory page
    pdf.fAddPage(strTitle='Gender Pay Gap Overview', strCo=strCo)
    fIntroduction(pdf=pdf)
    
    # Add Pay Quartile Calculation
    pdf.fAddPage(strTitle='Hourly Pay Quartile Calculation', strCo=strCo)
    fCalcQuartiles(pdf=pdf)
    # Add Median Pay Calculation
    pdf.fAddPage(strTitle='Median Hourly Pay Gap Calculation', strCo=strCo)
    fCalcMdnPay(pdf=pdf, dfCo=dfCo)
    # Add Mean Pay Calculation
    pdf.fAddPage(strTitle='Mean Hourly Pay Gap Calculation', strCo=strCo)
    fCalcAvgPay(pdf=pdf, dfCo=dfCo)
    # Add Percentage of Men and Women Receiving Bonus Calculation
    pdf.fAddPage(strTitle='Percentage of Men and Women Receiving Bonus Pay Calculation', strCo=strCo)
    fCalcBns(pdf=pdf, dfCo=dfCo)
    # Add Median Bonus Calculation
    pdf.fAddPage(strTitle='Median Bonus Pay Gap Calculation', strCo=strCo)
    fCalcMdnBns(pdf=pdf, dfCo=dfCo)
    # Add Mean Bonus Calculation
    pdf.fAddPage(strTitle='Mean Bonus Pay Gap Calculation', strCo=strCo)
    fCalcAvgBns(pdf=pdf, dfCo=dfCo)
    
    # Add Summary page
    pdf.fAddPage(strTitle='Summary of Gender Pay Gap Statistics', strCo=strCo)
    fReportedStats(pdf=pdf, dfCo=dfCo)
    # Add Bonus Pool page
    pdf.fAddPage(strTitle='Bonus Material: Implied Share of Bonus Pool by Gender', strCo=strCo)
    fShrBnsPool(pdf=pdf, dfCo=dfCo)
    
    # Add 1st Timeseries page
    pdf.fAddPage(strTitle='Timeseries: Hourly Pay', strCo=strCo)
    fTimeseriesPay(pdf=pdf, dfTs=dfTs)    
    # Add 2nd Timeseries page
    pdf.fAddPage(strTitle='Timeseries: Bonus Pay', strCo=strCo)
    fTimeseriesBonus(pdf=pdf)
    
    # Save the PDF
    strFilename = ''.join(strChar for strChar in dfCo.Names[0] if strChar.isalnum() | (strChar == ' ')) + '.pdf'
    pdf.output(strPathOut + '\\' + strFilename)
    

def fIntroduction(pdf):
    # The source file is written in basic html to allow text formatting
    with open(file=r'text\QandA.txt', mode='r') as objFile:
        strText = objFile.read()
    pdf.write_html(text=strText)
    

def fCalcQuartiles(pdf):
    # Read text from source file.  Use a table so as to control the width of text block.
    with open(file=r'text\CalcQuartiles.txt', mode='r') as objFile:
        strText = objFile.read()    
    listTable = [[(strText),' ']]
    pdf.fPdfDrawTable(tupleXY=(10, 40), listTable=listTable, tupleWidths=(133, 5))

    # Insert Quartiles chart
    strPath=r'images\CoPopPyr2.png'
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(158, 57, 125, 125))
    

def fCalcMdnPay(pdf, dfCo):
    # Read text from source file.  Use a table so as to control the width of text block.
    with open(file=r'text\CalcMdnPay1.txt', mode='r') as objFile:
        strText = objFile.read()    
    listTable = [[(strText),' ']]
    pdf.fPdfDrawTable(tupleXY=(10, 40), listTable=listTable, tupleWidths=(133, 5))

    # Additional text explaining chart
    strBlurb = 'The median hourly pay gap of {:.2%} means that the median woman received £{:.2f} for every £{:.0f} the median man received in hourly pay.'.format(
        dfCo.DiffMedianHourlyPercent[0], 100 * dfCo.PayMidF[0], 100 * dfCo.PayMidM[0])
    pdf.set_xy(10, 145)
    pdf.multi_cell(w=58, h=pdf.fSpace(intFontSize=10, floatMultiple=1.5), text=strBlurb, align='L')

    # Insert Median Pay chart
    strPath=r'images\CoPayMid.png'
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(68, 120, 75, 75))
    
    # Read text from source file.  Use a table so as to control the width of text block.
    with open(file=r'text\CalcMdnPay2.txt', mode='r') as objFile:
        strText = objFile.read()    
    listTable = [[(strText),' ']]
    pdf.fPdfDrawTable(tupleXY=(154, 40), listTable=listTable, tupleWidths=(133, 5))

    # Insert Median Pay explanatory chart
    strPath=r'images\CoPayMain.png'
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(158, 75, 125, 125))
    

def fCalcAvgPay(pdf, dfCo):
    # Read text from source file.  Use a table so as to control the width of text block.
    with open(file=r'text\CalcAvgPay1.txt', mode='r') as objFile:
        strText = objFile.read()    
    listTable = [[(strText),' ']]
    pdf.fPdfDrawTable(tupleXY=(10, 40), listTable=listTable, tupleWidths=(133, 5))

    # Additional text explaining chart
    strBlurb = 'The mean hourly pay gap of {:.2%} means that on average, a woman received £{:.2f} for every £{:.0f} a man received in hourly pay.'.format(
        dfCo.DiffMeanHourlyPercent[0], 100 * dfCo.PayAvgF[0], 100 * dfCo.PayAvgM[0])
    pdf.set_xy(10, 145)
    pdf.multi_cell(w=58, h=pdf.fSpace(intFontSize=10, floatMultiple=1.5), text=strBlurb, align='L')

    # Insert Mean Pay chart
    strPath=r'images\CoPayAvg.png'
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(68, 120, 75, 75))
    
    # Read text from source file.  Use a table so as to control the width of text block.
    with open(file=r'text\CalcAvgPay2.txt', mode='r') as objFile:
        strText = objFile.read()    
    listTable = [[(strText),' ']]
    pdf.fPdfDrawTable(tupleXY=(154, 40), listTable=listTable, tupleWidths=(133, 5))
    

def fCalcBns(pdf, dfCo):
    # Read text from source file.  Use a table so as to control the width of text block.
    with open(file=r'text\CalcBns1.txt', mode='r') as objFile:
        strText = objFile.read()    
    listTable = [[(strText),' ']]
    pdf.fPdfDrawTable(tupleXY=(10, 40), listTable=listTable, tupleWidths=(133, 5))

    # Additional text explaining chart
    strBlurb = '{:.2%} of women received a bonus.\n{:.2%} of men received a bonus.'.format(
        dfCo.FemaleBonusPercent[0], dfCo.MaleBonusPercent[0])
    pdf.set_xy(10, 145)
    pdf.multi_cell(w=58, h=pdf.fSpace(intFontSize=10, floatMultiple=1.5), text=strBlurb, align='L')

    # Insert Bonus chart
    strPath=r'images\CoBns.png'
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(68, 120, 75, 75))
    
    # Read text from source file.  Use a table so as to control the width of text block.
    with open(file=r'text\CalcBns2.txt', mode='r') as objFile:
        strText = objFile.read()    
    listTable = [[(strText),' ']]
    pdf.fPdfDrawTable(tupleXY=(154, 40), listTable=listTable, tupleWidths=(133, 5))
    

def fCalcMdnBns(pdf, dfCo):
    # Read text from source file.  Use a table so as to control the width of text block.
    with open(file=r'text\CalcMdnBns1.txt', mode='r') as objFile:
        strText = objFile.read()    
    listTable = [[(strText),' ']]
    pdf.fPdfDrawTable(tupleXY=(10, 40), listTable=listTable, tupleWidths=(133, 5))

    # Additional text explaining chart
    strBlurb = 'The median bonus pay gap of {:.2%} means that the median woman received £{:.2f} for every £{:.0f} the median man received in bonus pay.'.format(
        dfCo.BnsMidD[0], 100 * dfCo.BnsMidF[0], 100 * dfCo.BnsMidM[0])
    pdf.set_xy(10, 145)
    pdf.multi_cell(w=58, h=pdf.fSpace(intFontSize=10, floatMultiple=1.5), text=strBlurb, align='L')

    # Insert Median Bonus chart
    strPath=r'images\CoBnsMid.png'
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(68, 120, 75, 75))
    
    # Read text from source file.  Use a table so as to control the width of text block.
    with open(file=r'text\CalcMdnBns2.txt', mode='r') as objFile:
        strText = objFile.read()    
    listTable = [[(strText),' ']]
    pdf.fPdfDrawTable(tupleXY=(154, 40), listTable=listTable, tupleWidths=(133, 5))

    # Insert Median Bonus explanatory chart
    strPath=r'images\CoBnsMain.png'
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(158, 75, 125, 125))
    

def fCalcAvgBns(pdf, dfCo):
    # Read text from source file.  Use a table so as to control the width of text block.
    with open(file=r'text\CalcAvgBns1.txt', mode='r') as objFile:
        strText = objFile.read()    
    listTable = [[(strText),' ']]
    pdf.fPdfDrawTable(tupleXY=(10, 40), listTable=listTable, tupleWidths=(133, 5))

    # Additional text explaining chart
    strBlurb = 'The mean bonus pay gap of {:.2%} means that on average, a woman received £{:.2f} for every £{:.0f} a man received in bonus pay.'.format(
        dfCo.BnsAvgD[0], 100 * dfCo.BnsAvgF[0], 100 * dfCo.BnsAvgM[0])
    pdf.set_xy(229, 75)
    pdf.multi_cell(w=58, h=pdf.fSpace(intFontSize=10, floatMultiple=1.5), text=strBlurb, align='L')

    # Insert Mean Bonus chart
    strPath=r'images\CoBnsAvg.png'
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(154, 40, 75, 75))
        
        
def fReportedStats(pdf, dfCo):
    # Add tble with company details
    if type(dfCo.CompanyLinkToGPGInfo[0]) != str:
        listLink = ['Employer Link', 'No link provided to employer\'s GPG info']
    else:
        listLink = ['Employer Link', ('Click here for employer\'s GPG info', dfCo.CompanyLinkToGPGInfo[0])]
    listTable = [
        ['Snapshot Year', r''+str(dfCo.Year[0])],
        ['Industry', r''+str(dfCo.Industry[0])],
        ['No. of Employees', r''+str(dfCo.EmployerSize[0])],
        ['Company Number', r''+str(dfCo.CompanyNumber[0])],
        ['Reported on time', r''+str(not dfCo.SubmittedAfterTheDeadline[0])],
        ['Responsible Person', r''+str(dfCo.ResponsiblePerson[0])],
        ['Address', r''+str(dfCo.Address[0])],
        listLink
    ]
    pdf.fPdfDrawTable(tupleXY=(10,40), listTable=listTable, tupleWidths=(30,70))

    # Quartiles chart with explanatory text
    strPath=r'images\CoPopPyr2.png'
    strBlurb = ('"Full-pay relevant employees" are split into four equally sized groups based on hourly pay.' +
                ' The percentage of women and men in each pay group is shown.')
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(117, 40, 50, 50), strBlurb=strBlurb)

    # Median Pay Gap chart & text
    strPath = r'images\CoPayMid.png'
    strBlurb = 'The median hourly pay gap of {:.2%} means that the median woman received £{:.2f} for every £{:.0f} the median man received in hourly pay.'.format(
        dfCo.DiffMedianHourlyPercent[0], 100 * dfCo.PayMidF[0], 100 * dfCo.PayMidM[0])
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(177, 40, 50, 50), strBlurb=strBlurb)

    # Mean Pay Gap chart & text
    strPath = r'images\CoPayAvg.png'
    strBlurb = 'The mean hourly pay gap of {:.2%} means that on average, a woman received £{:.2f} for every £{:.0f} a man received in hourly pay.'.format(
        dfCo.DiffMeanHourlyPercent[0], 100 * dfCo.PayAvgF[0], 100 * dfCo.PayAvgM[0])
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(237, 40, 50, 50), strBlurb=strBlurb)

    # Who got a bonus? chart & text
    strPath = r'images\CoBns.png'
    strBlurb = '{:.2%} of women received a bonus.  {:.2%} of men received a bonus.'.format(
        dfCo.FemaleBonusPercent[0], dfCo.MaleBonusPercent[0])
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(117, 125, 50, 50), strBlurb=strBlurb)

    # Median bonus chart & text
    strPath = r'images\CoBnsMid.png'
    strBlurb = 'The median bonus pay gap of {:.2%} means that the median woman received £{:.2f} for every £{:.0f} the median man received in bonus pay.'.format(
        dfCo.BnsMidD[0], 100 * dfCo.BnsMidF[0], 100 * dfCo.BnsMidM[0])
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(177, 125, 50, 50), strBlurb=strBlurb)

    # Mean bonus chart & text
    strPath = r'images\CoBnsAvg.png'
    strBlurb = 'The mean bonus pay gap of {:.2%} means that on average, a woman received £{:.2f} for every £{:.0f} a man received in bonus pay.'.format(
        dfCo.BnsAvgD[0], 100 * dfCo.BnsAvgF[0], 100 * dfCo.BnsAvgM[0])
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(237, 125, 50, 50), strBlurb=strBlurb)

    
def fShrBnsPool(pdf, dfCo):
    
    # Read text from source file.  Use a table so as to control the width of text block.
    with open(file=r'text\CalcBnsPool.txt', mode='r') as objFile:
        strText = objFile.read()    
    listTable = [[(strText),' ']]
    pdf.fPdfDrawTable(tupleXY=(65, 40), listTable=listTable, tupleWidths=(233, 5))
    
    # Quartiles chart with explanatory text
    strPath=r'images\CoPopPyr.png'
    strBlurb = ('"Full-pay relevant employees" are split into four equally sized groups based on hourly pay.' +
                ' The percentage of women and men in each pay group is shown.')
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(22.5, 50, 50, 50), strBlurb=strBlurb)

    # Who got a bonus? chart & text
    strPath = r'images\CoBns.png'
    strBlurb = 'Of people employed on the snapshot date, {:.2%} of women received a bonus.  {:.2%} of men received a bonus.'.format(
        dfCo.FemaleBonusPercent[0], dfCo.MaleBonusPercent[0])
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(120, 50, 50, 50), strBlurb=strBlurb)

    # Mean bonus chart & text
    strPath = r'images\CoBnsAvg.png'
    strBlurb = 'For people who received a bonus, on average, a woman received £{:.2f} for every £{:.0f} a man received in bonus pay.'.format(
        100 * dfCo.BnsAvgF[0], 100 * dfCo.BnsAvgM[0])
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(217.5, 50, 50, 50), strBlurb=strBlurb)

    # Add arrows pointing down 
    pdf.fPdfDrawArrow(strPoint='down', tupleXY=(35, 125), strComment='use')
    pdf.fPdfDrawArrow(strPoint='down', tupleXY=(132.5, 125), strComment='combine')
    pdf.fPdfDrawArrow(strPoint='down', tupleXY=(230, 125), strComment='combine')

    # Insert population total chart with explanatory text
    strPath=r'images\CoPopTot.png'
    strBlurb = ('This represents all "full-pay relevant employees" as at the snapshot date, and shows their gender.' +
                '\nThese numbers should be very similar to the gender split of all employees.')
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(10, 150, 75, 25), strBlurb=strBlurb)

    # Add arrow pointing right
    pdf.fPdfDrawArrow(strPoint='right', tupleXY=(85, 150), strComment='combine')

    # Bonus recipients by gender & text
    strPath = r'images\CoPopBns.png'
    strBlurb = ('This represents the group of employees who were paid a bonus, and shows their gender.' +
                '\nThis doesn\'t include people who were paid a bonus but were no longer employed on the snapshot date.')
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(110, 150, 75, 25), strBlurb=strBlurb)

    # Add arrow pointing right
    pdf.fPdfDrawArrow(strPoint='right', tupleXY=(185, 150), strComment='combine')

    # Share of bonus pool br grnder & text
    strPath = r'images\CoBnsShr.png'
    strBlurb = ('This represents all the money paid as bonuses in the year, and shows how much went to each gender.' +
                '\nThis doesn\'t include people who were paid a bonus but were no longer employed on the snapshot date.')
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(210, 150, 75, 25), strBlurb=strBlurb)
    
    
def fTimeseriesPay(pdf, dfTs):
    # Add a table
    dfSubset = dfTs.loc[:, ['Year', 'SubmittedAfterTheDeadline', 'EmployerSize', 'CompanyLinkToGPGInfo']]
    dfSubset['SubmittedAfterTheDeadline'] = ~dfSubset['SubmittedAfterTheDeadline']    
    dfSubset['CompanyLinkToGPGInfo'] = dfSubset.apply(lambda row:
        'No link' if type(row['CompanyLinkToGPGInfo']) != str else ('Link', row['CompanyLinkToGPGInfo']), axis=1)
    listTable = [['Year', 'Reported on time', 'No. of Employees', 'Employer GPG Link']] + dfSubset.values.tolist()
    pdf.fPdfDrawTable(tupleXY=(20, 125), listTable=listTable, tupleWidths=(12, 15, 28, 20))
    
    # Read text from source file.  Use a table so as to control the width of text block.
    with open(file=r'text\Timeseries.txt', mode='r') as objFile:
        strText = objFile.read()    
    listTable = [[(strText),' ']]
    pdf.fPdfDrawTable(tupleXY=(10, 40), listTable=listTable, tupleWidths=(100, 5))
    
    # Add the charts
    strPath=r'images\TsPayMid.png'
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(111, 35, 75, 75))
    strPath=r'images\TsPayAvg.png'
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(212, 35, 75, 75))
    strPath=r'images\TsPopF.png'
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(111, 115, 75, 75))
    strPath=r'images\TsPopM.png'
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(212, 115, 75, 75))
    

def fTimeseriesBonus(pdf):
    # Add the charts
    strPath=r'images\TsBnsMid.png'
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(111, 35, 75, 75))
    strPath=r'images\TsBnsAvg.png'
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(212, 35, 75, 75))
    strPath=r'images\TsPopTot.png'
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(10, 115, 75, 75))
    strPath=r'images\TsPopBns.png'
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(111, 115, 75, 75))
    strPath=r'images\TsBnsShr.png'
    pdf.fPdfDrawChart(strPath=strPath, tupleXYWH=(212, 115, 75, 75))


class classPDF(FPDF):
    # Set standard size of text to be used
    intFontSize = 10
    
    def fResetFont(self):
        self.set_font('times', style='', size=self.intFontSize)
        self.set_text_color(r=0, g=0, b=0)
        
    def footer(self):
        # Set font & colour (greyscale, or r, g, b if g&b provided)
        self.set_font(family='helvetica', style='I', size=8)
        self.set_text_color(r=128)
        self.set_y(-10)
        self.cell(w=0, h=10, text='https://www.linkedin.com/in/michael-hill-v1/', align='L')
        self.cell(w=0, h=10, text=f'Page {self.page_no()}', align='R')
        self.fResetFont()

    def fAddPage(self, strTitle, strCo):
        # Add a page and set text formatting
        # The XY co-ords of the pdf are in mm from top left.
        # A4 size is 210 * 297 mm
        self.add_page(orientation='landscape', format='A4')
        self.set_margin(10) # 10mm margin
        self.fResetFont()
        # Page title
        self.set_font(family='helvetica', style='B', size=24)
        self.set_y(10)
        self.cell(w=0, h=self.fSpace(24, 1.2), text=strTitle, align='C')
        self.fResetFont()
        # Co Name
        self.set_font(family='helvetica', size=18)
        self.set_y(25)
        self.cell(w=0, h=self.fSpace(18, 1.2), text=strCo, align='C')
        self.fResetFont()

    def fPdfDrawTable(self, tupleXY, listTable, tupleWidths):
        self.set_xy(tupleXY[0], tupleXY[1])
        with self.table(width=sum(tupleWidths), col_widths=tupleWidths, align='LEFT', text_align='LEFT',
                        v_align='TOP', first_row_as_headings=False, borders_layout='NONE', line_height=self.fSpace(10, 1.5)) as table:
            for listRow in listTable:
                row = table.row()
                for item in listRow:
                    if type(item) is tuple:
                        row.cell(text=str(item[0]), link=r''+item[1], style=FontFace(color=(0,0,255)))
                    else:
                        row.cell(text=str(item))
   
    def fPdfDrawChart(self, strPath, tupleXYWH, strBlurb=''):
        # Add the chart
        self.image(name=strPath, x=tupleXYWH[0], y=tupleXYWH[1], w=tupleXYWH[2], h=tupleXYWH[3], keep_aspect_ratio=True)
        if strBlurb != '':
            # Write some text below
            self.set_xy(tupleXYWH[0], tupleXYWH[1] + tupleXYWH[3]) 
            self.multi_cell(w=tupleXYWH[2], h=self.fSpace(self.intFontSize, 1.2), text=strBlurb, align='C', border=0)
        
    def fPdfDrawArrow(self, strPoint, tupleXY, strComment):
        if strPoint == 'down':
            strPath = r'images\ArrowD.png'
            tupleBump = (18.75, 0)
        elif strPoint == 'left':
            strPath = r'images\ArrowL.png'
            tupleBump = (0, 18.75)
        else:
            strPath = r'images\ArrowR.png'
            tupleBump = (0, 18.75)
        # Add the image
        self.image(name=strPath, x=tupleXY[0], y=tupleXY[1], w=25, h=25, keep_aspect_ratio=True)
        # Write some text below / to the side
        self.set_xy(tupleXY[0] + tupleBump[0], tupleXY[1] + tupleBump[1])
        strBlurb = ('\ncombine with other' if strComment == 'combine' else '\nuse') + ' data to calculate new information'
        self.set_text_color(r=128)
        self.set_font(size=9)
        self.multi_cell(w=25, h=self.fSpace(self.intFontSize, 1.2), text=strBlurb, align='C', border=0)
        self.fResetFont()
        
    def fSpace(self, intFontSize, floatMultiple, strUnits='mm'):
        # Would expect there is already something built in to FPDF2 for this
        # Need to actually code for other units!
        # There are 72 points to an inch, and 2.54cm to an inch
        return floatMultiple * intFontSize * 25.4 / 72
