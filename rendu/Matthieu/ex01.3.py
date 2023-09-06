#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#lister les combinaisons de valeurs de dictionnaire
# 1=[a,b], 2=[c,d], 3=[e,f]
def combinaisondelistes(Liste1,Liste2):
	ListeCombinaisons = []
	print(f"combiner les listes :\n {Liste1} et {Liste2}\n")
	for valeurL1 in Liste1 :
		for valeurL2 in Liste2 :
			ListeCombinaisons += [valeurL1 + valeurL2]
			print(f"Ajout de la valeur {valeurL1 + valeurL2} \n")
	return ListeCombinaisons

DicoExemple = {1: ["a", "b","c"], 2: ["d", "e","f"]}
resultat = combinaisondelistes(DicoExemple[1],DicoExemple[2])
for combinaison in resultat:
	print(combinaison)
