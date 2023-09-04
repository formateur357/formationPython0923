# Exercice : Deviner le nombre secret

# Écrivez un programme Python qui génère un nombre aléatoire entre 1 et 100 (inclus) et demande à l'utilisateur de deviner ce nombre secret. Le programme devrait donner des indices pour aider l'utilisateur à deviner, tels que "Trop bas" ou "Trop élevé". Le programme doit également compter le nombre de tentatives nécessaires pour deviner correctement le nombre.

# Voici un exemple d'exécution du programme :
# ---------------------------------------
# Bienvenue dans le jeu "Devine le nombre secret" !
# Je vais choisir un nombre entre 1 et 100, et vous devez deviner quel est ce nombre.

# Devinez un nombre : 50
# Trop élevé. Essayez encore.

# Devinez un nombre : 25
# Trop bas. Essayez encore.

# Devinez un nombre : 37
# Bravo ! Vous avez deviné le nombre secret en 3 tentatives.
# -------------------------------------------

# Correction

# Importez la bibliothèque random pour générer un nombre aléatoire.
import random
# Générez un nombre aléatoire entre 1 et 100 inclus.
secret_number = random.randint(1, 100)
# Initialisez le compteur de tentatives.
attempt = 0
print("""Bienvenue dans le jeu "Devine le nombre secret" !
Je vais choisir un nombre entre 1 et 100, et vous devez deviner quel est ce nombre.""")
# Utilisez une boucle while pour permettre à l'utilisateur de deviner jusqu'à ce qu'il trouve le bon nombre.
while True:
    # Demandez à l'utilisateur de deviner un nombre.
    guess = input("Devinez un nombre entre 1 et 100 : ")
    # Assurez-vous que l'entrée de l'utilisateur est un nombre entier.
    try:
        guess = int(guess)
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue
    if guess > 100 or guess < 1:
        print("Veuillez entrer un nombre compris entre 1 et 100.")
        continue
    # Incrémentez le compteur de tentatives.
    attempt += 1
    # Comparez la devinette de l'utilisateur avec le nombre secret.
    if guess < secret_number:
        print("Trop bas. Essayez encore.")
    elif guess > secret_number:
            print("Trop haut. Essayez encore.")
    else:
        # L'utilisateur a deviné correctement, sortez de la boucle.
        print(f'Bravo ! Vous avez devine le nombre secret ({secret_number}).')
        break
