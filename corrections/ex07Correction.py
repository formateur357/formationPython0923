#! /usr/bin/env python3

import numpy as np

# Ex 1

arr = np.arange(1, 11, 1)
print(arr)

# Ex 2

sum = np.sum(arr*2)
print("sum : ", sum)

# Ex 3

even = arr[arr %2 == 0]
elt_gt_5 = arr[arr > 5]

both = even[even > 5]
print(f"even : {even}, gt_5 : {elt_gt_5}, both: {both}")

# Ex 4

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

sum_columns = np.sum(arr2d, axis=0)
sum_rows = np.sum(arr2d, axis=1)

print(f"Somme colonne: {sum_columns}\nSomme Lignes: {sum_rows}")

# Ex 5

arr_reshaped = arr2d.reshape(9)

new_row = np.array([10, 11, 12])

concat = np.vstack((arr2d, new_row))

print(concat)