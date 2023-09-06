#! /usr/bin/env python3

##########################
#
#
##########################
class Restaurant:
    
    def __init__(self) -> None:
        self.menu_items={}
        self.book_table={}
        self.customer_orders={}
        self.load_menu()
    ##########################
    #
    #
    ##########################        
    def choice(self) -> None:
        try:
          print("\n##################################")
          print("# Bienvenue au Restaurant happy :)")
          print("##################################\n")
          print("Veuillez selectionner l'action:\n")
          print("1: Ajouter un element au menu\n")
          print("2: Reserver une table\n")
          print("3: Prendre une commande\n")
          print("4: Addition client\n")
          print("0: Pour quitter\n")
          print("Veuillez selectionner l'action:")
          print("_______________________________")
          while True:
            try:
              choices = int(input("Que voulez faire ?:"))
              if choices == 1 :
                  self.add_item_to_menu()
                  break
              elif choices == 2:
                  self.reservations_tables() 
                  break
              elif choices == 3:
                  self.customer_order()
                  break
              elif choices == 4:
                  self.addition_order()
                  break
              else:
                  print("A bientôt")
            except ValueError:
                print('Séléctionnez un choix valide !') 
                continue       
        except EOFError:
            pass
        except KeyboardInterrupt:
            pass
    ##########################
    #
    #
    ##########################             
    def load_menu(self):
        with open("menu.txt","r") as f:
            data = f.read()
            if len(data) > 0:
                for v in data.splitlines():
                    self.menu_items[v.split(":")[0]] = v.split(":")[1]   
    ##########################
    #
    #
    ##########################                         
    def add_item_to_menu(self) -> None:
        listproduit = []
        try:
            while True:
                produit = input("Indiquez le produit a ajouter (nom,prix) (Control-D pour terminer):")
                listproduit=produit.split(",")
                self.menu_items[listproduit[0]]=listproduit[1]
                print(self.menu_items)
        except EOFError:
          pass
        except KeyboardInterrupt:
          pass
        with open("menu.txt","w") as f:
           for key, value in self.menu_items.items(): 
              f.write('%s:%s\n' % (key, value))
        self.choice() 
    ##########################
    #
    #
    ##########################                
    def reservations_tables(self) -> None:
        try:
          while True:
            table = input("Indiquez le nom client et numero de table (numero,nom,heure) (Control-D pour terminer):")
            self.book_table[table.split(",")[0]]=(table.split(",")[1],table.split(",")[2])
            print(self.book_table)
        except EOFError:
          pass
        except KeyboardInterrupt:
          pass
        self.choice() 
    ##########################
    #
    #
    ##########################             
    def customer_order(self) -> None:
        try:
          orders=0
          while True:
            order = input("Prendre la commande (table,item1,item2,...) (Control-D pour terminer):")
            commande=order.split(",")
            table=commande[0]
            if table not in self.book_table:
                print("la table séléctionée n'existe pas ")
                continue
            produit=[]
            for  items in commande:
                if orders != 0:
                    if items in self.menu_items:
                        produit.append(items)
                    else:
                        print(f"Ce produit n'existe pas {items} !")
                        continue
                else:
                    orders +=1
            self.customer_orders[table] = produit
            print(self.customer_orders)
        except EOFError:
          pass
        except KeyboardInterrupt:
          pass
        self.choice() 
    ##########################
    #
    #
    ##########################                    
    def addition_order(self) -> None:
        try:
          while True:
            table = input("Addition client entrez numero de table (Control-D pour terminer):")
            if table not in self.book_table:
                print("la table séléctionée n'existe pas ")
                continue
            print(f"\nPour la table {table} : {self.book_table[table][0]} \n")
            total=[]
            for  items in self.customer_orders[table]:
                    if items in self.menu_items:
                        print("- %s     %s€" % (items,self.menu_items[items]) )
                        total.append(float(self.menu_items[items]))
                        
            print(f"\nTOTAL:     {str(sum(total))}€\n")
        except EOFError:
          pass
        except KeyboardInterrupt:
          pass
        self.choice() 
##########################
# Start restaurant
##########################            
if __name__ == "__main__":
    resto = Restaurant()
    resto.choice()