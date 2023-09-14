import pandas as pd
import numpy as np
import math

# read excel
dfA= pd.read_excel('Running Dinner dataset 2022.xlsx', sheet_name='Bewoners')
dfB = pd.read_excel('Running Dinner dataset 2022.xlsx', sheet_name='Adressen')
dfC = pd.read_excel('Running Dinner dataset 2022.xlsx', sheet_name='Paar blijft bij elkaar')
dfD = pd.read_excel('Running Dinner dataset 2022.xlsx', skiprows=[0], sheet_name='Buren')
dfE = pd.read_excel('Running Dinner dataset 2022.xlsx', skiprows=[0], sheet_name='Kookte vorig jaar')
dfF = pd.read_excel('Running Dinner dataset 2022.xlsx', skiprows=[0], sheet_name='Tafelgenoot vorig jaar')

df = dfA.merge(dfB, how = 'left', on ='Huisadres')


#Zorgen dat het huisadres hetzelfde is alsin personen. Dit om later makkelijker te kunnen slicen. 
for i in range(len(df['Huisadres'])):
    df.loc[i, 'Huisadres'] = df['Huisadres'][i][0:2] + '_' + df['Huisadres'][i][2:]

df.to_excel('Output.xlsx')

for i in range(len(df['Huisadres'])):
    if df['Huisadres'][i] in df['Bewoner'][i]:
        	print(df['Bewoner'][i])
         
         
         
         
         
   
   
   
   
   
   
   
   
   
   
   print('hoi Sam')      