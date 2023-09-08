#! /usr/bin/env python3

import numpy as np

# Ex 1

arr = np.arange(1, 11, 1)
# print(arr)

# Ex 2

sum = np.sum(arr*2)
# print("sum : ", sum)

# Ex 3

even = arr[arr %2 == 0]
elt_gt_5 = arr[arr > 5]

both = even[even > 5]
# print(f"even : {even}, gt_5 : {elt_gt_5}, both: {both}")

# Ex 4

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

sum_columns = np.sum(arr2d, axis=0)
sum_rows = np.sum(arr2d, axis=1)

# print(f"Somme colonne: {sum_columns}\nSomme Lignes: {sum_rows}")

# Ex 5

arr_reshaped = arr2d.reshape(9)

new_row = np.array([10, 11, 12])

concat = np.vstack((arr2d, new_row))

# print(concat)

# Ex 6

rand_arr = np.random.randint(0, 101, 50)
# print(rand_arr)

# calcul de la moyenne

mean = np.mean(rand_arr)
# print(f"mean: {mean}")

# Trouver la valeur max dans le tableau et sa poition

max = np.max(rand_arr)
max_index = np.argmax(rand_arr)
# print(f"max: {max}\nindex : {max_index}")

# Tier le tableau par ordre croissant

sorted = np.sort(rand_arr)
# print(sorted)

# Ex 7

mat2d = np.random.randint(1, 11, (4, 4))
# print(mat2d)

determinant = np.linalg.det(mat2d)

transpose_mat = np.transpose(mat2d)

# print(f"Determinant = {determinant}\ntranspose = {transpose_mat}")

# Ex 8

rand = np.random.rand(100)
# print(rand)
filtered = rand[rand > 0.5]
filtered2 = filtered[filtered < 0.7]
print(filtered, '\n')
print(filtered2)

rand[rand < 0.2] = 0
rand[rand > 0.8] = 1

print(rand)