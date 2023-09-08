#! /usr/bin/env python3
import numpy as np

print("\n########## Création de tableau #########\n")
tableau = np.random.randint(1, 100, 50)
print(tableau)

print("\n########## Moyenne ############\n")
moyenne = np.mean(tableau)
print(moyenne)

print("\n########## Max éléments ############\n")
vmax = np.amax(tableau)
indice = tableau.argmax()
print(tableau.argmax())

print("\n########## Tri tableau ############\n")
sort = np.sort(tableau)
print(f"\nCroissant \n {sort}\n")
print(f"\nDécroissant \n {sort[::-1].argsort()}\n")
print(f"\nDécroissant \n {-np.sort(-tableau)}\n")

print("\n########## Matrice ############\n")
a = np.random.randint(1, 11, (4, 4))
det = np.linalg.det(a)
trans = np.transpose(a)
print(trans)

print("\n########## Filtrage ############\n")
b = np.random.rand(100)
filtre = np.where(b > 0.5, np.where(b < 0.7, b, 0), 0)
print(filtre)

print("\n########## Remplacement de donnée ############\n")
b = np.where(b < 0.2, 0, np.where(b > 0.8, 1, b))
print(b)
