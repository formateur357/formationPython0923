import pandas as pd
#Exercice 4 - Fusion de DataFrames :
#Créez deux DataFrames avec des informations sur les étudiants (ID, Nom, Âge) 
#et leurs résultats aux examens (ID, Matière, Note). 
#Fusionnez les deux DataFrames en utilisant l'ID comme clé.

Data_Etudiants={'ID_E':[1,2,3],
                'Nom':['Bob','Alice','Charlie'],
                'Age':[33,30,25]}

Data_Resultat={ 'ID_E':[1,2,3],
                'ID_R':[1,2,3],
                'Matière':['Maths','Physique','Anglais'],
                'Note':[[13,17,11],[12,15,18],[10,11,11]]}
df_E=pd.DataFrame(Data_Etudiants)
df_R=pd.DataFrame(Data_Resultat)

#Exercice 5 - Traitement des données manquantes :
#Ajoutez quelques lignes avec des données manquantes à l'un de vos DataFrames créés précédemment 
# (par exemple, des étudiants sans notes d'examen).
df_E.loc[len(df_E)]=['4','Emmanuel','34']
print(df_E)
df =df_E.merge(df_R,on='ID_E',how='left')
print(df)
print(df.isna())
df = df.fillna(df.mean())
# Utilisez Pandas pour remplir les valeurs manquantes par la moyenne des notes de la matière correspondante.
#df_R.loc[len(df_R)]=['4','4',['Maths','Physique','Anglais'],]
#Exercice 6 - Pivotage de données :
#
#Utilisez un DataFrame contenant des données sur les ventes avec les colonnes : Date, Produit, Montant. Utilisez pivot_table pour afficher le total des ventes par produit et par mois.
#
#Exercice 7 - Manipulation de chaînes de caractères :
#
#Créez un DataFrame avec une colonne contenant des adresses e-mail. Utilisez Pandas pour extraire le nom de domaine (par exemple, gmail.com) de chaque adresse e-mail et stockez-le dans une nouvelle colonne.
#
#Exercice 9 - Analyse temporelle :
#
#Utilisez un DataFrame contenant des données temporelles pour calculer la moyenne mobile sur 7 jours des données.
#
#Exercice 10 - Exportation de données :
#
#Prenez l'un de vos DataFrames et exportez-le dans un fichier CSV avec un nom de fichier personnalisé.