#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. Écrire une boucle qui affiche les entiers de 1 à 10. Utiliser
# d'abord une boucle while puis essayer avec une boucle for.
# Généraliser au sein d'une fonction avec un paramètre.

# Définir un tableau d'entiers, puis un tableau de mots.
# Proposer une fonction permettant d'afficher le contenu de tels tableaux.

# ========================================================================
# fonction d'affichage d'entiers entre min et max
# ========================================================================
def affiche_entiers (min,max) :
    """ def de la fonctionv"""
    for i in range(min, max):
        print(i)
        i += 1

# ========================================================================
# fonction d'affichage du contenu de deux tableaux
# ========================================================================
def affiche_tableaux (tab_int, tab_words):
    """""""
    for entiers in tab_int:
        print(entiers)
    for words in tab_words:
        print(words)

# ========================================================================
# fonction d'affichage du contenu des tableaux contenus dans un dico
# ========================================================================
def affiche_tableaux_dico (dico_tableaux):
    for cle in dico_tableaux:
        elt_courant = dico_tableaux [cle]
        print("La liste courante ", cle, "contient les éléments :", elt_courant)
        for element in range (0,len(elt_courant)):
            print(elt_courant[element])
        #print(f"{elt_courant}")
        #print (f"{cle}")

# ========================================================================
# fonction d'affichage du contenu de tableaux et diccos contenus dans un dico
# ========================================================================
def affiche_tableaux_dico2 (dico_tableaux):
    for cle in dico_tableaux:

        elt_courant = dico_tableaux [cle]
        # verif type du prochain élément du dico
        print ("type : ",type (elt_courant))
        if isinstance(elt_courant, list):
            print("La liste courante ", cle, "contient les éléments :", elt_courant)
            for element in range (0,len(elt_courant)):
                print(elt_courant[element])
        elif isinstance(elt_courant, dict):
            print("Le dico courant ", cle, "contient les éléments :", elt_courant)
            for element in elt_courant:
                print(elt_courant[element])
        #print(f"{elt_courant}")
        #print (f"{cle}")

# listes =================================================================
int_list = [1,2,3,4,5]
words_list = ["abc","def","ghe","ijk","lmn"]

# dicos ==================================================================
months = { 1: "Janvier", 2: "Fevrier", 3: "Mars", 4: "Avril", 5: "Mai", 6: "Juin", 7: "Juillet", 8: "August"}
dico_de_tableaux = { 1: int_list, 2: words_list}
dico_de_tableaux2 = { 1: int_list, 2: words_list, 3:months}
# ========================================================================
# while
# ========================================================================
# i=1
# while i <=10:
#         print(i)
#         i += 1

# ========================================================================
# for range
# ========================================================================
#
# ============for i in range (1,11):
# #         print(i)
# #         i += 1
# for liste
# ========================================================================

# nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for nombre in nombres:
#     print(nombre)

# ========================================================================
# for def params
# ========================================================================

#affiche_entiers (3,7)

#affiche_tableaux (int_list, words_list)

#affiche_tableaux_dico (dico_de_tableaux)

affiche_tableaux_dico2 (dico_de_tableaux2)