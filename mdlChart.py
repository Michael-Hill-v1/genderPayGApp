import pandas as pd
import matplotlib.pyplot as plt


# Set colour scheme for charts
strClrF4 = '#98594B'
strClrF3 = '#F48037'
strClrF2 = '#D8AE48'
strClrF1 = '#E5E790'
strClrF0 = '#DD4132'
strClrM4 = '#395551'
strClrM3 = '#1F5DA0'
strClrM2 = '#289DBE'
strClrM1 = '#C5AEB1'
strClrM0 = '#A4AE77'


###### Request Timeseries Charts ######
    
def fCreateTimeSeriesCharts(df):
    # Chart some data
    fChartTS(df=df,
             strTitle = 'Median Hourly Pay',
             listCols = ['Year', 'PayMidF'],
             listLbls = [('Women\'s Median Hourly Pay as Percentage of Men\'s', strClrF1)],
             strSaveTo = r'images\TsPayMid.png')
    fChartTS(df=df,
             strTitle = 'Mean Hourly Pay',
             listCols = ['Year', 'PayAvgF'],
             listLbls = [('Women\'s Mean Hourly Pay as Percentage of Men\'s', strClrF1)],
             strSaveTo = r'images\TsPayAvg.png')
    fChartTS(df = df,
             strTitle = 'Median Bonus Pay',
             listCols = ['Year', 'BnsMidF'],
             listLbls = [('Women\'s Median Bonus as Percentage of Men\'s', strClrF1)],
             strSaveTo = r'images\TsBnsMid.png')
    fChartTS(df = df,
             strTitle = 'Mean Bonus Pay',
             listCols = ['Year', 'BnsAvgF'],
             listLbls = [('Women\'s Mean Bonus as Percentage of Men\'s', strClrF1)],
             strSaveTo = r'images\TsBnsAvg.png')
    fChartTS(df = df,
             strTitle = 'Employees by Gender (%)',
             listCols = ['Year', 'PopTotF', 'PopTotM'],
             listLbls = [('Women', strClrF1), ('Men', strClrM1)],
             strSaveTo = r'images\TsPopTot.png')
    fChartTS(df = df,
             strTitle = 'Bonus Recipients by Gender (%)',
             listCols = ['Year', 'PopBnsF', 'PopBnsM'],
             listLbls = [('Women', strClrF1), ('Men', strClrM1)],
             strSaveTo = r'images\TsPopBns.png')
    fChartTS(df = df,
             strTitle = 'Share of Bonus Pool by Gender (%)',
             listCols = ['Year', 'BnsShrF', 'BnsShrM'],
             listLbls = [('Women', strClrF1), ('Men', strClrM1)],
             strSaveTo = r'images\TsBnsShr.png')
    fChartTS(df = df,
             strTitle = 'Men in Each Pay Quartile (%)',
             listCols = ['Year', 'PopMQ1', 'PopMQ2', 'PopMQ3', 'PopMQ4'],
             listLbls = [('Lower Quartile', strClrF1), ('Lower-Middle Quartile', strClrF2),
                         ('Upper-Middle Quartile', strClrF3), ('Upper Quartile', strClrF4)],
             strSaveTo = r'images\TsPopM.png')
    fChartTS(df = df,
             strTitle = 'Women in Each Pay Quartile (%)',
             listCols = ['Year', 'PopFQ1', 'PopFQ2', 'PopFQ3', 'PopFQ4'],
             listLbls = [('Lower Quartile', strClrF1), ('Lower-Middle Quartile', strClrF2),
                         ('Upper-Middle Quartile', strClrF3), ('Upper Quartile', strClrF4)],
             strSaveTo = r'images\TsPopF.png')

def fChartTS(df, strTitle, listCols, listLbls, strSaveTo):
    # Create subset of data for charting.  Rescale decimals to percentages.  Chart the data.  Save.
    dfSubset = df.loc[:, listCols]
    dfSubset.iloc[:, 1:(len(df.columns)-1)] *= 100
    figChart = fChartTsBar(df=dfSubset, strTitle=strTitle, listLbls=listLbls)
    figChart.savefig(strSaveTo)
    plt.close()



###### Request Company Snapshot Charts ######

