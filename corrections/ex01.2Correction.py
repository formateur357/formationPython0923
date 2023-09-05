# Définir une fonction en Python pour vérifier si un nombre est "Parfait" ou non.
def est_parfait(nombre):
    # Initialiser une variable pour stocker la somme des diviseurs positifs.
    somme_diviseurs = 0
    # Parcourir les nombres de 1 à (nombre // 2) + 1 pour trouver les diviseurs positifs.
    for diviseur in range(1, (nombre // 2) + 1):
        # Vérifier si le diviseur est un diviseur du nombre.
        if nombre % diviseur == 0:
            somme_diviseurs += diviseur
            
    # Comparer la somme des diviseurs avec le nombre d'origine pour déterminer s'il est parfait.
    if somme_diviseurs == nombre:
        return True
    else:
        return False

# Exemple d'utilisation de la fonction :
nombre = 9
# Appeler la fonction avec le nombre d'exemple.
resultat = est_parfait(nombre)
# Afficher le résultat.
if resultat:
    print(f"{nombre} est un nombre parfait")
else:
    print(f"{nombre} n'est pas un nombre parfait")
