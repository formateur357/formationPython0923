#! /usr/bin/env python3
# -*- coding: utf-8 -*-
class Employe:
	def __init__(self,emp_id,emp_name,emp_departement):
		self.emp_id = emp_id
		self.emp_name = emp_name
		self.emp_departement = emp_departement
		self.salary = 0
		print(f"CREATE EMPLOYE WITH : \n"
			  f"ID = {self.emp_id}\n NAME = {self.emp_name}\n DEPT = {self.emp_departement}")

	def calculate_salary(self,hours_worked):
		""" Calculate salary for amount of worked hours

		:param hours_worked: integer
		:return:
		"""
		salary = float(hours_worked * 20)
		print(f"Salaire de {self.emp_name} = {hours_worked} * 20 ")
		return salary

class FullTimeEmployee(Employe):
	def __init__(self,emp_id,emp_name,emp_departement,healthinsurance,retirement_plan):
		super().__init__(emp_id,emp_name,emp_departement)
		self.healthinsurance = float(healthinsurance)
		self.retirement_plan = float(retirement_plan)
		print(
			f'This employee works FULL-TIME with benefits : \nRetirement plan : {self.retirement_plan}\nHealth Insurance : {healthinsurance}')

	def calculate_salary(self,hours_worked):
		""" Calculate salary for amount of worked hours

		:param hours_worked: integer
		:return:
		"""
		advantages = self.healthinsurance + self.retirement_plan
		salary = float((hours_worked * 20))
		print(f"Salaire de {self.emp_name} = {hours_worked} * 20 ")
		print(f"Avantages sociaux deduits : {self.emp_name} = {advantages}")
		return float(salary+advantages)

class RH(Employe):
	def __init__(self):


class Manager(Employe):
	def __init__(self,emp_id,emp_name,emp_departement,bonus):
		super().__init__(emp_id,emp_name,emp_departement)
		self.bonus = bonus
		print(f"MANAGER WITH : \n Bonus = {self.bonus}\n")

	def calculate_salary(self,hours_worked):
		""" Calculate salary for amount of worked hours
			Managers get a flat bonus to their salary
		:param hours_worked: integer
		:return:
		"""
		salary = float((hours_worked * 20)+self.bonus)
		print(f"Salaire de {self.emp_name} = {hours_worked} * 20 + {self.bonus}")
		return salary

class Contractor(Employe):
	def __init__(self,emp_id,emp_name,emp_departement,ctr_hourly_rate,ctr_workhours):
		super().__init__(emp_id,emp_name,emp_departement)
		self.ctr_hourly_rate = ctr_hourly_rate
		self.ctr_workhours = ctr_workhours
		print(f"CONTRACTOR at rate : {ctr_hourly_rate} with {ctr_workhours} worked hours per weeks.")

	def calculate_salary(self):
		"""
		Calculate salary for amount of worked days

		:param days_worked: self-explanatory (only integers)
		:return:
		"""
		print(f"Salaire de {self.emp_name} = {self.ctr_hourly_rate} * {self.ctr_workhours}")
		return float(self.ctr_hourly_rate*self.ctr_workhours)


Henri = FullTimeEmployee(151,"HENRI","Logistique")
Cécile = FullTimeEmployee(241,"CECILE","Achats")

Michel = Manager(561,"MICHEL","Achats",250)
Jean = Manager(774,"JEAN","Logistique",150)

Vadim = Contractor(1445,"VADIM_C","Logistique")
Pietro = Contractor(2866,"PIETRO_C","Logistique")

for salarie in [Henri,Cécile,Michel,Jean,Vadim,Pietro]:
	if type(salarie) == Contractor:
		print(f"Salaire de {salarie.emp_name} : {salarie.calculate_salary(5)}")
	else:
		print(f"Salaire de {salarie.emp_name} : {salarie.calculate_salary(35)}")


