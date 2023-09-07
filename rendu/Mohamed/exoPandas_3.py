#! /usr/bin/env python3

import pandas as pd


#############
# Exercice exPandas1.1.txt
#
# Creation de deux Dictionnaire et DataFrame
#############################################
etudiant = {"Id": [1, 2, 3, 4, 5],
            "Nom": ["Paul", "Alice", "Dominique", "Fabien", "Alexandra"],
            "Age": [25, 35, 45, 22, 19]
            }
note = {"Id": [1, 2, 3, 4, 5],
        "Français": [11.5, 16, 18.5, None, None],
        "Mathématique": [10, 14.5, 9.5, None, None],
        "Dessin": [12.5, 13, 15.5, None, None],
        "Science physique": [None, 8.5, 14.5, None, 14],
        "Anglais": [10.5, 9, None, None, 13],
        }

df1 = pd.DataFrame(etudiant)
df2 = pd.DataFrame(note)

#############
# Fusion avec deux methode concat/merge
##########################################

print("\n######### Fusion Avec Concat #########\n")
tableau = pd.concat([df1, df2], axis=1)
print(tableau)

print("\n######### Fusion Avec Merge #########\n")
tableau2 = pd.merge(df1, df2)
print(tableau2)

#############
# Remplacement des Notes vide par la moyenne de matière
######################################################

print("\n######### Remplacment de donnée  #########\n")
mean = {
    "Français": tableau2.loc[:, "Français"].mean(),
    "Mathématique": tableau2.loc[:, "Mathématique"].mean(),
    "Dessin": tableau2.loc[:, "Dessin"].mean(),
    "Science physique": tableau2.loc[:, "Science physique"].mean(),
    "Anglais": tableau2.loc[:, "Anglais"].mean(),
}
tableau2.fillna(value=mean, inplace=True)
print(tableau2)

#############
# Pivotage de données
######################################################

print("\n######### Utilisation de pivot_table  #########\n")

data = pd.read_csv("rendu/Mohamed/ventes.csv")

df = pd.DataFrame(data)
df.Date = pd.to_datetime(df.Date)
df.Date = df.Date.dt.strftime('%Y-%m')
total = pd.pivot_table(df, index=["Produit"], values=[
                       "Montant"], aggfunc='sum', fill_value=0, columns=["Date"])
print(total)


#############
# Manipulation de données
######################################################
print("\n######### Manipulation de données  #########\n")

email = {"email": ['toto@gmail.com', 'tata@hotmail.com',
                   'titi@yahoo.com', 'titi@outlook.com']}

df = pd.DataFrame(email)
df['domain'] = df['email'].str.extract(r'@(.*)$')
print(df)

#############
# Analyse temporelle
######################################################
print("\n######### Analyse temporelle  #########\n")
data = pd.read_csv("rendu/Mohamed/ventes.csv", index_col="Date", parse_dates=True, header=0)
semaine = data.groupby('Produit').resample('W').mean()
print(semaine[1:100])

semaine.to_csv("Analyse_Temporel.csv")
#############
# Exportation de données
######################################################
print("\n######### Exportation de données  #########\n")
total.to_csv("Resulat_Ventes.csv")
print("Export Resulat_Ventes.csv success")
