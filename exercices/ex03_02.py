#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def printliste(tListe):
	for tMot in tListe:
		print(tMot)

lListeMots = []
while 1:
	try:
		tMotSaisi = input("Veuillez saisir un mot : \n")
	except EOFError:
		print("Fin de saisie.\n")
		lListeCroissant = list(sorted(lListeMots))
		lListeDecroissant = list(reversed(lListeCroissant))
		print("Liste des mots par ordre croissant :")
		printliste(lListeCroissant)
		print("\nListe des mots par ordre décroissant :")
		printliste(lListeDecroissant)
		break
	except:
		print("ERREUR DE SAISIE - ABANDON")
		break
	lListeMots.append(tMotSaisi)
