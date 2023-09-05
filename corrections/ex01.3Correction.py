from itertools import product

# Définir un dictionnaire avec des clés et des listes de lettres.
donnees = {'1': ['a', 'b'], '2': ['c', 'd']}

# Créer une liste de listes contenant les lettres pour chaque clé.
listes_de_lettres = [donnees[key] for key in donnees]

# Utiliser la fonction product pour générer toutes les combinaisons possibles.
combinaisons = list(product(*listes_de_lettres))

# Afficher les combinaisons.
for combinaison in combinaisons:
    print(''.join(combinaison))
