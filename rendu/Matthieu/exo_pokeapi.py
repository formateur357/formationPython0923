#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# https://pokeapi.co/api/v2/pokemon/{name_or_id}

import requests

def getPokemon(input):
	rooturl="https://pokeapi.co/api/v2/pokemon/"+str(input)+"/"
	# Envoyer une requete GET
	response = requests.get(rooturl)

	# Verifier si la requete a reussi (statut 200 OK)
	if response.status_code == 200:
		data = response.json()  # Convertir la reponse JSON en dictionnaire
		name = data['name']
		for slot in data['types']:
			pktype = slot['type']['name']	#.type.name
			print(pktype)
		# for index in dictypes:
		# 	typedico
		# slots = dictypes['slots']
		# typespkm = dictypes['types']
		# # listtypes = types['types']
		# techniques = data['abilities']
		# print(f"Nom pokemon = {name}\n")
		# print(f"{slots} {typespkm}")
	# print(f"Contenu: {data['body']}")
	else:
		print("Aucun enregistrement trouvé pour cet identifiant")

nameorId = input("Entrez un nom ou ID de pokemon : ")
try:
	nameorId = int(nameorId)
	print(f"Vous recherchez le pokemon correspondant à l'ID '{nameorId}'")
except ValueError:
	print(f"Vous recherchez le pokemon nommé '{nameorId}'")

getPokemon(nameorId)

# abilities
# base_experience
# forms
# game_indices
# height
# held_items
# id
# is_default
# location_area_encounters
# moves
# name
# order
# past_types
# species
# sprites
# stats
# types
# weight