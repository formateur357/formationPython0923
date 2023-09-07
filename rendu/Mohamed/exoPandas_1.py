#! /usr/bin/env python3

import pandas as pd
data = {"Prenom": ["Sylvie", "Gilles", "Sylvain"],
        "Age": [18, 23, 45],
        "Note": [12.5, 14, 18.5],
        "matiére": ["Français", "Mathématiques", "Dessin"]}

df = pd.DataFrame(data)
print("########Tableau###########\n")
print(df)
print("########Filtre par Where###########\n")
print(df.where(df.Age > 35))
print("########Filtre par loc###########\n")
print(df.loc[(df.Age > 35)])
print("########Moyenne d'age###########\n")
print(df['Age'].mean())
print("########Moyenne Notes###########\n")
print(df['Note'].mean())
