import requests as http
import numpy as np
import random

# def get_pokemon_evolution_chain(pokemon_id):
#     url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
#     response = requests.get(url) 
    
#     if response.status_code == 200:
#         species_data = response.json()
#         print(species_data)
#         evolution_chain_url = species_data['species']['url']
        
#         evolution_response = requests.get(evolution_chain_url)
        
#         if evolution_response.status_code == 200:
#             evolution_data = evolution_response.json()
#             print(f"Evolution Chain for {species_data['name'].capitalize()}:")
#             print(evolution_data)
#             chain = evolution_data['chain']
#             while chain:
#                 print(chain['species']['name'].capitalize())
#                 chain = chain.get('evolves to', [])[0]
#         else:
#             print("Failed to retrieve evolution chain data.")
#     else:
#         print("API request failed.")

def get_random_pokemon():
    pokemon_id = random.randint(1,300)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    
    response = http.get(url)
    if response.status_code == 200:
        return pokemon_id
        # data = response.json()
        # print("Random Pokemon Information :")
        # print(f"Name: {data['name'].capitalize()}")
        # print("Abilities:")
        # for ability in data['abilities']:
        #     print(f"- {ability['ability']['name'].capitalize()}")
        # print("Types:")
        # for pokemon_type in data['types']:
        #     print(f"- {pokemon_type['type']['name'].capitalize()}")
    else:
        print("API request failed.")
        
def get_pokemon_by_evolution():
    pokemonId = np.random.randint(1, 150)
    url = f"https://pokeapi.co/api/v2/pokemon/"
    print(pokemonId)
    response = http.get(url+"1")
    if response.status_code == 200:
        id = response.json()["id"]
        name = response.json()["name"]
        capacity = response.json()["base_experience"]
        # print(f"Le Pokemon {name} a une capacité {capacity} ")
        evalution_chaine = http.get(
            "https://pokeapi.co/api/v2/pokemon/"+str(pokemonId))
        if evalution_chaine.status_code == 200:
            evolution_url = evalution_chaine.json()["evolution_chain"]["url"]
            print(f"{evolution_url}")
            evol = http.get(evolution_url)
            
            if evol.status_code == 200:
                evolution = evol.json()["chain"]["evolves_to"]
                # for n1 in evolution:
                #     print(n1)

if __name__ == "__main__":
    get_pokemon_by_evolution()