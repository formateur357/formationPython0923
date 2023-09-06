#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Design a Python class named Restaurant with attributes:
# menu_items,
# book_table,
# customer_orders

class Restaurant:
	"""Le grand restaurant (ou le petit bistrot du coin)"""
	def __init__(self, menu_items, book_table, customer_orders) -> None :
		self.menu_items 		= menu_items
		self.book_table 		= book_table
		self.customer_orders 	= customer_orders

	# Implement the following methods:
	# add_item_to_menu: Use this method to add items to the restaurant's menu.

	def add_item_to_menu(self,item_, price_):
		"""Ajoute un plat au menu
		Paramètres attendus :
			item_  (string) : Nom du plat
		"""
		self.menu_items.append[item_]
		print(f"Ajout de l'item '{item_}' au menu ")

# book_tables: Implement this method to make table reservations.
	def book_tables(self,tableNumber_):
		"""Reserve une table
		Paramètres attendus :
			tableNumber_  (int) : Numero de table (doit exister dans la liste)
		"""
		if tableNumber_ in self.book_table:
			self.book_table[tableNumber_] = True
			print(f"TABLE {tableNumber_} Réservée\n")
		else:
			raise ValueError(f"Numero de table '{tableNumber_}' inconnu!")

# customer_order: Use this method to take customer orders.

	def customer_order(self,item_,itemNumber_,tableNumber_):

		if tableNumber_ in self.book_table[tableNumber_]:
			self.book_table[tableNumber_] = True
			print(f"TABLE {tableNumber_} Réservée\n")
		else:
			raise ValueError(f"Numero de table '{tableNumber_}' inconnu!")

		if item_ in self.menu_items:
			order = {tableNumber_,item_,itemNumber_}
		else:
			raise ValueError(f"Plat non référencé '{item_}'")
		self.customer_orders.append(order)


# Print the menu.
	def printmenu(self):
		for item in self.menu_items:
			print(f"| {item} |")
# Print table reservations.


# Print customer orders.


bistrot = Restaurant(["oeuf mimosa","andouillette triple A"],[10,11,12,13,14,15],{})
#newOrder = bistrot.customer_order("oeuf mimosa",2,10)
bistrot.printmenu()
bistrot.book_tables(10)

