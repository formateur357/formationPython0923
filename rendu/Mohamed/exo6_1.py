
class Employee:
    
    def __init__(self,id=0,name=None,department=None) -> None:
        self.emp_id=id
        self.emp_name=name 
        self.emp_department=department 
        
    def calculate_salary(self,hours_worked) -> int:
        return hours_worked*20
        
class Manager(Employee):
    
    def __init__(self,id=0,name=None,department=None,bonus=0) -> None:
        super().__init__(id,name,department)
        self.bonus=bonus
    def calculate_salary(self,hours_worked) -> int:
        salaire=super().calculate_salary(hours_worked)
        return salaire+self.bonus
    
class Contractor(Employee):
    def __init__(self,id=0,name=None,department=None) -> None:
        super().__init__(id,name,department)
    def calculate_salary(self,hours_worked) -> int:
        return hours_worked*200
    
salariee = {"Employee": Employee(id="Em1",name='Elodie',department="compta"),"Manager": Manager(id="Mng1",name='Jean',department="ventes",bonus=1500),"Contractor":Contractor(id="Crt1",name='Pierre',department="standard")}
hours_days= [45,10]
for k,v in salariee.items():
    content= f"{v.emp_name} ="
    if k == "Contractor":
        print(content,f"{v.calculate_salary(hours_days[1])}€")
    else:
        print(content,f"{v.calculate_salary(hours_days[0])}€")

