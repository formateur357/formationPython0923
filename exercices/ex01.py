#################################################
#Affichages et boucles
#################################################

#1. Écrire une boucle qui affiche les entiers de 1 à 10. Utiliser
#d'abord une boucle while puis essayer avec une boucle for.
#Généraliser au sein d'une fonction avec un paramètre.
#Définir un tableau d'entiers, puis un tableau de mots.
#Proposer une fonction permettant d'afficher le contenu de tels tableaux.

#1 - Boucle While :
#print('WHILE : ')
#nombre = 1
#while nombre < 11 :
#	print(nombre)
#	nombre = nombre+1

#2 - boucle For :
#print('FOR : ')
#listeundix = range(1,10)
#for nombre in listeundix :
#	print(nombre)


def ListeEntiers(type) :
	bReturn = True
	print(type)
	if type == "WHILE" :
		nombre = 1
		while nombre < 11:
			print(nombre)
			nombre = nombre + 1
	elif type == "FOR" :
		listeundix = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		for nombre in listeundix :
			print(nombre)
	else :
		bReturn = False
	return(bReturn)

#ListeEntiers("WHILE")
#ListeEntiers("FOR")

listeundix = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listemots = ["lundi", "mardi","mercredi"]
def ListeContenuTableau(Tableau) :
	for entier in Tableau:
		print(entier)

def AfficherTableau(type_) :
	if type_ == "entiers" :
		ListeContenuTableau(listeundix)
	elif type_ == "mots":
		ListeContenuTableau(listemots)

print("entiers : \n")
AfficherTableau("entiers")
print("jours : \n")
AfficherTableau("mots")