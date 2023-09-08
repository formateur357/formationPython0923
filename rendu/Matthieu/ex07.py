#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

# Exercice 1 : Création de tableaux
# Énoncé : Créez un tableau NumPy 1D contenant les nombres de 1 à 10 (inclus) et affichez-le.

tableau1d = np.arange(1,11,1)
print(tableau1d)

# Exercice 2 : Opérations de base
# Énoncé : À l'aide du tableau que vous avez créé dans l'exercice 1, effectuez les opérations suivantes :

# Multipliez tous les éléments par 2.
tableaumultip2 = tableau1d * 2
print(tableaumultip2)

# Calculez la somme de tous les éléments.
tableausum = sum(tableau1d)
print(tableausum)

# Exercice 3 : Sélection et filtrage
# Énoncé : À l'aide du tableau que vous avez créé dans l'exercice 1, effectuez les opérations suivantes :

# Sélectionnez tous les éléments pairs.
conditionpair = np.mod(tableau1d, 2)==0
conditionimpair = np.mod(tableau1d, 2)!=0
tableaupairs = np.extract(conditionpair, tableau1d)
tableauimpairs = np.extract(conditionimpair, tableau1d)

print(tableaupairs)
print(tableauimpairs)
# Sélectionnez tous les éléments supérieurs à 5.
TableauSup5 = np.extract(tableau1d>5, tableau1d)
print(TableauSup5)

# Exercice 4 : Opérations sur des tableaux 2D
# Énoncé : Créez un tableau NumPy 2D de forme (3, 3) contenant des nombres de 1 à 9. Ensuite, effectuez les opérations suivantes :

print("------------------\n"
	  "tableau2D\n"
	  "------------------\n")

tableau2d = np.arange(1,10).reshape(3,3)
print(tableau2d)

sommesColonnes = tableau2d.sum(axis=0)
for somme in sommesColonnes:
	print(somme)
sommesLignes = tableau2d.sum(axis=1)
print(sommesLignes)
# Calculez la somme de chaque colonne.
# Calculez la somme de chaque ligne.
#
# Exercice 5 : Manipulation de forme
# Énoncé : À l'aide du tableau que vous avez créé dans l'exercice 4, effectuez les opérations suivantes :
#
# Remodelez le tableau en une forme (9,).

tableauaplatiVerti = tableau2d.reshape(9,1)
tableauaplatiHori = tableau2d.reshape(1,9)
print(tableauaplatiHori)
print(tableauaplatiVerti)

# Exercice 6 : Statistiques simples
# Énoncé : Créez un tableau NumPy 1D de nombres aléatoires entre 0 et 100 (inclus) de longueur 50. Ensuite, effectuez les opérations suivantes :

print("------------------\n"
	  "EX6\n"
	  "------------------\n")

integers = np.random.default_rng().integers(0,100,size=50)
print(integers)

# Calculez la moyenne des éléments.
print(f"moyenne = {integers.mean()}")

# Trouvez la valeur maximale et sa position dans le tableau.
print(f"valeur max = {integers.max()}")

# Triez le tableau par ordre croissant.
integers.sort()
print(f"tableau trié = {integers}")

print("------------------\n"
	  "EX7\n"
	  "------------------\n")

# Exercice 7 : Création de matrices
# Énoncé : Créez une matrice NumPy 2D de forme (4, 4) contenant des nombres entiers aléatoires entre 1 et 10. Ensuite, effectuez les opérations suivantes :

matrice = np.random.default_rng().integers(0,10,size=(4,4))

print(matrice)
# Calculez le déterminant de la matrice.
print(f"determinant : {np.linalg.det(matrice)}")
# Calculez la transposée de la matrice.
print(f"transposee :\n{np.transpose(matrice)}")

# Exercice 8 : Filtrage avancé
# Énoncé : Créez un tableau NumPy 1D de longueur 100 contenant des nombres aléatoires entre 0 et 1. Ensuite, effectuez les opérations suivantes :
#
zerosetuns = np.random.default_rng().random(100,)
print(zerosetuns)

# Trouvez tous les nombres qui sont supérieurs à 0,5 et inférieurs à 0,7.
filtre1 = zerosetuns >0.5
filtre2 = zerosetuns <0.7
tableaufiltre = np.extract(np.logical_and(filtre1,filtre2), zerosetuns)

print(f"Tableau Filtre : \n{tableaufiltre}")
# Remplacez tous les nombres inférieurs à 0,2 par 0 et tous les nombres supérieurs à 0,8 par 1.

zerosetuns[zerosetuns < 0.2] = 0
zerosetuns[zerosetuns > 0.8] = 1

print(f"Tableau propre : \n{zerosetuns}")
