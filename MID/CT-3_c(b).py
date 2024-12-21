class students:
     def __init__(self,student_id,major):
          self.student_id=student_id
          self.major=major

     def display_student_info(self):
          print(f"Student ID: {self.student_id}, Major: {self.major}")

student_1=students("22101132","CSE")
student_1.display_student_info()


class Employee:
     def __init__(self, employee_name):
          self.employee_name=employee_name

class Manager(Employee):
     def __init__(self, employee_name,department):
          super().__init__(employee_name)
          self.department=department
     
     def show_manager_details(self):
          print(f"Name : {self.employee_name}, Department : {self.department}")
     
Employee_1=Manager("faisal","IT")
Employee_1.show_manager_details()

