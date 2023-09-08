# Exercice - Analyse de données météorologiques :
#
# Imaginez que vous avez un fichier JSON appelé "meteo.json" qui contient des données météorologiques quotidiennes pour un departement francais.
# Le fichier JSON contient des objets avec les attributs suivants : nom_dept, date, temp, temp_max, temp_min, humidity (en %).
#
# Partie 1 - Chargement des données :
#
# Importez la bibliothèque Pandas.
#
# Chargez le fichier JSON "meteo.json" dans un DataFrame.
#
# Affichez les cinq premières lignes du DataFrame pour avoir un aperçu des données.
#
# Partie 2 - Analyse des données :
#
# Calculez la température moyenne quotidienne en ajoutant une nouvelle colonne "temp_moy" au DataFrame.
#
# Trouvez la journée la plus chaude (température maximale la plus élevée) et la journée la plus froide (température minimale la plus basse).
#
# Calculez la moyenne des précipitations pour l'ensemble des données.
#
# Partie 3 - Filtrage des données :
#
# Créez un nouveau DataFrame contenant uniquement les données des jours où les précipitations étaient supérieures à 10 millimètres.
#
#
# Partie 4 - Exportation des résultats :
#
# Exportez le DataFrame résultant après le filtrage des précipitations élevées dans un fichier CSV appelé "precipitations_elevees.csv".
#
# Partie 5 - Visualisation (Bonus avec matplotlib):
#
# Utilisez Pandas pour créer un graphique de ligne montrant l'évolution de la température maximale au fil du temps.
#
# Créez un graphique à barres montrant le total des précipitations pour chaque mois de l'année.

import pandas as pd
import json
import matplotlib.pyplot as plt

# Ouvrir le fichier JSON et charger les données dans un dictionnaire
with open('meteo.json', 'r') as f:
    data = json.load(f)

# Créer un DataFrame à partir du dictionnaire
df = pd.DataFrame(data['results'])

# Afficher les cinq premières lignes du DataFrame (Par défaut, sinon passer le nbre de lignes en paramètre
print(df.head())

# Remplacer les valeurs nulles dans la colonne "temp_max" et "temp_min" par 0
df['temp_max'] = df['temp_max'].fillna(0)
df['temp_min'] = df['temp_min'].fillna(0)

# Calculer la température moyenne quotidienne
df['temp_moy'] = (df['temp_max'] + df['temp_min']) / 2

# Trouver la journée la plus chaude et la journée la plus froide
jour_plus_chaud = df.loc[df['temp_max'].idxmax()]
jour_plus_froid = df.loc[df['temp_min'].idxmin()]

print("Journée la plus chaude :", jour_plus_chaud['date'])
print("Journée la plus froide :", jour_plus_froid['date'])

# Calculer la moyenne des précipitations
moy_precipitations = df['humidity'].mean()
print("Moyenne des précipitations :", moy_precipitations)

# Créer un nouveau DataFrame contenant les données des jours avec des précipitations supérieures à 10 mm
df_precipitations_elevees = df[df['humidity'] > 10]

# Exporter le DataFrame résultant dans un fichier CSV
df_precipitations_elevees.to_csv('precipitations_elevees.csv', index=False, encoding='utf-8-sig')


# ==========================================================================================================
# BONUS : GRAPHIQUES
# ==========================================================================================================

# Créer une figure avec deux sous-graphiques
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Définir les noms des mois : objectif remplacer les numéros de mois par leurs noms
months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre',
          'Décembre']

# Premier sous-graphique : évolution de la température maximale au fil du temps...
df.plot(x='date', y='temp_max', kind='line', ax=ax1)

ax1.set_title('Evolution de la température maximale')
ax1.set_xlabel('Date')
ax1.set_ylabel('Température maximale (°C)')

# Deuxième sous-graphique : total des précipitations pour chaque mois de l'année
df['mois'] = pd.DatetimeIndex(df['date']).month
df.groupby('mois')['humidity'].sum().plot(kind='bar', ax=ax2)
ax2.set_title('Total des précipitations par mois')
ax2.set_xlabel('Mois')
ax2.set_ylabel('Précipitations (mm)')

# Ajuster l'espacement entre les sous-graphiques et les marges
fig.tight_layout(pad=2)

# Afficher le graphique
plt.show()