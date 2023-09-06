#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# #################################################
# Entrées / Sorties : Fichier
# #################################################
#
# 1. Parcourir l'ensemble des lignes d'un fichier rajouter un commentaire
# dans chacun d'entre eux.
# On choisit ici de remplacer la première ligne par elle même
# suivie d'un commentaire constant.
#

def printlinecomment(tLine, tComment) :
	"""Ajout un commentaire à la ligne"""
	return(f"{tLine}{tComment}\n")

fichierExemple = open(
	"C:\\Users\\mperrette\\Documents\\PROJETS\\23_Formation_python\\exemples_fichiers\\titatitutu.txt", mode='r')
updatedcontent = []
tlLines = fichierExemple.readlines()
fichierExemple.close()
print(list(tlLines))
for tLine in tlLines:
	updatedcontent.append(printlinecomment(tLine,"COMMENTAIRE"))

print(list(updatedcontent))
fichierExemple = open(
	"C:\\Users\\mperrette\\Documents\\PROJETS\\23_Formation_python\\exemples_fichiers\\titatitutu.txt", mode='w')
fichierExemple.writelines(updatedcontent)
fichierExemple.close()
#
# 2. A partir d'un fichier texte, on souhaite calculer le nombre de lignes,
# de mots et de caractères du texte.

def CountLines(lListeLines_):
	nLines_ = 0
	for tEntry in lListeLines_:
		nLines_ +=1
	return nLines_

def CountWords(tSentance_):
	return(tSentance_.count(" ")+1)

def CountChars(tLine_):
	return len(tLine_)

fichierExemple = open(
	"C:\\Users\\mperrette\\Documents\\PROJETS\\23_Formation_python\\exemples_fichiers\\titatitutu.txt", mode='r')

lContenu = fichierExemple.readlines()
nLignes = CountLines(lContenu)

nIndex = 0
nChars = 0
nWords = 0

while nIndex < nLignes:
	nChars += CountChars(lContenu[nIndex])-1 # -1 à cause du \n de fin de ligne
	nWords += CountWords(lContenu[nIndex])
	nIndex += 1

print(list(enumerate(lContenu)))
print(f"Lignes du fichier : {nLignes}")
print(f"mots du fichier : {nWords}")
print(f"Caractères du fichier : {nChars}")

fichierExemple.close()