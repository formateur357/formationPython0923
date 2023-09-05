from itertools import product

# Définir un dictionnaire avec des clés et des listes de lettres.
donnees = {'1': ['a', 'b'], '2': ['c', 'd']}

# Créer une liste de listes contenant les lettres pour chaque clé.
listes_de_lettres = [donnees[key] for key in donnees]

# Utiliser la fonction product pour générer toutes les combinaisons possibles.
combinaisons = list(product(*listes_de_lettres))

# Afficher les combinaisons.
for combinaison in combinaisons:
    print(''.join(combinaison))



#==============================================================================
#Solution sans itertools

def generate_combinations(data, current_key_index=0, current_combination=[]):
    if current_key_index == len(data):
        # If we have processed all keys, print the combination
        print(''.join(current_combination))
        return

    current_key = list(data.keys())[current_key_index]
    letters_for_key = data[current_key]

    for letter in letters_for_key:
        # Add the current letter to the combination
        current_combination.append(letter)

        # Recursively generate combinations for the next key
        generate_combinations(data, current_key_index + 1, current_combination)

        # Remove the last letter to backtrack and try the next letter
        current_combination.pop()

# Sample data: dictionary with keys and lists of letters
data = {'1':['a','b'], '2':['c','d'], '3':['e','f'], '4':['g','h']}

# Start generating combinations
generate_combinations(data)