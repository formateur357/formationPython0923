#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#C:\\Users\\mperrette\\Documents\\PROJETS\\23_Formation_python\\FormationSept2023\\Exos\\formationPython0923\\exercices\\meteo.json

import pandas as pd
import matplotlib.pyplot as plt

plt.close("all")

data = pd.read_json('C:\\Users\\mperrette\\Documents\\PROJETS\\23_Formation_python\\FormationSept2023\\Exos\\formationPython0923\\exercices\\meteo.json')
df = pd.json_normalize(data['results'])

#on filtre les entrées sans nom de département
filtre = df['nom_dept'].notnull()
filteredDepts = df[filtre]
df = filteredDepts
filtre = df['temp_max'].notnull()
resultat = df[filtre]
df = resultat
filtre = df['temp_min'].notnull()
resultat = df[filtre]
print(resultat)

resultat['temp_moy'] = (resultat['temp_min']+resultat['temp_max']) / 2

print(resultat[['nom_dept', 'temp_moy']])

FiltrePluie = filteredDepts['humidity']>10
Joursdepluie = filteredDepts[FiltrePluie]
print(Joursdepluie)
Joursdepluie.to_csv('C:\\Users\\mperrette\\Documents\\PROJETS\\23_Formation_python\\FormationSept2023\\Exos\\formationPython0923\\exercices\\precipitations_elevees.csv')

resultat.plot(x='date', y='temp_moy', title = 'Evolution de la temperature en fonction du temps',xlabel='date', ylabel='temperature')
plt.show()