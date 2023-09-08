#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
étudiants = pd.DataFrame({'ID':list(range(5)),
				   'Nom': ['Alice', 'Bob', 'Charlie','Hector','Francine'],
        		   'Age': [14, 13, 13,12,15]})

# df1 = pd.DataFrame(
#     {
#         "A": ["A0", "A1", "A2", "A3"],
#         "B": ["B0", "B1", "B2", "B3"],
#         "C": ["C0", "C1", "C2", "C3"],
#         "D": ["D0", "D1", "D2", "D3"],
#     },
#     index=[0, 1, 2, 3],
# )

print(étudiants)

notes = pd.DataFrame({'ID':list(range(5)),
				   	'Mathématiques':[12, 13, 15,None,14],
				   	'Français':[14,None,15,18,None],
					'Histoire':[19,14,11,15,16]})
# notes = pd.DataFrame(data=[list(range(3)),[11,15,16],[17,13,13],[15,15,11]],columns=['ID','Mathématiques', 'Français', 'Histoire'])

# notes = notes.fillna(0)
notes.fillna({'Français':notes['Français'].mean(),'Mathématiques':notes['Mathématiques'].mean(),'Histoire':notes['Histoire'].mean()})
print(notes['Français'].mean())
	# noteAjustee = notes.fillna(notes[matiere].mean)
	# print(f"note : {noteAjustee}")

ConcatNoteseleves = pd.merge(étudiants,notes,on='ID')

print(ConcatNoteseleves)