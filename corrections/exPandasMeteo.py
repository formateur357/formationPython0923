#! /usr/bin/env python3

import pandas as pd
import datetime
import matplotlib.pyplot as mp

data = pd.read_json('/Users/morganguy/Formation_Workspace/formationPython0923/exercices/meteo.json')
# print(data)

df = pd.DataFrame(pd.json_normalize(data['results']))
# print(df.head(6))

df['temp_moy'] = (df['temp_max'] + df['temp_min']) / 2
# print(df.head(10))

jour_le_plus_chaud = df[df['temp_max'] == df['temp_max'].max()]
jour_le_plus_froid = df[df['temp_min'] == df['temp_min'].min()]
moyenne_humidite = df['humidity'].mean()
# print(jour_le_plus_chaud)
# print(jour_le_plus_froid)
# print(moyenne_humidite)

jours_precipitations_elevees = df[df['humidity'] > 80]

# jours_precipitations_elevees.to_csv('humidity.csv', index=False)
# jours_precipitations_elevees.to_json('humidity.json', orient='records')
# print(jours_precipitations_elevees)

# df.plot(x='date', y="temp", title="Evolution de la temperature", xlabel="Date", ylabel="Temperature en Degree Celsius")
# mp.show()

df['Mois'] = (df['date'])

print(df)