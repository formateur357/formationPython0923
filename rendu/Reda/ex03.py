# #################################################
# Entrées / Sorties : Clavier
# #################################################
#
# 1. Lecture de nombres, pour chacun d'entre eux on indique
# s'il est pair ou impair. À l'issue de la saisie (Ctrl-d
# sous Unix ou Ctrl-z sous Windows) on affiche la moyenne
# des nombres entrés
#
#
# 2. Constituer une liste de mots entrés au clavier l'un après l'autre.
# Trier la liste constituée par ordre croissant puis par
# ordre décroissant.
#
# 3. On utilise un Hash pour gérer un stock de voitures.
# Le nom d'une voiture est utilisé comme clef, une valeur saisie au clavier
# vient en + ou - de l'éventuelle valeur deja existante.
#
# 4. On reprend ici l'exercice précédent mais à la fin de la saisie,
# on appelle un fonction qui va calculer la valeur du stock.
# Elle reçoit en paramètre le hash du stock, un hash donnant le
# prix H.T. d'une bouteille de xxxx et le taux de TVA.


# 1. Lecture de nombres, pour chacun d'entre eux on indique
# s'il est pair ou impair. À l'issue de la saisie (Ctrl-d
# sous Unix ou Ctrl-z sous Windows) on affiche la moyenne
# des nombres entrés

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def average(numbers):
    if len(numbers) == 0:
        return None
    return round(sum(numbers) / len(numbers), 2)


def nb_pairsimpairs():
    numbers=[]
    while True:
        number = int(input("Please, enter a number :"))
        if number == 0:
            print ("La moyenne de ces nombres entrés est : ",average(numbers))
            break
        else:
            numbers.append(number)
            # print (numbers)
            if is_even(number):
                print("Le nombre ",number," est pair")
            else: print("Le nombre ",number," est impair")


# 2. Constituer une liste de mots entrés au clavier l'un après l'autre.
# Trier la liste constituée par ordre croissant puis par
# ordre décroissant.

def words_exo():
    words = []
    while True:
        word = input("Please, enter a word :")
        if word == "a":
            words.sort()
            print("Liste des mots entrés dans l'ordre croissant: ",words)
            words.sort(reverse=True)
            print("Liste des mots entrés dans l'ordre décroissant: ",words)
            break
        else:
            words.append(word)
            print (words)



# 3. On utilise un Hash pour gérer un stock de voitures.
# Le nom d'une voiture est utilisé comme clef, une valeur saisie au clavier
# vient en + ou - de l'éventuelle valeur deja existante.

def hash_exo():
    cars = {
        "Toyota": 10,
        "Honda": 5,
        "Ford": 15,
        "Chevrolet": 8,
        "BMW": 3
    }
    print("Cars stock : ", cars)
    while True:
        # var_sentence = input("Please, enter a change in car inventory (car brand, variation) :")
        var_sentence = input("Enter car mark and stock value (e.g. Toyota -5): ")
        key, value_str = var_sentence.split()
        value = int(value_str)

        if key in cars:
            cars[key] += value
            print(f"Stock value for {key} updated to {cars[key]}")
            print("Updated cars stock : ", cars)
        else:
            print(f"{key} not found in our stock")


# ===========================================================================================
# MAIN SCRIPT
# ===========================================================================================

# nb_pairsimpairs()

# words_exo()

hash_exo()