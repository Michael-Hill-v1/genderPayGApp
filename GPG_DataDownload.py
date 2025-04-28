# pip install pandas

import pandas as pd
import requests
import os

def fMain():
    strFolder = r'data' 
    strFileOut = r'data\data.csv'
    intMaxYear = fDownloadFiles(strTo=strFolder)
    fAmalgamateRawFiles(strPathIn=strFolder, strFileOut=strFileOut, intMaxYear=intMaxYear)

###### Download data from gov.uk ######

def fDownloadFiles(strTo):
    intYear = 2017
    while True:
        strUrl = 'https://gender-pay-gap.service.gov.uk/viewing/download-data/' + str(intYear)
        try:
            response = requests.get(strUrl)
        except requests.exceptions.RequestException as error:
            print(error)
            raise SystemExit(error)
        else:
            intStatus = response.status_code
            if intStatus == 200:
                # Save the file
                with open(os.path.join(strTo, str(intYear) + '.csv'), 'wb') as fileOut:
                    fileOut.write(response.content)
                # Check for the next year
                intYear += 1
            else:
                # should be error 404 as the year is in the future
                break
    return intYear

##### AMALGAMATE, CLEAN, AND ENHANCE DATA #####
# Populate Nulls in SicCode with filler value

def fAmalgamateRawFiles(strPathIn, strFileOut, intMaxYear):
    # Start an empty dataframe. Open each file. Add a 'year' column. Add contents to dataframe.
    df = pd.DataFrame()
    for intYear in range(2017, intMaxYear):
        strFile = r'{}\{}.csv'.format(strPathIn, intYear)
        dfYear = pd.read_csv(filepath_or_buffer=strFile, converters = {'EmployerId': str})
        dfYear['Year'] = intYear
        df = pd.concat(objs=[df, dfYear])
    # Sort by year in case it isn't already.
    df = df.sort_values('Year', ascending=True)
    # Calculate additional columns
    df = fTranslateSic(df=df, strPathIn=strPathIn)
    df = fModifyDataset(df=df)
    # Save a copy of the amended data as csv
    df.to_csv(path_or_buf=strFileOut, index=False)
    
def fTranslateSic(df, strPathIn):
    # Map the SIC codes to Industry Names
    strFile = r'{}\SIC07_CH_condensed_list_en.csv'.format(strPathIn)
    dfMap = pd.read_csv(filepath_or_buffer=strFile)
    # Get rid of commas from the descriptions.  Will be splitting strings by commas later.
    dfMap['Description'] = dfMap['Description'].str.replace(',', '')
    # Add in the undefined code '1' that gets used in the GPG data
    dfMap = pd.concat([dfMap, pd.DataFrame({'SIC Code': [1], 'Description': ['Undefined Public Sector']})])
    # Put codes in reverse order and re-index.  Codes in the source file are missing leading zeroes.
    # This should help ensure replacements are on exact matches rather than partial matches.
    dfMap = dfMap.sort_values('SIC Code', ascending=False)
    dfMap = dfMap.reset_index(drop=True)
    # Loop through the list and make the replacements.  
    df['Industry'] = df['SicCodes'].fillna('Unknown')
    for idx in dfMap.index:
        df['Industry'] = df['Industry'].str.replace(str(dfMap['SIC Code'][idx]), dfMap['Description'][idx])
    return df

def fModifyDataset(df):
    # Rescale percentages to decimals for easier calculations
    df = fRescalePercentages(df)
    # Add new column with shortened Employer Names in upper case for better chart labels
    df = fAddNewNames(df)
    # Fix dodgy Bonus pay gap data
    df = fCleanBonusData(df)
    # Calculate how much women get per £1 a man gets
    df = fDeriveFemalePay(df)
    # Calculate portion of the workforce for each gender
    df = fDerivePopByGender(df)
    # Calculate portion of each gender by pay quartile
    df = fDeriveGenderPopByPayQuartile(df)
    # Calculate portion of the workforce by gender and whether they got a bonus
    df = fDerivePopByGenderAndBonus(df)
    # Calculate the share of bonus pool by gender    
    df = fDeriveBonusByGender(df)
    return df

def fRescalePercentages(df):
    # Rescale percentages to decimals for easier calculations
    df.loc[:, 'DiffMeanHourlyPercent':'FemaleTopQuartile'] /= 100
    return df

def fAddNewNames(df):
    # Add new column with Employer Names in upper case
    df['Names'] = df['EmployerName'].str.upper()
    # Clean / Shorten Names
    # Define a list of target phrases and replacement values
    listTuplePairs = [
        (',', ''),
        ('.', ''),
        (' LIMITED',  ''), 
        (' LTD',''),
        (' ASSET MANAGEMENT', ' ASSET MGMT'),
        (' INVESTMENT MANAGEMENT', ' INV MGMT'),
        (' MANAGEMENT', ' MGMT'),
        (' INTERNATIONAL', ' INTL')
    ]
    # Loop through the list and make the replacements
    for tuplePair in listTuplePairs:
        df['Names'] = df['Names'].str.replace(tuplePair[0], tuplePair[1])
    return df    
    