def fCreateCompanyCharts(df, tupleBonus):
    # Chart some data
    
    # Bar Charts
    fChartCo(df = df,
             strTitle = 'Median Hourly Pay (%)',
             listCols = ['PayMidF', 'PayMidM'],
             listLbls = [('Women', strClrF1), ('Men', strClrM1)],
             strSaveTo = r'images\CoPayMid.png')
    fChartCo(df = df,
             strTitle = 'Mean Hourly Pay (%)',
             listCols = ['PayAvgF', 'PayAvgM'],
             listLbls = [('Women', strClrF1), ('Men', strClrM1)],
             strSaveTo = r'images\CoPayAvg.png')
    fChartCo(df = df,
             strTitle = 'People Paid a Bonus (%)',
             listCols = ['FemaleBonusPercent', 'MaleBonusPercent'],
             listLbls = [('Women', strClrF1), ('Men', strClrM1)],
             strSaveTo = r'images\CoBns.png')
    fChartCo(df = df,
             strTitle = 'Median Bonus Pay (%)' if tupleBonus[0] else 'Median Bonus Pay\ncannot be calculated',
             listCols = ['BnsMidF', 'BnsMidM'],
             listLbls = [('Women', strClrF1), ('Men', strClrM1)],
             strSaveTo = r'images\CoBnsMid.png')
    fChartCo(df = df,
             strTitle = 'Mean Bonus Pay (%)' if tupleBonus[0] else 'Mean Bonus Pay\ncannot be calculated',
             listCols = ['BnsAvgF', 'BnsAvgM'],
             listLbls = [('Women', strClrF1), ('Men', strClrM1)],
             strSaveTo = r'images\CoBnsAvg.png')

    # Horizontal bar charts
    fChartCoH(df = df,
              strTitle = 'Employees by Gender (%)',
              listCols = ['PopTotF', 'PopTotM'],
              listLbls = [('Women', strClrF1), ('Men', strClrM1)],
              strSaveTo = r'images\CoPopTot.png')
    fChartCoH(df = df,
              strTitle = 'Bonus Recipients by Gender (%)' if  (tupleBonus[0] |  tupleBonus[1]) else 'No Bonus Recipients',
              listCols = ['PopBnsF', 'PopBnsM'],
              listLbls = [('Women', strClrF1), ('Men', strClrM1)],
              strSaveTo = r'images\CoPopBns.png')
    fChartCoH(df = df,
              strTitle = 'Share of Bonus Pool by Gender (%)' if  (tupleBonus[0] |  tupleBonus[1]) else 'No Bonus Recipients',
              listCols = ['BnsShrF', 'BnsShrM'],
              listLbls = [('Women', strClrF1), ('Men', strClrM1)],
              strSaveTo = r'images\CoBnsShr.png')
    
    # Chart "Population Pyramid"
    # Create a dataframe with the right data, then chart it
    dfQ = pd.DataFrame({'Quartile' : ['Lowest', 'Lower-Mid', 'Upper-Mid', 'Highest'],
                       'Women' : [-df.FemaleLowerQuartile[0], -df.FemaleLowerMiddleQuartile[0], -df.FemaleUpperMiddleQuartile[0], -df.FemaleTopQuartile[0]],
                       'Men' : [df.MaleLowerQuartile[0], df.MaleLowerMiddleQuartile[0], df.MaleUpperMiddleQuartile[0], df.MaleTopQuartile[0]]},
                      index = ['Q1', 'Q2', 'Q3', 'Q4'])
    fChartCoPyr(df = dfQ,
               strTitle = 'Hourly Pay Quartiles\nby Gender (%)',
               listLbls = [('Q1', strClrF1), ('Q2', strClrF2), ('Q3', strClrF3), ('Q4', strClrF4)],
               strSaveTo = r'images\CoPopPyr.png')
    
    # Chart "Population Pyramid2" - this includes a row for all employees combined
    # Create a dataframe with the right data, then chart it
    dfQ = pd.DataFrame({'Quartile' : ['All Staff\n(calculated)', '', 'Lowest Pay', 'Lower-Mid', 'Upper-Mid', 'Highest Pay'],
                       'Women' : [-df.PopTotF[0], 0, -df.FemaleLowerQuartile[0], -df.FemaleLowerMiddleQuartile[0], -df.FemaleUpperMiddleQuartile[0], -df.FemaleTopQuartile[0]],
                       'Men' : [df.PopTotM[0], 0, df.MaleLowerQuartile[0], df.MaleLowerMiddleQuartile[0], df.MaleUpperMiddleQuartile[0], df.MaleTopQuartile[0]]},
                      index = ['All', 'blank', 'Q1', 'Q2', 'Q3', 'Q4'])
    fChartCoPyr(df = dfQ,
               strTitle = 'Hourly Pay Quartiles\nby Gender (%)',
               listLbls = [('All', strClrM1), ('blank', strClrM1), ('Q1', strClrF1), ('Q2', strClrF2), ('Q3', strClrF3), ('Q4', strClrF4)],
               strSaveTo = r'images\CoPopPyr2.png')

    # Determine gender split data for complex graphics
    floatPopF = df.at[0,'PopTotF']
    floatPopM = df.at[0,'PopTotM']
    listWidths = [floatPopF, floatPopM]
    listWidthText = ['Women\nThe width of this bar\nshows that {:.0%} of\nemployees are women'.format(floatPopF),
                     'Men\nThe width of this bar\nshows that {:.0%} of\nemployees are men'.format(floatPopM)]
    
    # Complex Hourly Pay Graphic
    dfExtract = pd.DataFrame({'MyLabels' : listWidthText,
                               'Q1' : [df.PopFQ1[0], df.PopMQ1[0]],
                               'Q2' : [df.PopFQ2[0], df.PopMQ2[0]],
                               'Q3' : [df.PopFQ3[0], df.PopMQ3[0]],
                               'Q4' : [df.PopFQ4[0], df.PopMQ4[0]]},
                              index = ['Women', 'Men'])
    # Rescale decimals to percentages
    dfExtract.iloc[:, 1:(len(dfExtract.columns))] *= 100
    # Draw Chart
    figChart = fChartBarBig(df = dfExtract,
         strTitle = 'Employees Ranked By Hourly Pay',
         listLbls = [('Lowest Pay Quartile', strClrF1), ('Lower-Middle Quartile', strClrF2),
                     ('Upper-Middle Quartile', strClrF3), ('Highest Pay Quartile', strClrF4)],
         listWidths = listWidths)
    fAddAnnotationsPay(df = df, figChart = figChart)
    figChart.savefig(r'images\CoPayMain.png')
    plt.close()
    
    # Complex Bonus Pay Graphic
    dfExtract = pd.DataFrame({'MyLabels' : listWidthText,
                               'Q1' : [df.PopFBns0[0], df.PopMBns0[0]],
                               'Q2' : [df.FemaleBonusPercent[0], df.MaleBonusPercent[0]]},
                              index = ['Women', 'Men'])
    # Rescale decimals to percentages
    dfExtract.iloc[:, 1:(len(dfExtract.columns))] *= 100
    # Draw Chart
    figChart = fChartBarBig(df = dfExtract,
         strTitle = 'Employees Ranked By Bonus Pay',
         listLbls = [('People not paid a bonus', strClrF1), ('People paid a bonus', strClrF2)],
         listWidths = listWidths)
    if (df.FemaleBonusPercent[0] != 0) & (df.MaleBonusPercent[0] != 0):
        fAddAnnotationsBonus(df = df, figChart = figChart)
    figChart.savefig(r'images\CoBnsMain.png')
    plt.close()

