import random

# Écrire une boucle Python qui affiche les entiers de 1 à 10 avec une boucle while

def afficher_entiers_while():
    i = 1
    while i <= 10:
        print(i)
        i += 1
    print('\n')

# Écrire une boucle Python qui affiche les entiers de 1 à 10 avec une boucle for

def afficher_entiers_for():
    for i in range(1, 11, 2):
        print(i)
    print('\n')

# Fonction pour afficher le contenu d'un tableau d'entiers
def afficher_tableau(tableau):
    for element in tableau:
        print(f'{element}\n')
        
# Exemple d'utilisation des fonctions
def exemple():
    rand = random.randint(0, 100)
    print(rand)
    entiers = [23, 45, 6, 89, 0]
    mots = ["hi", "bonjour", "hello"]
    number = input("number ?")
    print(number)
    afficher_entiers_while()
    afficher_entiers_for()
    afficher_tableau(entiers)
    afficher_tableau(mots)
    
exemple()