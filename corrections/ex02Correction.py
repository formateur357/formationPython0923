# 1

# Ouvrir le fichier en mode lecture
# fichier = open("text.txt", "r")
# fichier.close()

# with open("/Users/morganguy/Formation_Workspace/formationPython0923/corrections/text.txt", "r") as fichier:
#     lignes = fichier.readlines()

# # Ouvrir le fichier en mode écriture et ajouter des commentaires
# with open("/Users/morganguy/Formation_Workspace/formationPython0923/corrections/text.txt", "w") as fichier:
#     for i, ligne in enumerate(lignes):
#         # Ajouter un commentaire à chaque ligne
#         fichier.write(ligne.strip() + "\n# Commentaire de ligne\n")
  

#2

# Ouvrir le fichier en mode lecture
with open("/Users/morganguy/Formation_Workspace/formationPython0923/corrections/text.txt", "r") as fichier:
    contenu = fichier.read()

# Calculer le nombre de lignes
nb_lignes = len(contenu.splitlines())

# Calculer le nombre de mots
nb_mots = len(contenu.split())

# Calculer le nombre de caractères
nb_char = len(contenu)

# Afficher les résultats
print("Nombre de lignes:", nb_lignes)
print("Nombre de mots:", nb_mots)
print("Nombre de caractères:", nb_char)
