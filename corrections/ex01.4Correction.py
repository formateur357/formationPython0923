try:
    # Demander à l'utilisateur de saisir un nombre.
    nombre = int(input("Veuillez saisir un nombre : "))
    
    # Afficher le nombre saisi.
    print("Vous avez saisi le nombre: ", nombre)
except KeyboardInterrupt:
    # Gérer l'exception KeyboardInterrupt (Ctrl-C ou Delete).
    print("\nOperation annulee par l'utilisateur")
except ValueError:
    # Gérer l'exception si l'utilisateur entre une valeur non valide.
    print("Erreur : Veuillez saisir un nombre entier valide.")
# Le programme se poursuit normalement après la saisie ou l'exception.



# Explication du code :

# Nous utilisons un bloc try...except pour gérer les exceptions potentielles.

# À l'intérieur du bloc try, nous demandons à l'utilisateur de saisir un nombre à l'aide de la fonction input(). Nous utilisons int() pour convertir l'entrée en un nombre entier.

# Ensuite, nous affichons le nombre saisi à l'écran.

# Nous utilisons except KeyboardInterrupt pour gérer l'exception qui se produit lorsque l'utilisateur annule la saisie en appuyant sur Ctrl-C ou Delete. Dans ce cas, nous affichons un message indiquant que l'opération a été annulée par l'utilisateur.

# Nous utilisons également except ValueError pour gérer l'exception qui se produit si l'utilisateur entre une valeur qui ne peut pas être convertie en nombre entier. Dans ce cas, nous affichons un message d'erreur.

# Après avoir géré l'exception (ou si aucune exception n'est levée), le programme se poursuit normalement.