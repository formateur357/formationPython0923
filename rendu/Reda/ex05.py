#! /usr/bin/env python3

# Exercise: Restaurant Class
#
# Design a Python class named Restaurant with
# attributes like menu_items, book_table, and customer_orders.
# Implement the following methods:
#
# add_item_to_menu: Use this method to add items to the restaurant's menu.
# book_tables: Implement this method to make table reservations.
# customer_order: Use this method to take customer orders.
# Print the menu.
# Print table reservations.
# Print customer orders.
# Note: Utilize dictionaries and lists to store the relevant data.

# version mono classe

class Restaurant:
    """An abstract Restaurant"""
    def __init__(self, menu_items, book_table, customer_orders) -> None:
        self.menu_items = []
        self.book_table = {}
        self.customer_orders = {}

    def add_item_to_menu(self, item):
        self.menu_items.append(item)

    def book_tables(self,table_num, book_num):
        self.book_table[table_num] = book_num

    def customer_order(self,order_num, order_lib):
        self.customer_orders[order_num] = order_lib

    def get_menu(self):
        # menu = '\n'.join(self.menu_items)
        return ('\n'.join(self.menu_items))

    def get_resa(self):
        result = ''
        for key, value in self.book_table.items():
            result += f'{key}: {value}\n'
        return result

    def get_orders(self):
        result = ''
        for key, value in self.customer_orders.items():
            result += f'{key}: {value}\n'
        return result

# ===========================================================================================
# MAIN SCRIPT
# ===========================================================================================

resto = Restaurant(5,4,3)
print(f"{str(resto.menu_items)}")
print(f"{str(resto.book_table)}")
print(f"{str(resto.customer_orders)}")

print("======== POPULATING ==========")

resto.add_item_to_menu("Entrée")
resto.add_item_to_menu("Plat")
resto.add_item_to_menu("Dessert")
print(f"menu_items : {str(resto.menu_items)}")

resto.customer_order("1","Commande de M.Georges")
resto.customer_order("2","Commande de M.Alain")
resto.customer_order("3","Commande de M.Lama")
resto.customer_order("4","Commande de M.Arnaud")
print(f"customer_orders : {str(resto.customer_orders)}")

resto.book_tables('8', 'M.Georges')
resto.book_tables('7', 'M.Alain')
resto.book_tables('6', 'M.Lama')
resto.book_tables('5', 'M.Arnaud')
print(f"book_table : {str(resto.book_table)}")

# Print the menu
print(f"\n\nThe menu today :\n{str(resto.get_menu())}\n\n")

# Print table reservations.
print(f"Table reservations :\n{str(resto.get_resa())}\n\n")

# Print customer orders.
print(f"Customer orders :\n{str(resto.get_orders())}\n\n")