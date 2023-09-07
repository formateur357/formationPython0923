# Exercice 1 - Création de DataFrame :
#
# Créez un DataFrame contenant les informations suivantes sur trois étudiants : Nom, Âge, Matière étudiée. Affichez le DataFrame.
#
# Exercice 2 - Sélection et filtrage :
#
# À partir du DataFrame créé dans l'exercice 1, sélectionnez les étudiants dont l'âge est supérieur à 25 ans.
#
# Exercice 3 - Calcul de statistiques :
#
# Calculez la moyenne d'âge des étudiants du DataFrame.

import pandas as pd

# Créer un dictionnaire contenant les informations sur les étudiants
data = {'Nom': ['Alice', 'Bob', 'Charlie'],
        'Âge': [20, 21, 27],
        'Matière étudiée': ['Mathématiques', 'Informatique', 'Physique']}

# Créer un DataFrame à partir du dictionnaire

df = pd.DataFrame(data)
print ("Liste des étudiants : ")
print(df,"\n")

# Exercice 2 - Sélection et filtrage :
#
# À partir du DataFrame créé dans l'exercice 1, sélectionnez les étudiants dont l'âge est supérieur à 25 ans.

# Sélectionner les étudiants dont l'âge est supérieur à 25 ans
df_selected = df[df['Âge'] > 25]

# Afficher le DataFrame sélectionné
print ("Liste des étudiants dont l'âge est supérieur à 25 ans : ")
print(df_selected,"\n")

# Exercice 3 - Calcul de statistiques :
#
# Calculez la moyenne d'âge des étudiants du DataFrame.

# Calculer la moyenne d'âge des étudiants
mean_age = df['Âge'].mean()

# Arrondir la moyenne d'âge à deux décimales
mean_age = round(mean_age, 2)

# Afficher la moyenne d'âge
print("La moyenne d'âge des étudiants est :", mean_age," ans.\n")


