#! /usr/bin/env python3

import pandas as pd

# data = {'Nom': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 35]}

# s = pd.Series([10, 20, 30, 40, 50])

# print("s[2:4] =", s[2:4])

# df = pd.DataFrame(data)

# print(str(df))

df = pd.read_csv('/Users/morganguy/Formation_Workspace/formationPython0923/exemples/ventes.csv')

# .loc et .iloc pour acceder a une ligne par index ou par etiquette
# print(df.loc[1:4, ['Mois', 'Profit']])

# # Pour afficher les premieres lignes
# print(df.head(), '\n')

# # Pour afficher les informations sur la dataframe
# print(df.info(), '\n')

# # Pour afficher les statistiques de base
# print(df.describe(), '\n')

# Pour filtrer les donnees on construit notre filtre puis on l'applique en passant par l'index.
# filtre = df['Profit'] > 3000

# resultat = df[filtre]

# print(resultat)

df['Pertes'] = [1000, 2000, 3000, 1000, 2000, 3000, 1000, 2000, 300, 1000, 2000, 3000]

df.rename(columns={'Profit': 'Gain'}, inplace=True)

df.drop("Chiffre d'affaires", axis=1, inplace=True)

print(df)

df.to_csv('nouvelles_ventes.csv', index=False)