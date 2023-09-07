#! /usr/bin/env python3

# ex1
import pandas as pd

data = {
    'Nom': ['Alice', 'Bob', 'Charlie'],
    'Age': [15, 20, 25],
    'Matiere Etudiee': ['Maths', 'Physique', 'Informatique']
}

df = pd.DataFrame(data)

# print(df)

#ex2

# filtre = df['Age'] > 25
# etudiants_age_sup_25 = df[filtre]

# print(etudiants_age_sup_25)

#ex3

moyenne_age = df['Age'].mean()

print(f"Moyenne d'age : {moyenne_age}")