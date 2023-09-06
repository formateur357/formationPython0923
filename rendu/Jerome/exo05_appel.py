from exo05_classe import Restaurant

restaurant = Restaurant()

restaurant.add_item_to_menu("Pâtes", 12.50)
restaurant.add_item_to_menu("Côte de Boeuf", 18.90)
restaurant.add_item_to_menu("Falafel", 14)

restaurant.book_table(1, "Pierre", "20:00")
restaurant.book_table(2, "Paul", "20:30")

restaurant.customer_order("Pierre", ["Falafel", "Pâtes"])
restaurant.customer_order("Paul", ["Côte de Boeuf"])

restaurant.print_menu()
restaurant.print_table_reservations()
restaurant.print_customer_orders()