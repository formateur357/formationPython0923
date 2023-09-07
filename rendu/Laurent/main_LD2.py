# import sys
#
# #connaitre OS
# # import sys
# # import os
# #
# # os.system("python --version")
# # print("Python version")
# # print(sys.version)
# # print("Version info.")
# # print(sys.version_info)
#
# # ne pas tout importer avec le from
# from sys import version
# # print(f"Python version {version}")
# # print (f"exemple {1+1}")
#
# #TYPE
# # a = 9
# # if a==9:print(a)
# #
# # p = None # init null
# # b = True # boolean
#
# # ’une chaîne de texte "avec des guillemets"’
# # "avec l’apostrophe, les guillemets doivent être \"échappés\""
# # ’avec l\’apostrophe, les guillemets doivent être "échappés"’
# # >>> """un retour
# # ... à la ligne"""
# # ’un retour\nà la ligne’
# # c=  "avec l’apostrophe, les guillemets doivent être \"échappés\""
# # print(c)
#
# # chaine octet en ascii
# # type(b"Content-Type: text/html; charset=utf-8")
#
# # permutation
# # x,y = y,x
#
# # liste
# # names = ["a","b","c"]
# # names[2] --> c (liste commence à 0)
# # names += ["d"] -> ajout
# # del name[2] -> sup
# # names[1:-1] -> borne début liste jusqu'à la fin
# # print(names)
#
# # my_list.append(4)      # Add an element to the end
# # my_list[0] = 0         # Modify an element by index
# # my_list.remove("apple")# Remove an element by value
#
# # DICTONNAIRE (tableau avec index)
# # months = { 1:"janvier", 2:"février", 3:"mars", 4:"avril", 5:"mai", 6:"juin", 7:"juillet", 8:"août", 9:"septembre",10:"octobre", 11:"novembre", 12:"décembre"}
# # print(months[11])
#
# # ensemble
# # # A = {1, 2, 3, 3, 2, 1}
# # # B = {2, 4}
# # # A | B --> comparaison
# # # A ^ B --> ^ = xor
#
# # CONDITION
# # IF
# # t = 12
# # if t < 10:
# # 	temperature = "froid"
# # 	elif t < 20:
# # 	temperature = "tiède"
# # 	else:
# # 	temperature = "chaud"
#
# # if 2 in {1, 2, 3} & {2, 4}:  print("trouvé")
#
# # FOR
# # found = False
# # for name in ["pim", "pam", "poum", "toto"]:
# # if name == "toto": found = True
#
# # for name in ["toto", "pim", "pam", "poum"]:
# # 	if len(name) != 3: continue (ne fait pas la suite (conditon suivante) , reprend la boucle)
# # 	if "m" in name: break
#
# # for m in months:
# # 	if m > 6: break
# # 	print(m, months[m])
#
# # for c in "ok":
# # 	print(c, ord(c))
# # o 111
# # k 107
# # for b in b"ko":
# # 	print(b, chr(b))
# # 107 k
# # 111 o
#
# # WHILE
# # t = 12
# # while t < 20:
# # 	t += 1
#
# # FONCTION
# # def create_point(x, y, z):
# # 	return (x, y, z)
# #
# # create_point(4, 6, 3)
# #
#
# #Exo 1
# # def aff_entier():
# # 	i = 1
# # 	while i <= 10:
# # 		print(i)
# # 		i += 1
# #
# # def aff_entier_for():
# # 	for i in range(1,11):
# # 		print(i)
# #
# # def aff_tab_entier(tableau):
# # 	for element in tableau:
# # 		print(f'{element}\n')
# #
# # def aff_tab_mots(tableau):
# # 	for mot in tableau:
# # 		print(f'{mot}\n')
# #
# # def exemple():
# # 	entiers = [23,45,6,89,0]
# # 	mots =  ["lundi", "mardi", "mercredi", "jeudi"]
# # 	aff_entier()
# # 	aff_entier_for()
# # 	aff_tab_entier(entiers)
# # 	aff_tab_mots(mots)
# # exemple()
#
#
#
# # Exo 1.1
# # import random
# # rand = random.randint(1,100)
# # essaie = 1
# # while essaie < 4:
# # 	print("essaie ", essaie, "/ 3")
# # 	numberStr = input("Devinez un nombre entre 1 et 100 : ")
# # 	try:
# # 		number = int(numberStr)
# # 	except ValueError:
# # 		print("Veuillez entrer un nombre valide")
# # 		continue
# # 	if number < rand:
# # 	 	print("Trop bas. Essayez encore\n")
# # 	elif number > rand:
# # 		print("Trop haut. Essayez encore\n")
# # 	else:
# # 		print("bravo, vous avez devinez le nombre secret en 3 tentatives\n")
# # 		break
# # 	essaie += 1
# # print("Le nombre était : ",rand)
#
#
# # Exo 1.2
# # Définir une fonction en Python pour vérifier si un nombre est "Parfait" ou non.
# # def est_parfait(nombre):
# # 	# Initialiser une variable pour stocker la somme des diviseurs positifs.
# # 	somme_diviseurs = 0
# # 	# Parcourir les nombres de 1 à (nombre // 2) + 1 pour trouver les diviseurs positifs.
# # 	for diviseur in range(1, (nombre // 2) + 1):
# # 		# Vérifier si le diviseur est un diviseur du nombre.
# # 		if nombre % diviseur == 0:
# # 			somme_diviseurs += diviseur
# #
# # 	# Comparer la somme des diviseurs avec le nombre d'origine pour déterminer s'il est parfait.
# # 	if somme_diviseurs == nombre:
# # 		return True
# # 	else:
# # 		return False
# #
# # # Exemple d'utilisation de la fonction :
# # nombre = 9
# # # Appeler la fonction avec le nombre d'exemple.
# # resultat = est_parfait(nombre)
# # # Afficher le résultat.
# # if resultat:
# # 	print(f"{nombre} est un nombre parfait")
# # else:
# # 	print(f"{nombre} n'est pas un nombre parfait")
#
#
# # while True:
# # 	try:
# # 		guess = input("Veuillez saisir un nombre : ")
# # 	except KeyboardInterrupt:
# # 		print("interruption")
# # 		continue
# # 	else:
# # 		print(f"Nombre saisie{guess}")
# # 		break
#
# # from itertools import product
# # dico ={'1':['a','b'], '2':['c','d']}
# # for x, y in product(*dico.values()):
# #     print(x + y)
#
# # FICHIER
# # with open("monfic.txt", "r" ) as fic:
# # 	lignes = fic.readlines()
# #
# # with open("monfic.txt", "w" ) as fic:
# # 	for i, ligne in enumerate(lignes):
# # 		fic.write(ligne.strip() + "\n# Commentaire \n")
# #
# # try:
# # 	nombre = input("Veuillez saisir un nombre : ")
# # except KeyboardInterrupt:
# #     # Gérer l'exception KeyboardInterrupt (Ctrl-C ou Delete).
# #     print("\nOperation annulee par l'utilisateur")
# # nbre = 0
# # tot = 0
# # moy = 0
# # for c in nombre:
# # 	# print(c)
# # 	el = c.strip().split(',')
# # 	ch = el[0]
# # 	if ch != '':
# # 		if (int(ch) % 2) == 0:
# # 			print(f"{ch} est paire")
# # 		else:
# # 	 		print(f"{ch} est impaire")
# # 		nbre += 1
# # 		tot += int(ch)
# # moy = tot / nbre
# # print(f"moyenne {moy}")
#
# class personne:
# 	def __init__ (self,nom,prenom,adresse):
# 		""" Constructeur """
# 		self.nom = nom
# 		self.prenom = prenom
# 		self.adresse = adresse
# 		self.age = ""
#
# 	def afficher(self):
# 		return self.nom, self.prenom,self.adresse
#
# 	def getage(self,age,adresse):
# 		self.age = age
# 		self.adresse = adresse
# 		return self.age, self.adresse
#
# 	def vieillir(self):
# 		self.age += 1
# 		return self.age
#
# # p = personne("dupont","paul","20 rue des lilas - 75001 paris")
# # p.afficher()
# # print(f"\nnom : {p.nom}\nprenom : {p.prenom}\nadresse : {p.adresse}")
# #
# # p.getage(25,"les lilas")
# # print(f"\nage : {p.age}\nadresse : {p.adresse}")
# #
# # p.vieillir()
# # print(f"\nage : {p.age}")
#
# class personneParent:
# 	def __init__ (self):
# 		# personne.__init__(self)
# 		self.enfants = []
#
# 	def ajouterEnfant(self,enfants):
# 		self.enfants.append(enfants)
# 		return self.enfants
#
# 	def estMonEnfant(self,enfants):
# 		return enfants in self.enfants
#
# par = personneParent()
# par.ajouterEnfant("laurent")
# par.ajouterEnfant("paul")
# par.ajouterEnfant("marc")
# print(f"\nenfants : {par.enfants}")
#
# class personneEnfant:
# 	def __init__ (self):
# 		personne.__init__(self)
# 		self.parents = []
#
# 	def ajouterParent(self,parents):
# 		self.parents.append(parents)
# 		return self.parents
#
# enf = personneEnfant()
# enf.ajouterParent("marie")
# enf.ajouterParent("gustave")
# class employe:
# 	def __init__ (self):
# 		""" Constructeur """
# 		self.salarie = {}
# 		self.coutHoraire = 20
#
# 	def calculate_salary(self,emp_id,emp_name,hours_worked,fixe):
# 		self.salarie[emp_id] = {"emp_name":emp_name, "salaire":(hours_worked * self.coutHoraire) + fixe, "emp_fixe":fixe}
#
# 	def afficheSalarie(self):
# 		for emp_id, salarie in self.salarie.items():
# 			print(f"emp {emp_id} - salaire {salarie['emp_name']} à {salarie['salaire']} $ avec fixe {salarie['emp_fixe']} $.")
#
#
# class manager (employe):
# 	def __init__ (self):
# 		""" Constructeur """
# 		fixe = 500
#
# class contrcator(employe):
# 	def __init__ (self):
# 		""" Constructeur """
# 		fixe_contractuel = 100
#
#
# cl = employe()
# ma = manager()
#
# cl.calculate_salary("1","tom",100,0)
# cl.calculate_salary("2","kim",100, 50)
# cl.afficheSalarie()

