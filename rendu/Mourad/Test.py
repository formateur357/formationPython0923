
class Restaurant:
    def __init__(self, menu_name,book_table, customer):
        self.menu_name = menu_name
        self.book_table = book_table
        self.customer_ord = customer

     
    def menu_nom(self):
        print('{}'.format(self.menu_name))
    def menu_table(self):
        print(' {}'.format(self.book_table))
    def customer_order(self):
        print(''.format(self.customer_ord))
        

#Print the menu.
#Print table reservations.
#Print customer orders.


restaurant = Restaurant('barbacue', '1','4')

print(restaurant.menu_name)
print(restaurant.book_table)
print(restaurant.customer_ord)
restaurant.menu_nom()
restaurant.menu_table()
restaurant.customer_order()