def fChartCo(df, strTitle, listCols, listLbls, strSaveTo):
    # Create subset of data for charting.  Rescale to percentages.  Chart data.  Save.
    dfSubset = df.loc[:, listCols]
    dfSubset.iloc[:, 0:(len(dfSubset.columns))] *= 100
    figChart = fChartCoBar(df=dfSubset, strTitle=strTitle, listLbls=listLbls)
    figChart.savefig(strSaveTo)
    plt.close()
    
def fChartCoH(df, strTitle, listCols, listLbls, strSaveTo):
    # Create subset of data for charting.  Rescale to percentages.  Chart data.  Adjust plot height.  Save.
    dfSubset = df.loc[:, listCols]
    dfSubset.insert(loc=0, column='Blanks', value = '') # blank bar labels used to keep formatting
    dfSubset.iloc[:, 1:(len(dfSubset.columns))] *= 100
    figChart = fChartBarH(df=dfSubset, strTitle=strTitle, listLbls=listLbls, tupleSize=(3, 1))
    figChart.subplots_adjust(bottom=0.3, top=0.7)
    figChart.savefig(strSaveTo)
    plt.close()

def fChartCoPyr(df, strTitle, listLbls, strSaveTo):
    # Chart data.  Save.
    figChart = fChartBarPyramid(df=df, strTitle=strTitle, listLbls=listLbls)
    figChart.savefig(strSaveTo)
    plt.close()


###### CHART RENDERING ######

