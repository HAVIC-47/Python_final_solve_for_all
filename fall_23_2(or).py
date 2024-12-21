class Employee:
     def __init__(self, name, age,salary):
          self.name=name
          self.age=age
          self.salary=salary


     def display_details(self):
          print(f"Name: {self.name}")
          print(f"Age: {self.age}")
          print(f"Salary: {self.salary}")

class FullTimeEmployee(Employee):
     def __init__(self, name, age, salary , bonus):
          super().__init__(name, age, salary)
          self.bonus=bonus

     def calculate_total_salary(self):
          return self.salary+self.bonus
     
     def display_details(self):
           super().display_details()
           print(f"Bonus: {self.bonus}")
           print(f"Total Salary: {self.calculate_total_salary()}")
class PartTimeEmployee(Employee):
     def __init__(self, name, age, salary, hours_worked):
          super().__init__(name, age, salary)
          self.hours_worked=hours_worked

     def calculate_payment(self, hourly_rate):
          return self.hours_worked*hourly_rate
     
     def display_details(self):
          super().display_details()
          print(f"Hours Worked: {self.hours_worked}")


FT_employee= FullTimeEmployee("faisal",21,1000000,40000)
FT_employee.display_details()

pt_employee= PartTimeEmployee("sharif_magi", 18,20000,4)
pt_employee.display_details()
print(f"Payment: {pt_employee.calculate_payment(2000)}")

