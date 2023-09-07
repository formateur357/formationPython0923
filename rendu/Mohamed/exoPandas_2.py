# %%
#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd


dataload = pd.read_json("meteo.json")
data = pd.json_normalize(dataload['results'])
df = pd.DataFrame(data)

print("################Afficher les 5 premier ligne#########")
print(df.loc[1:5])
print("################la température moyenne quotidienne##########")
df["temp_moy"] = (df['temp_min'] + df['temp_max']) / 2
# print(df.loc[:, ['temp_min', 'temp_max']].mean())
print(df)
print("################la température la plus haute##########")
print(df.loc[:, ["temp"]].max())
print("################la température la plus basse##########")
print(df.loc[:, ["temp"]].min())
print("################la moyenne des précipitations##########")
print(df.loc[:, ["humidity"]].mean())
print("################précipitations étaient supérieures à 10 millimètres##########")
df2 = df.where(df.humidity > 60)

df2.to_json('precipitations_elevees.json')
df2.to_csv('precipitations_elevees.csv')
print("################ Filtre df3 ##########")
df3 = df[df["nom_dept"].notnull()]
df4 = df3[df3["temp_moy"].notnull()]


plt.figure(figsize=(10, 6))
plt.bar(df4['nom_dept'], df4['temp_moy'])
plt.xlabel('Meteo')
plt.ylabel('Température en degrés')
plt.title('Evolution de la temperature')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
