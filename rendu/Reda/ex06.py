# Exercice de Classe Python : Gestion des Employés avec Héritage Multiple et Polymorphisme
#
# Dans cet exercice, vous allez créer une hiérarchie de classes Python pour gérer les informations
# des employés et leur paie. L'accent sera mis sur l'héritage multiple et le polymorphisme.
#
# Étape 1 : Classe de Base Employé
#
# Créez une classe de base en Python nommée Employé avec les attributs emp_id, emp_name, et emp_department.
# Étape 2 : Méthodes de Calcul de Salaire
#
# Implémentez deux méthodes de calcul de salaire dans la classe Employé :
# calculate_salary : Cette méthode prend hours_worked en argument et calcule le salaire de l'employé en fonction du nombre d'heures travaillées. Utilisez un taux horaire de 20 $ par heure pour les employés réguliers.
# Étape 3 : Classe Manager
#
# Créez une classe nommée Manager qui hérite de Employé. Les managers ont un attribut supplémentaire, bonus,
# qui est un montant fixe ajouté à leur salaire.
# Étape 4 : Calcul de Salaire pour les Managers
#
# Implémentez la méthode calculate_salary pour les managers, qui inclut le montant du bonus.
# Étape 5 : Classe Contractor
#
# Créez une classe nommée Contractor qui hérite également de Employé. Les contractuels sont payés à un tarif journalier fixe de 200 $, quelle que soit la durée de travail.
# Étape 6 : Calcul de Salaire pour les Contractuels
#
# Implémentez la méthode calculate_salary pour les contractuels.
# Étape 7 : Polymorphisme
#
# Démontrez le polymorphisme en créant des instances d'Employé, de Manager, et de Contractor
# et en calculant leurs salaires à l'aide de la méthode calculate_salary.
# Montrez que chaque type d'employé calcule son salaire différemment.


class Employee:
    """An abstract Employee"""
    def __init__(self, emp_id, emp_name, emp_department) -> None:
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_department = emp_department

    # Implémentez deux méthodes de calcul de salaire dans la classe Employé :
    # calculate_salary : Cette méthode prend hours_worked en argument et
    # calcule le salaire de l'employé en fonction du nombre d'heures travaillées.
    # Utilisez un taux horaire de 20 $ par heure pour les employés réguliers.

    def calculate_salary(self,hours_worked,hourly_rate_employee):
        # print ("Calcul salaire employé")
        return hourly_rate_employee*hours_worked


# Étape 3 : Classe Manager
# Créez une classe nommée Manager qui hérite de Employé. Les managers ont un attribut supplémentaire, bonus,
# qui est un montant fixe ajouté à leur salaire.


class Manager(Employee):
    def __init__(self, emp_id, emp_name, emp_department, bonus):
        super().__init__(emp_id, emp_name, emp_department)
        self.bonus = bonus
    # Étape 4 : Calcul de Salaire pour les Managers
    # Implémentez la méthode calculate_salary pour les managers, qui inclut le montant du bonus.

    def calculate_salary(self,hours_worked,hourly_rate_manager):
        # print("Calcul salaire manager")
        return (hourly_rate_manager*hours_worked)+self.bonus

# Étape 5 : Classe Contractor
# Créez une classe nommée Contractor qui hérite également de Employé.
# Les contractuels sont payés à un tarif journalier fixe de 200 $, quelle que soit la durée de travail.


class Contractor(Employee):
    def __init__(self, emp_id, emp_name, emp_department):
        super().__init__(emp_id, emp_name, emp_department)

    # Étape 6 : Calcul de Salaire pour les Contractuels
    # Implémentez la méthode calculate_salary pour les contractuels.
    def calculate_salary(self):
        # print("Calcul salaire contractor")
        return 200



# ===========================================================================================
# MAIN SCRIPT
# ===========================================================================================

# Some variables..
hourly_rate_employee = 20
hourly_rate_manager = 25
bonus_manager = 200
nb_hours_employee = 10
nb_hours_manager = 10
nb_hours_contractor = 5

# Étape 7 : Polymorphisme
# Démontrez le polymorphisme en créant des instances d'Employé, de Manager, et de Contractor

print("======== POPULATING ==========")
employee_1 = Employee(1,"Alain","Compta")
manager_1 = Manager(2,"Bernard","Achats",bonus_manager)
contractor_1 = Contractor(3,"Charles","IT")

# et en calculant leurs salaires à l'aide de la méthode calculate_salary.
# Montrez que chaque type d'employé calcule son salaire différemment.

# calculate_salary by class (Employee, Manager, Contractor)

# my_class = type(employee_1)
# my_class_name = employee_1.__class__.__name__
# print("my_class: ",my_class_name.lower())

print (f"\n{str(employee_1.emp_name)} est un {employee_1.__class__.__name__.lower()}. Il a gagné {employee_1.calculate_salary(nb_hours_employee,hourly_rate_employee)}, en travaillant {nb_hours_employee} heures. ")
print (f"\n{str(manager_1.emp_name)} est un {manager_1.__class__.__name__.lower()}. Il a gagné {manager_1.calculate_salary(nb_hours_manager,hourly_rate_manager)}, en travaillant {nb_hours_manager} heures. ")
print (f"\n{str(contractor_1.emp_name)} est un {contractor_1.__class__.__name__.lower()}. Il a gagné {contractor_1.calculate_salary()}, en travaillant {nb_hours_contractor} heures. ")
