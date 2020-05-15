import pandas as pd
import numpy as np
import time
import datetime


df = pd.read_csv('/Users/Mike_F/Desktop/US_Accidents_Dec19.csv')

df.drop(['TMC','Description','Country','Timezone','Airport_Code','Weather_Timestamp','Traffic_Calming','Traffic_Signal','Turning_Loop','Amenity','Bump','Crossing','Give_Way','Junction','No_Exit','Railway','Roundabout','Station','Stop','ID','Wind_Speed(mph)','Precipitation(in)','Visibility(mi)','Wind_Chill(F)','End_Lat','End_Lng'], axis = 1, inplace = True)

df[['Start_Date', 'Start_Time']] = df['Start_Time'].str.split(' ', n=1, expand=True)

df['Start_Date'] = pd.to_datetime(df['Start_Time'])

df[['End_Date', 'End_Time']] = df['End_Time'].str.split(' ', n=1, expand=True)

df['End_Date'] = pd.to_datetime(df['End_Time'])


df['Start_Year'] = df['Start_Date'].apply(lambda date: date.year)
df['Start_Month'] = df['Start_Date'].apply(lambda date: date.month)
df['Start_Day'] = df['Start_Date'].apply(lambda date: date.day)

df.drop(df[df['Start_Year'] < 2019].index, inplace = True)

df['Difference'] = (df['End_Date'] - df['Start_Date'])

df.drop(['Start_Date'], axis=1,inplace=True)
df.drop(['End_Date'], axis=1,inplace=True)

pd.DataFrame.to_csv(df,"" + time.strftime('Ticket %Y-%m-%d') + ".csv",',')