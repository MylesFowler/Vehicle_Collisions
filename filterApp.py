import pandas as pd
import numpy as np
import datetime 
import time


df = pd.read_csv('/Users/Mike_F/Desktop/US_Accidents_Dec19.csv')

df.drop(['End_Time','ID','Wind_Speed(mph)','Precipitation(in)','Visibility(mi)','Wind_Chill(F)','Start_Lng','End_Lat','End_Lng'], axis = 1, inplace = True)

df[['Start_Date', 'Start_Time']] = df['Start_Time'].str.split(' ', n=1, expand=True)
df['Start_Date'] = pd.to_datetime(df['Start_Date'])

df['Start_Year'] = df['Start_Date'].apply(lambda date: date.year)
df['Start_Month'] = df['Start_Date'].apply(lambda date: date.month)
df['Start_Day'] = df['Start_Date'].apply(lambda date: date.day)

df.drop(df[df['Start_Year'] < 2019].index, inplace = True)

df.drop(['Start_Date'], axis=1,inplace=True)

pd.DataFrame.to_csv(df,"" + time.strftime('Ticket %Y-%m-%d') + ".csv",',')