import pandas as pd

data = pd.read_json('C:/Formation_Python/meteo.json')
#print(data.head(5))
df=pd.json_normalize(data["results"])
Resultat = pd.DataFrame(df)
print(Resultat.head(5))
#  nouvelle colonne "temp_moy" 
Resultat["temp_moy"]=(Resultat['temp_min'] + Resultat['temp_max'])/2
print(Resultat)
# temperature max" 
print(Resultat.loc[:, ["temp"]].max())
# temperature min" 
print(Resultat.loc[:, ["temp"]].min())
# humidité moyenne
print(Resultat.loc[:, ["humidity"]].mean())


