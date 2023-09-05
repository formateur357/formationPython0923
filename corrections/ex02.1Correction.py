# Fonction pour calculer la moyenne d'âge des étudiants et trouver l'étudiant avec la meilleure moyenne.
def calculer_moyenne_etudiant():
    try:
        # Ouvrir le fichier d'entrée en mode lecture.
        with open("/Users/morganguy/Formation_Workspace/formationPython0923/corrections/etudiants.txt", "r") as fichier_entree:
            lignes = fichier_entree.readlines()
            
            # Ignorer la première ligne (en-tête).
            lignes = lignes[1:]
            
            total_age = 0
            meilleur_etudiant = None
            meilleure_moyenne = 0
            
            for ligne in lignes:
                elements = ligne.strip().split(',')
                nom = elements[0]
                prenom = elements[1]
                age = int(elements[2])
                moyenne = float(elements[3])
                
                # Calculer la moyenne d'âge.
                total_age += age
                
                # Vérifier si cette moyenne est la meilleure jusqu'à présent.
                if moyenne > meilleure_moyenne:
                    meilleure_moyenne = moyenne
                    meilleur_etudiant = (nom, prenom, age, moyenne)
                    
            # Finir de calculer la moyenne d'âge.
            moyenne_age = total_age / len(lignes)
            
            # Ouvrir le fichier de sortie en mode écriture.
            with open("resultats.txt", "w") as fichier_sortie:
                fichier_sortie.write(f"Moyenne d'age des etudiants : {moyenne_age:.2f}\n")
                fichier_sortie.write(f"Etudiant avec la meilleure moyenne :\n")
                fichier_sortie.write(f"Nom : {meilleur_etudiant[0]}\n")
                fichier_sortie.write(f"Prenom : {meilleur_etudiant[1]}\n")
                fichier_sortie.write(f"Age : {meilleur_etudiant[2]}\n")
                fichier_sortie.write(f"Moyenne : {meilleur_etudiant[3]:.2f}\n")

        print("Traitement terminé. Les résultats ont été enregistrés dans 'resultats.txt'.")

    except FileNotFoundError:
        print("Le fichier 'etudiants.txt' n'a pas ete trouve.")
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")
        
# Appel de la fonction principale.
calculer_moyenne_etudiant()
