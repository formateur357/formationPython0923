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
print(np.sort(tableau))

print("\n########## Matrice ############\n")
a = np.random.randint(1, 11, (4, 4))
det = np.linalg.det(a)
trans = np.transpose(a)
print(trans)

print("\n########## Filtrage ############\n")
b = np.random.rand(100)
supp = np.where(b > 0.5, b, "")
inf = np.where(b < 0.7, b, "")
print(f"Superieur 0.5 : {supp}\n")
print(f"Inferieur 0.7 : {inf}\n")

print("\n########## Remplacement de donnée ############\n")
b = np.where(b < 0.2, 0, b)
b = np.where(b > 0.8, 1, b)
print(b)
