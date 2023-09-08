# Exercice 1 : Création de tableaux
# Énoncé : Créez un tableau NumPy 1D contenant les nombres de 1 à 10 (inclus) et affichez-le.
#
# Exercice 2 : Opérations de base
# Énoncé : À l'aide du tableau que vous avez créé dans l'exercice 1, effectuez les opérations suivantes :
#
#    Multipliez tous les éléments par 2.
#    Calculez la somme de tous les éléments.
#
# Exercice 3 : Sélection et filtrage
# Énoncé : À l'aide du tableau que vous avez créé dans l'exercice 1, effectuez les opérations suivantes :
#
#    Sélectionnez tous les éléments pairs.
#    Sélectionnez tous les éléments supérieurs à 5.
#
# Exercice 4 : Opérations sur des tableaux 2D
# Énoncé : Créez un tableau NumPy 2D de forme (3, 3) contenant des nombres de 1 à 9. Ensuite, effectuez les opérations suivantes :
#
# Calculez la somme de chaque colonne.
# Calculez la somme de chaque ligne.
#
# Exercice 5 : Manipulation de forme
# Énoncé : À l'aide du tableau que vous avez créé dans l'exercice 4, effectuez les opérations suivantes :
#
# Remodelez le tableau en une forme (9,).
# Ajoutez une nouvelle ligne contenant des nombres de 10 à 12.
#
# Concaténez verticalement le tableau original avec la nouvelle ligne

import numpy as np

# Exercice 1 : Création de tableaux
arr1d = np.arange(1, 11)
print(arr1d)

# Exercice 2 : Opérations de base
arr1d_mult = arr1d * 2
print("\n",arr1d_mult)
print(arr1d_mult.sum())

# Exercice 3 : Sélection et filtrage
arr1d_pairs = arr1d[arr1d % 2 == 0]
arr1d_sup5 = arr1d[arr1d > 5]
print("\n",arr1d_pairs)
print(arr1d_sup5)

# Exercice 4 : Opérations sur des tableaux 2D
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\narr2d est un tableau à {} dimensions".format(arr2d.ndim))
print(arr2d.sum(axis=0))
print(arr2d.sum(axis=1))

# Exercice 5 : Manipulation de forme
arr1d_re = arr2d.reshape(9,)
print("\n",arr1d_re)

# Exercice 6
new_row = np.arange(10, 13)
arr2d_new = np.vstack((arr2d, new_row))
print("\n",arr2d_new)

# Exercice 7
arr2d_concat = np.concatenate((arr2d, [new_row]))
print("\n",arr2d_concat)

