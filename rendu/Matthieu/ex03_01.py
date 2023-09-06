#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import atexit

nIteration = 0
nTotal = 0
while 1:
	try:
		nNombreentre = int(input("Entrez un nombre\n"))
	except ValueError:
		print("Merci d'entrer un nombre valide\n")
		continue
	except KeyboardInterrupt:
		print("Abandon du programme")
		break
	except EOFError:
		print(f"Fin de saisie\n La moyenne des nombres entrés est : {float(nTotal/nIteration)}")
		break
	if nNombreentre % 2 == 0:
		print("NOMBRE PAIR\n")
	else:
		print("NOMBRE IMPAIR\n")
	nTotal += nNombreentre
	nIteration += 1
