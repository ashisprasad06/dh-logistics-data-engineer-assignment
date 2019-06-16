# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 12:06:57 2019

@author: ashis.prasad
"""


import re
import pandas as pd
import numpy as np
import datetime
from pandas import DataFrame, Series
import sys
from ParameterFilesandValue import *


def FormatDTString(dt):
    return dt.replace(' ', 'T')+'.000Z'


def GenerateDeNormalizedDF():
    
    '''
    This function will created DeNormalized Dataframe
    
    return MergedDf = Denormalized Df
    '''
    try:
        # Create dataframes using the input file and look-up file
        LookupDf=pd.read_csv(referencepath+referencefilname)
        chunk_list=[]
        for df in pd.read_csv(inputpath+inputfilename, chunksize=500000):
            chunk_list.append(df[['DOLocationID','tip_amount', 'tpep_dropoff_datetime', 'trip_distance']])
            del(df)
            
        Maindf=pd.concat(chunk_list)
        # Merge both Dataframe into 1 to de-normalize the data further using Column mentioned in left_on and right_on key
        MergedDf=pd.merge(Maindf, LookupDf, how='inner', left_on='DOLocationID', right_on='LocationID')
    
        del(Maindf)
        return MergedDf
    
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()


def GenerateTopTippingZone(InputDataFrame):
    
    '''
    This function will create file with Top Tipping Zone
    
    Input : This requires input dataframe object
    Output : This will create output file in Output Directory
    '''
    try:
        Temp_TipAmountDf=InputDataFrame[['Borough','tip_amount', 'Zone']].copy()
        Final_Df=Temp_TipAmountDf.groupby(['Borough','Zone'])[['tip_amount']].sum().sort_values(by='tip_amount', ascending=False).head(5)
        del(Temp_TipAmountDf)
        Final_Df.to_csv(outputpath+Output_File_TopTipping_Zone)
        del(Final_Df)
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()



def GenerateLongestTripperDay(InputDataFrame):  
    
    '''
    This function will create file with Top Tipping Zone
    
    Input : This requires input dataframe object
    Output : This will create output file in Output Directory
    '''
    try:
        # Extracting required from InputDataFrame
        Temp_PerDayTrip=InputDataFrame[['tpep_dropoff_datetime', 'trip_distance', 'Borough', 'Zone']].copy()
        
        #Add Required Columns Drop_off_Dt and Week
        Temp_PerDayTrip['Drop_off_Dt']=pd.to_datetime(Temp_PerDayTrip['tpep_dropoff_datetime']).dt.date
        Temp_PerDayTrip['week']=pd.to_datetime(Temp_PerDayTrip['tpep_dropoff_datetime']).dt.week
        
        #Filter the rows which has either Null Zone or Unknown Borough or if does not fall in 1st week of Jan, 2018
        Temp_PerDayTrip2=Temp_PerDayTrip[(pd.to_datetime(Temp_PerDayTrip['tpep_dropoff_datetime']).dt.year == 2018) & (Temp_PerDayTrip['week'] == 1) & ((Temp_PerDayTrip['Borough'] != 'Unknown') | (Temp_PerDayTrip['Zone'].notnull()))].copy()
        
        #Empty the Temp_PerDayTrip to release memory
        del(Temp_PerDayTrip)
        
        #Calculate Rank of Trip Distance on basis of Drop_off_Dt
        CalculateRnk=Temp_PerDayTrip2.groupby(['Drop_off_Dt'])
        Temp_PerDayTrip2['RN']=CalculateRnk['trip_distance'].rank(ascending=False)
        
        # Create Final DataFrame
        Final_Df=Temp_PerDayTrip2[Temp_PerDayTrip2['RN'] <= 5.0 ].sort_values(by=['Drop_off_Dt', 'trip_distance'], ascending=[True,False]).copy()
        
        #Empty the Temp_PerDayTrip to release memory
        del(Temp_PerDayTrip2)
        
        #Change the Format of Trip_Drop_off_Dttm
        Final_Df['tpep_dropoff_datetime']=[FormatDTString(x) for x in Final_Df['tpep_dropoff_datetime']]
        
        #export the final result in to CSV file
        
        Header=['Drop_off_Dt', 'tpep_dropoff_datetime', 'Borough', 'Zone','trip_distance']
        Final_Df.to_csv(outputpath+Output_File_LongTripPerDay, columns=Header, index=None)
        del(Final_Df)
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()

