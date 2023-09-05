# Définir une fonction pour élever un nombre au carré
def carre(x):
    return x ** 2

# Créer une liste de nombres
nombres = [1, 2, 3, 4, 5]
# Utiliser la fonction map() pour élever au carré chaque élément de la liste
nombre_carres = list(map(carre, nombres))

# Afficher les nombres au carré
print("liste d'origine :", nombres)
print("liste au carre :", nombre_carres)