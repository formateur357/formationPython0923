#! /usr/bin/env python3

#1

# nombres = []
# somme = 0

# try:
#     while True:
#         nombre = float(input("Entrez un nombre (Ctrl-d pour terminer) : "))
#         nombres.append(nombre)
#         somme += nombre
# except EOFError:
#     print("EOF")
#     pass # Arret de la saisie avec Ctrl-d (Unix) ou Ctrl-z (Windows)
# except:
#     print("Bad input. Quitting.")
    
# if nombres:
#     moyenne = somme / len(nombres)
#     print("Moyenne des nombres entres :", moyenne)
# else:
#     print("Aucun nombre n'a ete saisi.")

#2 

# mots = []

# try:
#     while True:
#         mot = input("Entrez un mot (Ctrl-d pour terminer) : ")
#         mots.append(mot)
# except EOFError:
#     pass

# if mots:
#     mots.sort() # Tri en ordre croissant
#     print(f"\nListe triee en ordre croissant {mots}")
#     mots.sort(reverse=True) # Tri en ordre decroissant
#     print(f"\nListe triee en ordre decroissant {mots}")
# else:
#     print("\nAucun mot n'a ete saisi.")

#3-4

stock_voitures = {}
catalogue_prix = {}

def calculer_valeur_stock(stock, prix):
    valeur_stock = 0
    for nom, quantite in stock.items():
        valeur_stock += quantite * prix[nom]
    return valeur_stock

try:
    while True:
        nom_voiture = input("Entrez le nom de la voiture : ")
        quantite = float(input("Entrez la quantite (+ pour ajoutez, - pour reduire)"))
        prix = float(input("Prix de la voiture (en euros) : "))
        if nom_voiture in stock_voitures:
            stock_voitures[nom_voiture] += quantite
        else:
            stock_voitures[nom_voiture] = quantite
        catalogue_prix[nom_voiture] = prix
except EOFError:
    pass
except:
    print("La quantite doit etre numerique.")
    
print(f"Stock de voitures mis a jour : {stock_voitures}")
print(f"La valeur total du stock est de : {calculer_valeur_stock(stock_voitures, catalogue_prix)}")
