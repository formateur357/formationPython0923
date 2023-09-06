#! /usr/bin/env python3

class Restaurant:
    def __init__(self) -> None:
        self.menu_items = {}
        self.book_table = {}
        self.customer_orders = []
        
    def add_item_to_menu(self, item_name, item_price):
        self.menu_items[item_name] = item_price
        print(f"Addes {item_name} to the menu for {item_price:.2f}$")
        
    def book_tables(self, table_number, customer_name, reservation_time):
        if table_number not in self.book_table:
            self.book_table[table_number] = {"Customer Name": customer_name, "Reservation Time": reservation_time}
            print(f"Table {table_number} booked for {customer_name} at {reservation_time}.")
        else:
            print(f"Table {table_number} is already reserved.")
            
    def customer_order(self, table_number, order_items):
        if table_number in self.book_table:
            self.customer_orders.append({"Table Number": table_number, "Ordered Items": order_items})
            print(f"Order taken for table {table_number}: {', '.join(order_items)}")
        else:
            print(f'Table {table_number} does not have a reservation.')
            
    def display_menu(self):
        print("Restaurant Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: {price:.2f}$")
            
    def display_table_reservations(self):
        print("Table Reservations:")
        for table, reservation in self.book_table.items():
            print(f"Table {table} - Reserved for {reservation['Customer Name']} at {reservation['Reservation Time']}.")

    def display_customer_orders(self):
        print("Customer Orders:")
        for order in self.customer_orders:
            print(f"Table {order['Table Number']} - Ordered Items: {', '.join(order['Ordered Items'])}")
            
restaurant = Restaurant()
restaurant.add_item_to_menu("Burger", 8.99)
restaurant.add_item_to_menu("Pizza", 10.99)
restaurant.book_tables(1, "John", "7:00 PM")
restaurant.book_tables(2, "Alice", "8:00 PM")
restaurant.customer_order(1, ["Burger", "Pizza"])
restaurant.customer_order(3, ["Salad"])
restaurant.display_menu()
restaurant.display_table_reservations()
restaurant.display_customer_orders()