import pandas as pd 
#Exercice 1 - Création de DataFrame :
#Créez un DataFrame contenant les informations suivantes sur trois étudiants : Nom, Âge, Matière étudiée. Affichez le DataFrame.
data={'Nom':['Bob','Alice','Charlie'],
      'Age':[33,30,25],
      'Matiere':['Math','Physique','Anglais']}
df=pd.DataFrame(data)

#Exercice 2 - Sélection et filtrage :
#À partir du DataFrame créé dans l'exercice 1, sélectionnez les étudiants dont l'âge est supérieur à 25 ans.
Age_filter = df.loc[(df.Age>25 )]
print(Age_filter)

#Exercice 3 - Calcul de statistiques :
#Calculez la moyenne d'âge des étudiants du DataFrame.
Age_Moyenne= df['Age'].mean()
print (Age_Moyenne)