liste_mots = []

try:
    while True:
        mot = input("saisir des mots :")
        liste_mots.append(mot)
except EOFError:
        pass

liste_mots_asc = sorted(liste_mots)

liste_mots_desc = sorted(liste_mots, reverse=True)

print("Mots triés par ordre croissant :")
for mot in liste_mots_asc:
    print(mot)

print("Mots triés par ordre décroissant :")
for mot in liste_mots_desc:
    print(mot)
