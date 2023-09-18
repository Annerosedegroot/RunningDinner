import random
import numpy as np
import pandas as pd

Mensen = ["M_1", "V_1", "M_2", "V_2", "M_3", "V_3", "M_4", "V_4", "M_5", "V_5"]
Huizen = ['H_1', 'H_2', 'H_3', 'H_4', 'H_5']
grootteHuizen = [3,2,0,3,2]

dfMensen = pd.DataFrame(Mensen, columns=['Mensen'])
dfHuizen = pd.DataFrame(Huizen, columns=['Huizen'])

huizendict = dict()
available_individuals = dfMensen['Mensen'].tolist()
dfGangen = pd.DataFrame()


gang = ['Voorgerecht', 'Hoofdgerecht', 'Nagerecht']


for j in range(len(gang)):
    for i in range(len(Huizen)):
        huisgrootte = grootteHuizen[i]
        # Check if there are enough individuals left to choose from
        if len(available_individuals) < 2:
            break  # No more unique individuals to select
        
        random_persons = random.sample(available_individuals, huisgrootte)
        huizendict[Huizen[i]] = random_persons
        

        available_individuals = [ind for ind in available_individuals if ind not in random_persons]
        dfTijdelijk = pd.DataFrame(huizendict[f'{Huizen[i]}'])
    dfGangen = pd.concat([dfGangen, dfTijdelijk])



print(dfGangen)
