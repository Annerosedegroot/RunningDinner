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
print(df)
df.to_excel('Output.xlsx')