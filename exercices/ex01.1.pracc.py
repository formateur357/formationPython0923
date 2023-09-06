#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random

#génère un nombre aléatoire entre 1 et 100 (inclus)
def InitJeunombre100() :
	"""Initialise un entier aleatoire entre 1 et 100"""
	nNombreMystère = random.randint(0,100)
	return nNombreMystère

#donner des indices pour aider l'utilisateur à deviner, tels que "Trop bas" ou "Trop élevé"
def CheckNombre(nNombreJoueur_,nNombreMystere_) :
	print(f"Vous avez entré : {nNombreJoueur_}")
	if nNombreJoueur_ == nNombreMystere_ :
		return True
	elif int(nNombreJoueur_) > int(nNombreMystere_) :
		print("Le nombre Mystère est plus petit, essayez encore !")
		return False
	elif int(nNombreJoueur_) < int(nNombreMystere_) :
		print("Le nombre Mystère est plus grand, essayez encore !")
		return False

#compter le nombre de tentatives nécessaires pour deviner correctement le nombre.

#Le jeu continue tant que le joueur ne demande pas à quitter
def ManageInput(Input) :
	if Input == "QUITTER" :
		return True
	else :
		nombreInput = int(Input)
	return False

#Demander un nombre :

#print("Bienvenue dans 'le nombre Mystère' \n Devinez le nombre mystère entre 1 et 100 \n.")
#nThisNumber = InitJeunombre100()
#nIteration = 0
#bTrouve = False
#while  bTrouve == False :
#	nIteration += 1
#	nombreInput = input("votre choix?\n")
#	if ManageInput(nombreInput) == True :
#		print("Abandon après ")
#		nIteration -= 1
#		break
#	bTrouve = CheckNombre(nombreInput, nThisNumber)

#print(f"{nIteration} essais.")

help(InitJeunombre100)

try :
	num = 10/0
except ValueError()
	print("ERROR")