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
        "Francais": [11.5, 16, 18.5, None, None],
        "Mathematique": [10, 14.5, 9.5, None, None],
        "Dessin": [12.5, 13, 15.5, None, None],
        "Science physique": [None, 8.5, 14.5, None, 14],
        "Anglais": [10.5, 9, None, None, 13],
        }

df1 = pd.DataFrame(etudiant)
df2 = pd.DataFrame(note)

#############
# Fusion avec deux methode concat/merge
##########################################

# print("\n######### Fusion Avec Concat #########\n")
tableau = pd.concat([df1, df2], axis=1)
# print(tableau)

# print("\n######### Fusion Avec Merge #########\n")
tableau2 = pd.merge(df1, df2)
# print(tableau2)

#############
# Remplacement des Notes vide par la moyenne de matière
######################################################
mean = {
        "Francais": tableau2.loc[:, "Francais"].mean(),
        "Mathematique":  tableau2.loc[:, "Mathematique"].mean(),
        "Dessin":  tableau2.loc[:, "Dessin"].mean(),
        "Science physique":  tableau2.loc[:, "Science physique"].mean(),
        "Anglais":  tableau2.loc[:, "Anglais"].mean() 
}

tableau2.fillna(value=mean, inplace=True)
# print(tableau2)

#############
# Pivotage de données
######################################################

data = pd.read_csv("/Users/morganguy/Formation_Workspace/formationPython0923/rendu/Mohamed/ventes.csv")
df = pd.DataFrame(data)

# df.Date = pd.to_datetime(df.Date)
# df.Date = df.Date.dt.strftime('%Y-%m')
# total = pd.pivot_table(df, index=["Produit"], values=["Montant"], aggfunc='sum', fill_value=0, columns=["Date"])

# print(total)

#############
# Manipulation de données
######################################################
# email = {"email": ['toto@gmail.com', 'tata@hotmail.com',
#                    'titi@yahoo.com', 'titi@outlook.com']}

# df = pd.DataFrame(email)
# df['domain'] = df['email'].str.split('@').str[1]
# df['domain'] = df['email'].str.extract(r'@(.*)$')
# print(df)


#############
# Analyse temporelle
######################################################

# df['MoyenneMobile'] = df['Montant'].rolling(window=7).mean()
data = pd.read_csv("/Users/morganguy/Formation_Workspace/formationPython0923/rendu/Mohamed/ventes.csv", index_col="Date", parse_dates=True, header=0)
semaine = data.groupby('Produit').resample('W').mean()
print(semaine)
#############
# Exportation de données
######################################################

df.to_csv("Resultat_Vente.csv")