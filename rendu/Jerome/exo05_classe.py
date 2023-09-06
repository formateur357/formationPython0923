class Restaurant:
    def __init__(self) -> None:
        self.menu_items = {}
        self.booked_tables = {}
        self.customer_orders = []

    def add_item_to_menu(self, item_name, item_price):
        self.menu_items[item_name] = item_price

    def book_table(self, table_number, customer_name, reservation_time):
        self.booked_tables[table_number] = {'customer_name': customer_name, 'reservation_time': reservation_time}

    def customer_order(self, customer_name, items_ordered):
        order = {'customer_name': customer_name, 'items_ordered': items_ordered}
        self.customer_orders.append(order)

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: {price}€")

    def print_table_reservations(self):
        print("Réservations:")
        for table_number, reservation_info in self.booked_tables.items():
            print(f"Table {table_number}: réservée pour {reservation_info['customer_name']} à {reservation_info['reservation_time']}")

    def print_customer_orders(self):
        print("Commandes:")
        for order in self.customer_orders:
            print(f"La commande de {order['customer_name']} : {', '.join(order['items_ordered'])}")