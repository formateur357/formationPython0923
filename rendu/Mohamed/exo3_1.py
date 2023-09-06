#! /usr/bin/env python3

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
trie_mots()