def fChartBarPyramid(df, strTitle, listLbls, tupleSize=(5, 5)):
    # Create the chart
    figChart, axesChart = plt.subplots(figsize=(tupleSize[0], tupleSize[1]))
    
    # Set spacing and labels of Y axis
    seriesLabels = df.iloc[:, 0]
    listYVals = list(range(0, len(df)))
    plt.yticks(ticks=listYVals, labels=seriesLabels, fontsize=12)

    # Set spacing and labels of X axis if not already defined
    listXVals = [df.loc[:, 'Women'].min()/2, df.loc[:, 'Men'].max()/2]
    plt.xticks(ticks=listXVals, labels=['Women', 'Men'], fontsize=16)
    
    # Need to fudge the axes location to fit in the y-axis labels
    plt.subplots_adjust(left=0.3, top=0.8)

    for intCol in range(1, len(df.columns)):
        for intRow in range(0, len(df)):
            # Set the data value
            floatData = df.iloc[intRow, intCol]
            # Plot the series    
            barSeries = axesChart.barh(y=intRow, width=floatData, height=1, left=0, 
                label=listLbls[intRow][0], color=listLbls[intRow][1], edgecolor='#FFFFFF')
            # Add labels to datapoints
            if floatData != 0:
                axesChart.bar_label(container=barSeries, labels=[round(100*abs(floatData))],
                                    label_type='center', color='#000000', fontsize=18)

    # Add a title
    plt.suptitle(t=strTitle, fontsize=20)
    # Add gridlines if the chart includes the "All Staff" in addition to quartile data
    if len(df) > 4:
        axesChart.set_xticks([df.loc['All', 'Women'], 0, df.loc['All', 'Men']], minor=True)
        plt.grid(axis='x', which='minor')
    # Hide tick marks and outline (spine)
    axesChart.spines[['left', 'right', 'top', 'bottom']].set_visible(False)
    axesChart.tick_params(axis='x', which='both', bottom=False, labelbottom=True)
    axesChart.tick_params(axis='y', which='both', left=False, labelleft=True)

    return figChart


def fChartBarBig(df, strTitle, listLbls, listWidths, tupleSize=(5, 5), maxStack=100):
    # Create the chart
    figChart, axesChart = plt.subplots(figsize=(tupleSize[0], tupleSize[1]))
    
    # Set spacing and labels of X axis
    listXVals = [0, 1.5]
    plt.xticks(ticks=listXVals, labels=df.iloc[:, 0], fontsize=8)

    # For a stacked chart, need to keep track of the cumulative values
    seriesStack = df.iloc[:, 1] * 0
    for intCol in range(1, len(df.columns)):
        # Set the data series
        seriesData = df.iloc[:, intCol]
        # Plot the series    
        barSeries = axesChart.bar(x=listXVals, height=seriesData, width=listWidths, bottom=seriesStack, 
            label=listLbls[intCol - 1][0], color=listLbls[intCol - 1][1], edgecolor='#FFFFFF')
        # Add labels to datapoints
        axesChart.bar_label(container=barSeries, fmt='{:.0f}', label_type='center', color='#000000', fontsize=12)
        # Record the cumulative bar values
        seriesStack += seriesData
    
    # Set the maximum y-axis value
    plt.ylim(0, max(maxStack, max(seriesStack)))
    plt.grid(axis='y')
    axesChart.yaxis.set_major_locator(plt.MultipleLocator(25))
    # Make space for the legend
    plt.subplots_adjust(bottom = 0.27)
    # Add a title and legend (legend needs to be added after series are defined)
    plt.suptitle(t=strTitle, fontsize=16)
    # Reorder the legend labels
    listHandles, listLabels = figChart.gca().get_legend_handles_labels()
    listOrder = list(reversed(range(len(listLabels))))
    figChart.legend(handles=[listHandles[i] for i in listOrder], labels=[listLabels[i] for i in listOrder],
                    loc='lower center', fontsize=8, ncols=1)     
    # Hide tick marks and outline (spine)
    axesChart.spines[['left', 'right', 'top', 'bottom']].set_visible(False)
    axesChart.tick_params(axis='x', which='both', bottom=False, labelbottom=True)
    axesChart.tick_params(axis='y', which='both', left=False, labelleft=True)

    return figChart


