#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#lit le fichier
with open("/formationPython0923/exercices/ex02_1_content/etudiants.txt") as fEtudiants:
	lRegistre = fEtudiants.read().split()
	print(lRegistre)

nindex = 1
nMoyenne = 0
nMoyenneEleve = 0
nAge = 0
while nindex < len(lRegistre) :
	print(lRegistre[nindex])
	nMoyenneEleve = float(list(lRegistre[nindex].split(","))[3])
	nAge += float(list(lRegistre[nindex].split(","))[2])
	if nMoyenneEleve > nMoyenne :
		nMoyenne = nMoyenneEleve
		tNomEleveMoyenne = list(lRegistre[nindex].split(","))[0]
		tPrenomEleveMoyenne = list(lRegistre[nindex].split(","))[1]
	for tDonnee in list(lRegistre[nindex].split(",")):
		print(tDonnee)
	print("\n")
	nindex += 1

nAgeMoy = nAge/4
print(f"AGE MOYEN = {nAgeMoy}")
print(f"{tNomEleveMoyenne} {tPrenomEleveMoyenne} {nMoyenne}")