def fCleanBonusData(df):
    # Need to handle nulls and incorrect values for DiffMeanBonusPercent and DiffMedianBonusPercent
    # These occur when  MaleBonusPercent = 0, as they can't be calculated
    # Set to zero, even though that's wrong
    # Where FemaleBonusPercent = 0 and MaleBonusPercent != 0 there is inconsistent treatment
    # Some report gaps of 100%, others 0%, and other weird values
    # Set to 100%, as that's right
    df['BnsAvgD'] = df.apply(lambda row:
        0 if (row['MaleBonusPercent'] == 0)
        else 1 if ((row['MaleBonusPercent'] != 0) & (row['FemaleBonusPercent'] == 0))
        else row['DiffMeanBonusPercent'], axis=1)
    df['BnsMidD'] = df.apply(lambda row:
        0 if (row['MaleBonusPercent'] == 0)
        else 1 if ((row['MaleBonusPercent'] != 0) & (row['FemaleBonusPercent'] == 0))
        else row['DiffMedianBonusPercent'], axis=1)
    return df

def fDeriveFemalePay(df):
    # Calculate how much women get per £1 a man gets
    df['PayAvgF'] = 1 - df.DiffMeanHourlyPercent
    df['PayMidF'] = 1 - df.DiffMedianHourlyPercent
    df['BnsAvgF'] = df.apply(lambda row:
        0 if (row['FemaleBonusPercent'] == 0)
        else 1 - row['BnsAvgD'], axis=1)
    df['BnsMidF'] = df.apply(lambda row:
        0 if (row['FemaleBonusPercent'] == 0)
        else 1 - row['BnsMidD'], axis=1)
    # Set how much pay men get (£1)
    df[['PayAvgM', 'PayMidM']] = [1, 1]
    # Set how much bonus men get (£1 if bonus received, else £0)
    df['BnsAvgM'] = df.apply(lambda row: '1' if row['MaleBonusPercent'] > 0 else 0, axis=1)
    df['BnsMidM'] = df['BnsAvgM']    
    return df

def fDerivePopByGender(df):
    # Calculate portion of the workforce for each gender
    df['PopTotM'] = 0.25 * (df.MaleLowerQuartile +
                            df.MaleLowerMiddleQuartile +
                            df.MaleUpperMiddleQuartile +
                            df.MaleTopQuartile)
    df['PopTotF'] = 0.25 * (df.FemaleLowerQuartile +
                            df.FemaleLowerMiddleQuartile +
                            df.FemaleUpperMiddleQuartile +
                            df.FemaleTopQuartile)
    return df

def fDeriveGenderPopByPayQuartile(df):    
    # Calculate portion of each gender by pay quartile
    df['PopMQ1'] = 0.25 * df.MaleLowerQuartile / df.PopTotM
    df['PopMQ2'] = 0.25 * df.MaleLowerMiddleQuartile / df.PopTotM
    df['PopMQ3'] = 0.25 * df.MaleUpperMiddleQuartile / df.PopTotM
    df['PopMQ4'] = 0.25 * df.MaleTopQuartile / df.PopTotM
    df['PopFQ1'] = 0.25 * df.FemaleLowerQuartile / df.PopTotF
    df['PopFQ2'] = 0.25 * df.FemaleLowerMiddleQuartile / df.PopTotF
    df['PopFQ3'] = 0.25 * df.FemaleUpperMiddleQuartile / df.PopTotF
    df['PopFQ4'] = 0.25 * df.FemaleTopQuartile / df.PopTotF
    # Calculate 'half-iles' too
    df['PopMH1'] = df['PopMQ1'] + df['PopMQ2']
    df['PopFH1'] = df['PopFQ1'] + df['PopFQ2']
    return df

def fDerivePopByGenderAndBonus(df):
    # Calculate portion of each gender with no bonus
    df['PopMBns0'] = 1 - df.MaleBonusPercent
    df['PopFBns0'] = 1 - df.FemaleBonusPercent
    # Calculate portion of the workforce by gender and whether they got a bonus
    df['PopTotBnsM'] = df.PopTotM * df.MaleBonusPercent
    df['PopTotNoBnsM'] = df.PopTotM - df.PopTotBnsM
    df['PopTotBnsF'] = df.PopTotF * df.FemaleBonusPercent
    df['PopTotNoBnsF'] = df.PopTotF - df.PopTotBnsF
    # Calculate portion of the workforce who have a bonus by gender
    df['PopBnsM'] = df.PopTotBnsM / (df.PopTotBnsM + df.PopTotBnsF)
    df['PopBnsF'] = df.PopTotBnsF / (df.PopTotBnsM + df.PopTotBnsF)
    return df

def fDeriveBonusByGender(df):
    # Calculate the share of bonus pool by gender
    df['BnsTotM'] = df.PopBnsM * 1
    df['BnsTotF'] = df.PopBnsF * df.BnsAvgF
    df['BnsShrM'] = df.BnsTotM / (df.BnsTotM + df.BnsTotF)
    df['BnsShrF'] = df.BnsTotF / (df.BnsTotM + df.BnsTotF)
    df = df.drop(columns=['BnsTotM', 'BnsTotF'])
    return df

fMain()
