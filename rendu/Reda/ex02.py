#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#################################################
# Entrées / Sorties : Fichier
#################################################

# 1. Parcourir l'ensemble des lignes d'un fichier rajouter un commentaire
# dans chacun d'entre eux.
# On choisit ici de remplacer la première ligne par elle même
# suivie d'un commentaire constant.
#
#
# 2. A partir d'un fichier texte, on souhaite calculer le nombre de lignes,
# de mots et de caractères du texte.


# ============================================================================================================
# new requirement :
# récupérer toutes les lignes d'un fichier et insérer un commentaire après chaque ligne


# ouvrir fichier test.txt
raw_file = open("test.txt", mode='r')


def two_steps_method(file):
    # mettre toutes les lignes du fichier dans une liste
    lines_list = file.readlines()
    print(lines_list)

    # insérer un commentaire incrément après chaque ligne
    occ_comment = 1
    with open(file.name, 'w') as f:
        for line in lines_list:
            f.write(line.strip() + '\n')
            f.write('# **** comment : {}\n'.format(occ_comment))
            occ_comment += 1

# ===========================================================================================


def one_steps_method(file):
    with open(file.name, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        occ_comment = 1
        for line in lines:
            f.write(line.strip() + '\n')
            f.write('# **** comment : {}\n'.format(occ_comment))
            occ_comment += 1
        f.truncate()


def calc_lines(file):
    """ calculer le nombre de lignes de file"""
    return len(file.readlines())

def calc_char(file):
    """ calculer le nombre de lignes de file"""
    with open(file.name, 'r') as f:
        contents = f.read()
        num_chars = len(contents)
        #print("Number of characters:", num_chars)
    return num_chars


# ===========================================================================================
# MAIN SCRIPT
# ===========================================================================================

two_steps_method(raw_file)

# one_steps_method(raw_file)


raw_file.close()
raw_file = open("test.txt", mode='r')

print (" nb lignes: ", calc_lines(raw_file))

nb_carac = calc_char(raw_file)
print("Number of characters: ", nb_carac)
