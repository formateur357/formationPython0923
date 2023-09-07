#! /usr/bin/env python3

class Employee:
    def __init__(self, emp_id, emp_name, emp_department) -> None:
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_department = emp_department
        
    def calculate_salary(self, hours_worked):
        hourly_rate = 20
        return hours_worked * hourly_rate
    
class Manager(Employee):
    def __init__(self, emp_id, emp_name, emp_department, bonus) -> None:
        super().__init__(emp_id, emp_name, emp_department)
        self.bonus = bonus
        
    def calculate_salary(self, hours_worked):
        base_salary = super().calculate_salary(hours_worked)
        return base_salary + self.bonus
    
class Contractor(Employee):
    def __init__(self, emp_id, emp_name, emp_department) -> None:
        super().__init__(emp_id, emp_name, emp_department)
        
    def calculate_salary(self, days_worked):
        daily_rate = 200
        return daily_rate * days_worked
    
def calculate_and_print_salary(employee, time_worked):
    salary = employee.calculate_salary(time_worked)
    print(f"{employee.emp_name}'s salary: ${salary:.2f}")
    
employee1 = Employee("E001", "John", "RH")
manager1 = Manager("M001", "Alice", "Operations", 1000)
contractor1 = Contractor("C001", "Bob", "IT")

hours_worked = 45
days_worked = 10
calculate_and_print_salary(employee1, hours_worked)
calculate_and_print_salary(manager1, hours_worked)
calculate_and_print_salary(contractor1, days_worked)
