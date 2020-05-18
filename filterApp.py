import pandas as pd
import numpy as np
import time
import datetime

df = pd.read_csv('/Users/Mike_F/Desktop/US_Accidents_Dec19.csv')

df.drop(['TMC','Description','Country','Timezone','Airport_Code','Weather_Timestamp','Traffic_Calming','Traffic_Signal','Turning_Loop','Amenity','Bump','Crossing','Give_Way','Junction','No_Exit','Railway','Roundabout','Station','Stop','ID','Wind_Speed(mph)','Precipitation(in)','Visibility(mi)','Wind_Chill(F)','End_Lat','End_Lng'], axis = 1, inplace = True)
#df['Start_Time'].astype(str).str[-5:-5]
df[['Start_Date', 'Start(time)']] = df['Start_Time'].str.split(' ', n=1, expand=True)

df['Start_Date'] =  pd.to_datetime(df['Start_Time'])

df[['End_Date', 'End(time)']] = df['End_Time'].str.split(' ', n=1, expand=True)

df['End_Date'] = pd.to_datetime(df['End_Time'])

df['Difference'] = (df['End_Date'] - df['Start_Date']).astype(str).str[-15:-13]

df['Start_year'] = df['Start_Date'].dt.year
df['Start_month'] = df['Start_Date'].dt.month
df['Start_day'] = df['Start_Date'].dt.day

#drop tables < 2019
df.drop(df[df['Start_year'] < 2018].index, inplace = True)

df.drop(df[df['City'] != 'Los Angeles'].index, inplace = True)

#drop unused tables
df.drop(['Start_Time','End_Time','Start_Date','End_Date'], axis=1,inplace=True)

print(df.corr())
pd.DataFrame.to_csv(df,"" + time.strftime('%Y-%m-%d') + ".csv",',')

#https://www.kaggle.com/sobhanmoosavi/us-accidents
