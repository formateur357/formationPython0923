# Données d'exemple : un dictionnaire avec des clés et des listes de lettres
data = {'1': ['a', 'b'], '2': ['c', 'd']}

# Initialiser une liste vide pour stocker les combinaisons
combinaisons = []
# Parcourir les clés et les listes de lettres
for cle, lettres in data.items():
    # Créer une nouvelle liste pour stocker les combinaisons étendues
    combinaisons_etendues = []
    
    # Parcourir les combinaisons existantes (ou la liste initiale de lettres pour la première clé)
    for combinaison in combinaisons or lettres:
        # Étendre chaque combinaison existante avec les lettres de la clé actuelle
        for lettre in lettres:
            combinaisons_etendues.append(combinaison + lettre)
            
    # Mettre à jour la liste des combinaisons avec les combinaisons étendues
    combinaisons = combinaisons_etendues

# Afficher les combinaisons
for combinaison in combinaisons:
    print(combinaison)
    
    
# from itertools import product

# # Définir un dictionnaire avec des clés et des listes de lettres.
# donnees = {'1': ['a', 'b'], '2': ['c', 'd']}

# # Créer une liste de listes contenant les lettres pour chaque clé.
# listes_de_lettres = [donnees[key] for key in donnees]

# # Utiliser la fonction product pour générer toutes les combinaisons possibles.
# combinaisons = list(product(*listes_de_lettres))

# # Afficher les combinaisons.
# for combinaison in combinaisons:
#     print(''.join(combinaison))


# Nous commençons avec un dictionnaire nommé donnees contenant des clés et des listes de lettres.

# Nous initialisons une liste vide appelée combinations pour stocker les combinaisons.

# Nous parcourons les éléments du dictionnaire, où chaque clé correspond à une liste de lettres.

# Pour chaque clé et liste de lettres, nous créons une nouvelle liste appelée combinaisons_etendues pour stocker les combinaisons étendues.

# Nous parcourons les combinaisons existantes (ou la liste initiale de lettres pour la première clé).

# Pour chaque combinaison existante, nous l'étendons avec chaque lettre de la liste de lettres actuelle, créant ainsi de nouvelles combinaisons. Ces combinaisons étendues sont ajoutées à la liste combinaisons_etendues.

# Nous mettons à jour la liste des combinaisons (combinations) avec les combinaisons étendues (combinaisons_etendues) pour la clé actuelle.

# Enfin, nous affichons toutes les combinaisons en parcourant la liste combinations et en imprimant chaque combinaison.

# Ce programme génère et affiche toutes les combinaisons de lettres en étendant les combinaisons existantes pour chaque clé du dictionnaire