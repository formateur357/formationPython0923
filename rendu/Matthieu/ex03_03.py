#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# 3. On utilise un Hash pour gérer un stock de voitures.
# Le nom d'une voiture est utilisé comme clef, une valeur saisie au clavier
# vient en + ou - de l'éventuelle valeur deja existante.

dRegistre = {"clio":0,"mégane":0,"sénic":0}

try:
	while 1:
		tNomvoiture = input("Entrez un nom de voiture à gérer :")
		if tNomvoiture in dRegistre :
			print(f"Edition flotte de voiture '{tNomvoiture}'")
			try:
				nNombreaAjouter = int(input(f"Nombre de voitures à rajouter à la catégorie {tNomvoiture} : "))
				dRegistre[tNomvoiture] += nNombreaAjouter
				print(f"Nombre de {tNomvoiture} = {dRegistre[tNomvoiture]}\n")
			except ValueError:
				print("Valeur invalide - ignorée")
				continue
		else:
			print("ERREUR - Nom de voiture inconnu")
			continue
except:
	print("Fin de programme")
	pass