# import pandas as pd
# data = {'Nom': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 32, 35],
# 		'Matière étudiée': ['Francais', 'Math', 'Physique']	}
# df = pd.DataFrame(data)
# print(str(df))
#
# filtre = df['Age'] > 25
# resultat = df[filtre]
# print(f"\nEtudiants > 25 ans : \n{resultat}")
#
# # moyenneAge = df.describe().loc[['mean']]
# # print(f"\nMoyenne d'age :\n {moyenneAge}")
# moyenneAge2 = df['Age'].mean()
# print(f"\nMoyenne d'age : {moyenneAge2}")

import pandas as pd

data = pd.read_json('meteo.json')
data = pd.json_normalize(data['results'])
df = pd.DataFrame(data)

# 5 premieres lignes
print(df.head(5), '\n')

# Ajouter une nouvelle colonne "temp_moy" au DataFrame.
# Calculez la température moyenne quotidienne
df['tempMoy'] = (df['temp_min'] + df['temp_max']) / 2

filtre = df['nom_dept'] == 'Finistère'
resultat = df[filtre]
print(resultat)

# max
# .loc Sélectionne une ou plusieurs colonne d un dataFrame
print("temp max : ",resultat.loc[:, ["temp_max"]].max())
# ou max = resultat[resultat["temp_max"] == resultat["temp_max"].max()]
# print("temp max2 : ",max)

# min
print("temp min : ",resultat.loc[:, ["temp_max"]].min())

# moy precep
print("prec moy : ",resultat.loc[:, ["humidity"]].mean())

# Filtre humidité > 70
filtre = resultat['humidity'] > 70
resultat = resultat[filtre]
print("Humidité > 50% : ",resultat)

# exportation csv
resultat.to_csv('humidtet_sup_70.csv', index=False)

# Utilisez Pandas pour créer un graphique de ligne montrant l'évolution de la température maximale au fil du temps.
# Créez un graphique à barres montrant le total des précipitations pour chaque mois de l'année.
import matplotlib.pyplot as plt

# plt.figure(figsize=(10, 6))
plt.bar(resultat['date'], resultat['temp_max'])
plt.xlabel('date')
plt.ylabel('temp_max')
plt.title('Evolution des températures par date')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



