#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pand
montableau = pand.DataFrame({ 'Nom':["Lisa", "Bart", "Nelson"],
				 'Age':[27,25,30],
				 'Matière':["Mathématiques","Histoire","Sport"]})
print(f"mon tableau : \n{montableau}\n")

filtre = montableau['Age'] > 25
print(f"Mon filtre \n{montableau[filtre]}\n")

numberEntries = len(montableau)
somme =	sum(montableau['Age'])
print(f"Somme :{somme} ")

moyenne = somme / numberEntries
print(f"Moyenne :{moyenne} ")
