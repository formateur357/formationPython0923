import pandas as pd

data = pd.read_json('C:/Formation_Python/meteo.json')
#print(data.head(5))
df=pd.json_normalize(data["results"])
filter_temp=df['temp'].notnull()
resultat=df[filter_temp]

#Calculez la température moyenne quotidienne en ajoutant une nouvelle colonne "temp_moy" au DataFrame.
print(resultat)

