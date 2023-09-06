#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#Ex 01.2 :

def checkpositive(number_):	# Entier positif
	if number_ < 0:
		raise ArithmeticError("La valeur doit être un entier positif")

print("Le programme vérifie si le nombre est parfait.")
Inputatester = input("entrez un nombre à vérifier?\n")
listeDiviseurs = []
diviseur = 1
sommeParfaite = 0

#Validation input
while 1 :
	try:
		nombreInput = int(Inputatester)
		checkpositive(nombreInput)
		print(f"Test du nombre: {nombreInput} \n")
		break
	except ValueError:
		print("VEUILLEZ ENTRER UN NOMBRE ENTIER VALIDE \n")
		continue

#Check de la liste des diviseurs
while diviseur < nombreInput :
	print(f"Diviseur : {diviseur}\n")
	# Diviseurs propres (pas de reste de division)
	# utiliser le modulo
	if (nombreInput % diviseur) != 0:
		print("Diviseur invalide - pas ajouté à la liste")
	else :
		listeDiviseurs += [diviseur]
		print(f"Liste des Diviseurs mise à jour : \n {listeDiviseurs}")
	diviseur += 1

#Somme des diviseurs
for valeur in listeDiviseurs :
	sommeParfaite += valeur
if sommeParfaite == nombreInput :
	print(f"LE NOMBRE EST BIEN PARFAIT. \n Il est égal à la somme des diviseurs :\n {listeDiviseurs}")
else:
	print(f"LE NOMBRE N'EST PAS PARFAIT. \n Il est différent de la somme des diviseurs :\n {listeDiviseurs}")

