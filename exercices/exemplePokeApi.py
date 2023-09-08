import requests

def get_pokemon_info(pokemon_name_or_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name_or_id}/"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Pokemon Information:")
        print(f"Name: {data['name'].capitalize()}")
        print("Abilities:")
        for ability in data['abilities']:
            print(f"- {ability['ability']['name'].capitalize()}")
        print("Types:")
        for pokemon_type in data['types']:
            print(f"- {pokemon_type['type']['name'].capitalize()}")
    else:
        print("Pokemon not found or API request failed.")

if __name__ == "__main__":
    pokemon_name_or_id = input("Enter the name or ID of a Pokemon: ")
    get_pokemon_info(pokemon_name_or_id)