def fAddAnnotationsPay(df, figChart):
    # Add annotations - Pay
    floatX = df.at[0,'PopTotF'] / 2
    axesChart = figChart.axes[0]
    # Add the median annotation
    axesChart.text(s=('The median hourly pay gap of\n' +
                      '{:.2f}%'.format(100 * df.at[0,'DiffMedianHourlyPercent']) +
                      ' means this woman\n' +
                      'earns £{:.2f} for every £100\n'.format(100 * df.at[0,'PayMidF']) +
                      'this man earns when working\nthe same number of hours'),
                   x=floatX + 0.5, y=77, fontsize=8, ha='center', va='bottom', wrap=True)
    axesChart.annotate(text='', xy=(floatX, 50), xytext=(floatX + 0.3, 73),
            arrowprops=dict(width=2, shrink=0, facecolor='#000000'))
    axesChart.annotate(text='', xy=(floatX + 1, 50), xytext=(floatX + 0.7, 73),
            arrowprops=dict(width=2, shrink=0, facecolor='#000000'))
    # Add the low pay bracket annotation
    axesChart.text(s=('{:.0f}%'.format(100 * df.at[0,'PopFQ1']) +
                      ' of women\nand ' +
                      '{:.0f}%'.format(100 * df.at[0,'PopMQ1']) +
                      ' of men\n' +
                      'are in the lowest\npay bracket'),
                   x=floatX + 0.5, y=27, fontsize=8, ha='center', va='bottom', wrap=True)
    axesChart.annotate(text='', xy=(floatX, df.at[0,'PopFQ1'] / 0.02),
                       xytext=(floatX + 0.2, 30),
            arrowprops=dict(width=2, shrink=0, facecolor='#000000'))
    axesChart.annotate(text='', xy=(floatX + 1, df.at[0,'PopMQ1'] / 0.02),
                       xytext=(floatX + 0.8, 30),
            arrowprops=dict(width=2, shrink=0, facecolor='#000000'))


def fAddAnnotationsBonus(df, figChart):
    # Add annotations - Bonus
    floatX = df.at[0,'PopTotF'] / 2
    axesChart = figChart.axes[0]
    axesChart.text(s=('The median bonus pay gap of\n' +
                      '{:.2f}%'.format(100 * df.at[0,'BnsMidD']) +
                      ' means this woman\n' +
                      'earns £{:.2f} for every £100\n'.format(100 * df.at[0,'BnsMidF']) +
                      'this man earns in bonus pay\nannually'),
                   x=floatX + 0.5, y=23, fontsize=8, ha='center', va='top', wrap=True)
    axesChart.annotate(text='', xy=(floatX, 100 - df.at[0,'FemaleBonusPercent'] / 0.02),
                       xytext=(floatX + 0.25, 27.5),
                       arrowprops=dict(width=2, shrink=0, facecolor='#000000'))
    axesChart.annotate(text='', xy=(floatX + 1, 100 - df.at[0,'MaleBonusPercent'] / 0.02),
                       xytext=(floatX + 0.75, 27.5),
                       arrowprops=dict(width=2, shrink=0, facecolor='#000000'))


def fChartCoBar(df, strTitle, listLbls, tupleSize=(4, 4), maxStack=100):  
    # Create the chart
    figChart, axesChart = plt.subplots(figsize=(tupleSize[0], tupleSize[1]))
    
    # Set spacing and labels of X axis if not already defined
    listXVals = list(range(0, len(df.columns)))
    plt.xticks(ticks=listXVals, labels=df.head(), fontsize=8)

    # Loop through columns, plotting data points    
    for intCol in range(0, len(df.columns)):
        # Set the data value
        floatData = df.iloc[0, intCol]
        # Plot the series
        barSeries = axesChart.bar(x=listXVals[intCol], height=floatData, width=1,
            label=listLbls[intCol][0], color=listLbls[intCol][1], edgecolor='#FFFFFF')
        if floatData != 0:
            # Add labels to datapoints
            axesChart.bar_label(container=barSeries,
                fmt='{:.2f}',
                label_type='center', color='#000000', fontsize=18)
        # Keep track of the highest bar for setting the y-axis size
        maxStack = max(maxStack, floatData)
    
    # Set the maximum y-axis value
    plt.ylim(0, maxStack)
    # Add a title and legend
    plt.suptitle(t=strTitle, fontsize=20)
    figChart.legend(loc='lower center', fontsize=16, ncols=2) 
    # Hide tick marks and outline (spine)
    axesChart.spines[['left', 'right', 'top', 'bottom']].set_visible(False)
    axesChart.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    axesChart.tick_params(axis='y', which='both', left=False, labelleft=False)
    
    return figChart


