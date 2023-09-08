#! /usr/bin/env python3

import numpy as np

# creer un tableau 1d ou 2d 

arr1d = np.array([1, 2, 3, 4, 5, 6])
arr1d2 = np.array([0, 3, 4, 5, 6, 8])
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
# print(concatenated)

# sauvegarder un tableau dans un fichier
# np.save("newTab.npy", reshaped)

# Charger un tableau depuis un fichier
# loaded = np.load('newTab.npy')

# print(loaded)

# operation de filtrage et de masquage

mask = arr1d > 5
filtered_data = arr1d[mask]

# calcul statistique

median = np.median(arr1d)
std = np.std(arr1d)
correlation = np.corrcoef(arr1d, arr1d2)
covariance = np.cov(arr1d, arr1d2)

print(f"median: {median}\nstd : {std}\ncorrelation: {correlation}\ncovariance: {covariance}")

# Indexation avancee
index = [1, 2, 4]
selected = arr1d[index]


# utilisation avec matplotlib

# import matplotlib.pyplot as plt

# x = np.linspace(0, 10, 100)
# y = np.sin(x)
# plt.plot(x, y)
# plt.show()

# vitesse des calculs vectorise superieurs a une boucle for classique
arr = np.random.rand(10000000)
# result = arr* 2
# for ar in arr:
#     result = ar  * 2
    
steps = np.random.normal(0, 1, 1000)
position = np.cumsum(steps)

print(position)