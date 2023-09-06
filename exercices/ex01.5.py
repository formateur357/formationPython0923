#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def square(number):
	"""Retourne le carré du nombre entré"""
	return pow(number,2)

listetest = range(1,20)
print(f"liste : {list(map(print,listetest))}")

listesquared = list(map(square,listetest))

catListe = list(zip(listetest,listesquared))
print(f"Resultat (nombre , carré correspondant):\n {catListe}")