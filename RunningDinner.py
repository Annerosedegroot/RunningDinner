import pandas as pd
import numpy as np
import math

#Geef hier de naam van de nieuwe excel database op:
ExcelInput = 'Running Dinner dataset 2022.xlsx'


#Hier gaan we de excel tabbladen naar verschillende DataFrames inlezen.
dfA = pd.read_excel(ExcelInput, sheet_name='Bewoners')
dfB = pd.read_excel(ExcelInput, sheet_name='Adressen')
dfC = pd.read_excel(ExcelInput, sheet_name='Paar blijft bij elkaar')
dfD = pd.read_excel(ExcelInput, skiprows=[0], sheet_name='Buren')
dfE = pd.read_excel(ExcelInput, skiprows=[0], sheet_name='Kookte vorig jaar')
dfF = pd.read_excel(ExcelInput, skiprows=[0], sheet_name='Tafelgenoot vorig jaar')

#Hier gaan we de verschillende dataframes samenvoegen tot 1 enkele dataframe

df = dfA.merge(dfB, how = 'left', on ='Huisadres')



#Zorgen dat de lijst met huisadressen hetzelfde is als de lijst met personen. Dit om later makkelijker te kunnen slicen. String slicen
for i in range(len(df['Huisadres'])):
    df.loc[i, 'Huisadres'] = df['Huisadres'][i][0:2] + '_' + df['Huisadres'][i][2:]


#Een lijst maken zodat er later een extra colom kan worden toegevoegd aan de dataframe om te zien of er mensen bij elkaar moeten blijven of niet. 
Bijelkaarbinairlijst = list()
for i in range(len(df['Huisadres'])):
    if df['Huisadres'][i] == 'WO_59' or df['Huisadres'][i] == 'WO_25':
        Bijelkaarbinairlijst.append(1)
    elif df['Huisadres'][i] != 'WO_59' and df['Huisadres'][i] != 'WO_25':
        Bijelkaarbinairlijst.append(0)

#De colom maken om te kunnen visualiseren welke personen er bij iemand moeten blijven

df['Koppel blijft bijelkaar'] = Bijelkaarbinairlijst

#Verzamelingen definieren
Huisadres = df['Huisadres']
Deelnemers = df['Bewoner']
print(df)




df.to_excel('Output.xlsx')  
         
