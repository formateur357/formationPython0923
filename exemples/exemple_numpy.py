#! /usr/bin/env python3

import numpy as np

# creer un tableau 1d ou 2d 

arr1d = np.array([1, 2, 3, 4, 5, 6])
arr1d2 = np.array([0, 3, 4, 5, 6])
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# creer un tableau de valeur equidistantes
arr_range = np.arange(0, 90, 9)

arr_random = np.random.rand(3, 3)

# methodes pour Remodeler un tableau 
reshaped = arr1d.reshape((2, 3))


concatenated = np.concatenate((arr1d, arr1d2))

# fonction de math exp, mean, sqrt
result = np.exp(arr1d)
print(concatenated)

# sauvegarder un tableau dans un fichier
np.save("newTab.npy", reshaped)

# Charger un tableau depuis un fichier
loaded = np.load('newTab.npy')

print(loaded)