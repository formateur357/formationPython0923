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
where = df.where(df.Age > 35)
print(where)
print("########Filtre par loc###########\n")
loc = df.loc[(df.Age > 35)]
print(loc)
print("########Moyenne d'age###########\n")
Moyenne = df['Age'].mean()
print(Moyenne)
print("########Moyenne Notes###########\n")
Moyenne_note = df['Note'].mean()
print(Moyenne_note)
