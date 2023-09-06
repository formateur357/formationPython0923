stock = {}

try:
    while True:
            nom_voiture = input("entrez le nom de la voiture : ")
            quantite = float(input("Entrez la quantité (+ pour ajouter, - pour réduire : "))
            if nom_voiture in stock:
                 stock[nom_voiture] += quantite
            else:
                stock[nom_voiture] = quantite
except EOFError:
        pass

 print(f"Stock mis à jour : {stock}")