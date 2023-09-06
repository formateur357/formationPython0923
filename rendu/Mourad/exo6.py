class Employees:
    #initialiser les attribus : emp_id, emp_name, et emp_department.
        def __init__(self) -> None:
                self.emp_id = {}
                self.emp_name = {} 
                self.department  = {} 

    #renseigner les attribus
        def set_id(self, emp_id):
            self.__emp_id = emp_id

        def set_name(self, emp_name):
            self.__emp_name = emp_name

        def set_department(self, department):
            self.__department = department

    #return the attributes
        def get_id(self):
            print (self.__emp_id)
    
        def get_name(self):
            print (self.__emp_name)

        def get_department(self):
            print (self.__department)

    #return the objects state as a string
Employees=Employees()
Employees.set_id("1")
Employees.set_name("Mourad")
Employees.set_department("IT")
Employees.get_id()
Employees.get_name()
Employees.get_department()