nombres = []
somme = 0

def pair(nombre):
    if nombre % 2 == 0:
        return "pair"
    else:
        return "impair"

try:
    while True:
        nombre = float(input("Entrez un nombre et faire Ctrl-d pour terminer : "))
        nombres.append(nombre)
        somme += nombre
except EOFError:
    pass

if len(nombres) == 0:
    print("pas de nombre saisi")
else:
    for nombre in nombres:
        print(f"{nombre} est un nombre {pair(nombre)}.")

    moyenne = somme / len(nombres)
    print(f"La moyenne des nombres entrés est : {moyenne}")