def fChartTsBar(df, strTitle, listLbls, tupleSize=(3.5, 3.5), maxStack=100):
    # Create the chart
    figChart, axesChart = plt.subplots(figsize=(tupleSize[0], tupleSize[1]))
    
    # Set spacing and labels of X axis
    seriesLabels = df.iloc[:, 0]
    listXVals = list(range(0, len(df)))
    plt.xticks(ticks=listXVals, labels=seriesLabels, fontsize=8)

    # For a stacked chart, need to keep track of the cumulative values
    seriesStack = df.iloc[:, 1] * 0
    for intCol in range(1, len(df.columns)):
        # Set the data series
        seriesData = df.iloc[:, intCol]
        # Plot the series    
        barSeries = axesChart.bar(x=listXVals, height=seriesData, width=1, bottom=seriesStack, 
            label=listLbls[intCol - 1][0], color=listLbls[intCol - 1][1], edgecolor='#FFFFFF')
        # Add labels to datapoints
        axesChart.bar_label(container=barSeries, fmt='{:.0f}', label_type='center', color='#000000', fontsize=9)
        # Record the cumulative bar values
        seriesStack += seriesData
    
    # Set the maximum y-axis value
    plt.ylim(0, max(maxStack, max(seriesStack)))
    # Make space for the legend
    plt.subplots_adjust(bottom = 0.1 + 0.05 * (len(df.columns) // 2))
    # Add a title and legend (legend needs to be added after series are defined)
    plt.suptitle(t=strTitle)
    figChart.legend(loc='lower center', fontsize=8, ncols=2)    
    # Hide tick marks and outline (spine)
    axesChart.spines[['left', 'right', 'top', 'bottom']].set_visible(False)
    axesChart.tick_params(axis='x', which='both', bottom=False)
    axesChart.tick_params(axis='y', which='both', left=False, labelleft=False)

    return figChart

##### DICT INFO SEEMS OVERKILL FOR SINGLE PARAMETER? #####
def fChartBarH(df, strTitle, listLbls, tupleSize=(3.5, 3.5), maxStack=100, blnLabel=True, **dictInfo):
    # Create the chart
    figChart, axesChart = plt.subplots(figsize=(tupleSize[0], tupleSize[1]))
    
    # Set spacing and labels of Y axis
    seriesLabels = df.iloc[:, 0]
    listYVals = list(range(0, len(df)))
    plt.yticks(ticks=listYVals, labels=seriesLabels, fontsize=6)
    
    # Need to fudge the axes location to fit in the y-axis labels
    plt.subplots_adjust(left=max(0.1, 0.018 * seriesLabels.str.len().max()))

    # For a stacked chart, need to keep track of the cumulative values
    seriesStack = df.iloc[:, 1] * 0
    for intCol in range(1, len(df.columns)):
        # Set the data series
        seriesData = df.iloc[:, intCol]
        # Plot the series    
        barSeries = axesChart.barh(y=listYVals, width=seriesData, height=1, left=seriesStack, 
            label=listLbls[intCol - 1][0], color=listLbls[intCol - 1][1], edgecolor='#FFFFFF')
        # Add labels to datapoints
        axesChart.bar_label(container=barSeries, fmt='{:.0f}', label_type='center', color='#000000', fontsize=9)
        # Record the cumulative bar values
        seriesStack += seriesData

    if 'tupleHiLit' in dictInfo:
        # Reset index so Y position can be found
        df.reset_index(drop=True, inplace=True)
        intY = df[df[dictInfo['tupleHiLit'][0]] == dictInfo['tupleHiLit'][1]].index[0]
        # Find end of bar for the row
        floatX = 0
        for intCol in range(1, len(df.columns)):
            floatX += df.iloc[intY, intCol]
        # Overlay a black box around the existing bar
        barSeries = axesChart.barh(y=intY, width=floatX, height=1, fill=False, edgecolor='#000000')
    
    # Set the maximum x-axis value to remove redundant white space in axes
    # Set 1% larger to allow highlight border to display properly    
    plt.xlim(0, 1.01 * max(maxStack, max(seriesStack)))
    # Add a title and legend (legend needs to be added after series are defined)
    plt.suptitle(t=strTitle)
    figChart.legend(loc='lower center', fontsize=8, ncols=2)    
    # Hide tick marks and outline (spine)
    axesChart.spines[['left', 'right', 'top', 'bottom']].set_visible(False)
    axesChart.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    axesChart.tick_params(axis='y', which='both', left=False, labelleft=blnLabel)

    return figChart
