#! /usr/bin/env python3
import re

def calcul_moyenne():
    stock_nombre=[]
    try:
      while True:
        try:
            nombre=int(input("Veuillez entrer un nombre :"))
            stock_nombre.append(nombre)
        except ValueError:
            print("Merci d'entrer un nombre !")
            continue
    except KeyboardInterrupt:
            moyenne = sum(stock_nombre)/len(stock_nombre)
            print(f"\nla moyenne est de {moyenne}\n")

#calcul_moyenne()

def trie_mots():
    stock_mots=[]
    try:
        while True:
            try:
                nombre=str(input("Veuillez entrer un mot :"))
                stock_mots.append(nombre)
            except ValueError:
                print("Merci d'entrer un nombre !")
                continue
    except KeyboardInterrupt:
            stock_mots.sort()
            print(f"\nOrdre croissant : {stock_mots}\n")
            stock_mots.sort(reverse=True)
            print(f"\nOrdre décroissant : {stock_mots}\n")
#trie_mots()

def stock_voitures():
    stock_voiture={"clio":[50,20000,20],"porche":[10,200000,20],"audi":[10,200000,20]}
    try:
        while True:
            try:
                voiture=str(input("Veuillez entrer la marque du véhicule :"))
                keys = list(stock_voiture.keys())
                if voiture in keys:
                    quantite=str(input("Nombre a défalquer du stock ex(-1 ou +1) :"))
                    x = re.search("(-)([0-9])+|\(+)([0-9]+)", quantite)
                    if x.group()[0] == "-":
                        newstock = stock_voiture[voiture][0]-int(x.group()[1])
                        stock_voiture[voiture][0] = newstock
                    if x.group()[0] == "+":
                        newstock = stock_voiture[voiture][0]+int(x.group()[1])
                        stock_voiture[voiture][0] = newstock
                else:
                    print("Merci d'entrer un nom de voiture existant !")
                    continue
            except ValueError:
                print("Merci d'entrer une chaine de str !")
                continue
    except KeyboardInterrupt:
            print(f"\nStock voiture : {stock_voiture}\n")
stock_voitures()