import numpy as np

tableau = np.arange(1, 11)
print(tableau)

# Multiplication par  de 2
print("\n#########Mutliplication par fonction #######\n")
fTableau = np.multiply(tableau, 2)
print(fTableau)

print("\n#########Mutliplication par chiffre #######\n")
mTableau = np.array(tableau)*2
print(mTableau)

print("\n#########Somme #######\n")
sumTableau = np.sum(tableau)
print(sumTableau)

print("\n#########Chiffre paire #######\n")
paire = np.where(tableau % 2 != 0)
print(paire)

print("\n#########Chiffre superieur 5 #######\n")
sup5 = np.where(tableau > 5)
print(sup5)

print("\n#########Creation tableau 2d #######\n")
nTableau = np.arange(1, 28).reshape(3, 9)
print(nTableau)

print("\n#########Ligne sum #######\n")
print(np.sum(nTableau, axis=1))

print("\n#########Colonne sum #######\n")
print(np.sum(nTableau, axis=0))

print("\n#########Remodeler #######\n")
rTableau = np.reshape(nTableau, (27,))

print("\n#########Ajout element #######\n")
aTableau = np.append(rTableau, [28, 29, 30])
print(aTableau)
