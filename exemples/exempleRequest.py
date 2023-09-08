#! /usr/bin/env python3

import requests

# exemple de requete avec GET

def get_exemple():
    url = "https://reqres.in/api/users"
    
    # Envoyer une requete GET
    response = requests.get(url)
    
    # Verifier si la requete a reussi (statut 200 OK)
    if response.status_code == 200:
        data = response.json() # Convertir la reponse JSON en dictionnaire
        print(f"Titre: {data['data']}")
        # print(f"Contenu: {data['body']}")
    else:
        print("la requete a echoue")
        
def put_exemple():
    url = "https://reqres.in/api/users/1"
    data = {'id': 1, 'email': 'george.blob@reqres.in', 'first_name': 'George', 'last_name': 'Blob', 'avatar': 'https://reqres.in/img/faces/1-image.jpg'}
    
    # envoyer une requete PUT
    response = requests.put(url, json=data)
    
    # Verifier si la requete a reussi
    
    if response.status_code == 200:
        created_post = response.json()
        print(created_post)
    else:
        print("la requete a echoue") 
        

put_exemple()
get_exemple()
