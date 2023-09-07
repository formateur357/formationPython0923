#! /usr/bin/env python3

import pandas as pd
df = pd.read_csv('/Users/morganguy/Formation_Workspace/formationPython0923/exemples/ventes.csv')
# df = pd.DataFrame(data)
# print(data)
# print(df)
# df.sort_values(by='Profit', inplace=True)

print(df)
print(df['Profit'].sum())
print(df['Profit'].mean())
print(df['Profit'].count())

# new_row = pd.Series({'Mois': '13eme', "Chiffre d'affaires": 15000, "Profit": 10000}, )
df = df.assign(Pertes=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(df)