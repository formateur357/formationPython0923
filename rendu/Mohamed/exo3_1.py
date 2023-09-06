#! /usr/bin/env python3
import re

def calcul_moyenne():
    stock_nombre=[]
    try:
      while True:
        try:
            nombre=int(input("Veuillez entrer un nombre (Ctrl-c ou Ctrl-d pour terminer):"))
            stock_nombre.append(nombre)
        except ValueError:
            print("Merci d'entrer un nombre !")
            continue
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass
    moyenne = sum(stock_nombre)/len(stock_nombre)
    print(f"\nla moyenne est de {moyenne}\n")

#calcul_moyenne()

def trie_mots():
    stock_mots=[]
    try:
        while True:
            try:
                nombre=str(input("Veuillez entrer un mot (Ctrl-c ou Ctrl-d pour terminer) :"))
                stock_mots.append(nombre)
            except ValueError:
                print("Merci d'entrer un nombre !")
                continue
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass
    stock_mots.sort()
    print(f"\nOrdre croissant : {stock_mots}\n")
    stock_mots.sort(reverse=True)
    print(f"\nOrdre décroissant : {stock_mots}\n")
#trie_mots()

def calcul_stock(stock):
    total_stock=[]
    for k,v in stock.items():
        print(v)
        quantite=v[0]
        prix=v[1]
        total_stock.append(quantite*prix)
    print(sum(total_stock))
    
def stock_voitures():
    stock_voiture={"clio":[50,20000,20],"porche":[10,200000,20],"audi":[10,200000,20]}
    try:
        while True:
            try:
                voiture=str(input("Veuillez entrer la marque du véhicule (Ctrl-c ou Ctrl-d pour terminer) :"))
                if voiture in stock_voiture:
                    quantite=str(input("Nombre a défalquer du stock ex(-1 ou +1) :"))
                    x = re.search("(-)([0-9])+|(\+)([0-9]+)", quantite)
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
        pass
    except EOFError:
        pass
    print(f"\nStock voiture : {stock_voiture}\n")
    calcul_stock(stock_voiture)
stock_voitures()